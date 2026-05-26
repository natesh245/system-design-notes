# Chapter 5: Web Servers, Frameworks & Security

Building production web servers in Node.js requires deciding on structural middleware frameworks and defending your application from common runtime vulnerabilities like Prototype Pollution, ReDoS, and denial of service (DoS) attacks.

---

## 🛣️ Web Framework Architecture: Express vs. Koa

Node.js provides a low-level native `http` module. To manage complexity, we use framework wrappers. The two classic options, Express and Koa, handle middleware execution differently:

### Express: Linear Callback Flow
Express is built on sequential callbacks. Once a middleware executes, it passes control forward using `next()`. If a middleware performs asynchronous tasks, returning values or catching errors up-stream is difficult because the chain executes linearly.

```text
Request ---> [ Middleware 1 ] ---> [ Middleware 2 ] ---> Route Handler ---> Response
```

### Koa: The "Onion" Model
Koa, created by the same team behind Express, utilizes `async/await` natively. Middlewares act as nested layers. Execution flows down the stack and then flows back up in reverse order once the downstream handlers resolve.

```text
Request ---------------------------------------------> Response
  |                                                      ^
  v                                                      |
[ Middleware 1 ] (Pre-processing)  <--+  [ Middleware 1 ] (Post-processing)
  |                                   |                  ^
  v                                   |                  |
[ Middleware 2 ] (Pre-processing)  <--+  [ Middleware 2 ] (Post-processing)
  |                                                      ^
  +--------> [ Controller/Handler ] ---------------------+
```

#### Koa Onion Example:
```javascript
const Koa = require('koa');
const app = new Koa();

// Middleware 1: Logger (tracks total execution time)
app.use(async (ctx, next) => {
    const start = Date.now();
    await next(); // Wait for downstream middlewares to resolve
    const ms = Date.now() - start;
    console.log(`${ctx.method} ${ctx.url} - ${ms}ms`);
});

// Middleware 2: Authentication
app.use(async (ctx, next) => {
    console.log('Authenticating...');
    await next();
    console.log('Auth check complete.');
});

// Controller
app.use(async ctx => {
    ctx.body = 'Hello World';
});

app.listen(3000);
```

---

## 🔒 Node.js Runtime Security Hardening

Because Node.js runs in a single-threaded runtime environment, security vulnerabilities can easily crash or compromise the entire server.

### 1. Prototype Pollution

#### What is it?
Prototype Pollution occurs when a JavaScript application recursively merges or assigns user-controlled JSON objects into an existing object without validation. A malicious user can pass keys like `__proto__`, polluting the base `Object.prototype` with arbitrary properties.

#### The Exploit Vector:
```javascript
// Malicious payload sent via HTTP POST body:
// { "theme": "dark", "__proto__": { "isAdmin": true } }

function deepMerge(target, source) {
    for (let key in source) {
        if (typeof target[key] === 'object' && typeof source[key] === 'object') {
            deepMerge(target[key], source[key]);
        } else {
            target[key] = source[key];
        }
    }
    return target;
}

const userProfile = {};
deepMerge(userProfile, JSON.parse(payload));

// Inspecting prototype:
const guestUser = {};
console.log(guestUser.isAdmin); // Outputs: true! (Every object in the app is polluted)
```

#### Mitigations:
1.  **Block Magic Keys:** Filter out `__proto__`, `constructor`, and `prototype` keys during merges or JSON parsing.
2.  **Create Objects Without Prototypes:** Use `Object.create(null)` to create dictionary objects that do not inherit from `Object.prototype`.
3.  **Freeze the Prototype:** Freeze the base object prototype at startup:
    ```javascript
    Object.freeze(Object.prototype);
    ```
4.  **Use Modern Map Types:** Use ES6 `Map` objects instead of plain objects for storing dynamic user-controlled keys.

---

### 2. Regular Expression Denial of Service (ReDoS)

#### What is it?
A ReDoS attack occurs when a regular expression uses nested quantifiers (e.g. `(a+)+`) or overlapping groups. If matching fails against a long, malicious string, the regex engine falls into **Catastrophic Backtracking**, checking every permutation of paths. This blocks the single main event loop thread, freezing the server.

#### Example of an "Evil" Regex:
```javascript
const regex = /(a+)+b/; // Dangerous pattern
const maliciousInput = "a".repeat(30) + "X"; // 30 'a's followed by a non-matching char

console.log("Checking regex...");
regex.test(maliciousInput); // This single line will lock up the CPU for minutes!
```

#### Mitigations:
*   Avoid nested quantifiers in regular expressions (e.g., `*`, `+` inside other groups).
*   Use validation libraries like `validator.js` or schemas (Joi, Ajv) rather than writing custom complex regex.
*   Validate and limit the maximum length of user-input strings *before* running regex evaluations.
*   Use analysis tools like `safe-regex` to check expressions for vulnerability before committing them.

---

### 3. Securing HTTP Headers (Helmet)

By default, Node.js HTTP servers expose details (like the `X-Powered-By: Express` header), making it easier for attackers to identify vulnerabilities.

Using the **`helmet`** middleware helps secure your Express app by setting appropriate HTTP headers:
*   `Content-Security-Policy`: Restricts where scripts, styles, and media resources can be loaded from.
*   `Strict-Transport-Security`: Forces clients to connect via HTTPS (SSL/TLS).
*   `X-Frame-Options`: Prevents **Clickjacking** attacks by blocking the site from being loaded inside an iframe on other websites.
*   `X-Content-Type-Options`: Disables MIME-sniffing, preventing browsers from executing files that claim to be text or images but contain scripts.

```javascript
const express = require('express');
const helmet = require('helmet');

const app = express();
app.use(helmet()); // Automatically sets secure defaults
```

---

## 🚦 Rate Limiting at Scale (Distributed)

To prevent brute-force attacks and scraper bots, you must throttle requests. For multi-instance, horizontal systems, you cannot store rate limits in local memory. You must use a shared, fast cache like Redis.

### Sliding Window Log Algorithm (with Redis):

Using Redis sorted sets (`ZSET`), we can track requests within a moving time window:

```javascript
const Redis = require('ioredis');
const redis = new Redis();

async function rateLimiter(ip, limit = 100, windowInSeconds = 60) {
    const key = `rate:${ip}`;
    const now = Date.now();
    const clearBefore = now - (windowInSeconds * 1000);

    // Run transaction
    const multi = redis.multi();
    
    // 1. Remove expired timestamps outside the current window
    multi.zremrangebyscore(key, 0, clearBefore);
    // 2. Count active logs remaining in this window
    multi.zcard(key);
    // 3. Add current timestamp to the log
    multi.zadd(key, now, now);
    // 4. Set expiry to clean up inactive users
    multi.expire(key, windowInSeconds);

    const results = await multi.exec();
    const requestCount = results[1][1];

    if (requestCount > limit) {
        return { allowed: false, count: requestCount };
    }
    return { allowed: true, count: requestCount };
}
```
*   **Why ZSET:** The `ZREMRANGEBYSCORE` command removes older logs, keeping memory consumption low. `ZCARD` counts only valid transactions within the active time window, preventing request spikes.
