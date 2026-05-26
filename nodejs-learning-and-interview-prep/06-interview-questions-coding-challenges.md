# Chapter 6: Interview Q&As & Coding Challenges

This chapter covers conceptual questions and hands-on coding exercises commonly asked during mid-to-senior level Node.js and backend engineering interviews.

---

## 💬 Part 1: Conceptual Q&A

### Q1: What is the difference between `process.nextTick()` and `setImmediate()`?
*   **`process.nextTick()`** targets the V8 microtask queue. Its callbacks are executed **immediately** after the currently executing JavaScript operation finishes, before the Event Loop transitions to the next phase (or even runs another macro-task).
*   **`setImmediate()`** targets the Libuv event loop Check phase. It schedules a callback to run during the Check phase of the Event Loop cycle, allowing other I/O events, timers, and close handles to be processed first.
*   *Key Takeaway:* `nextTick()` executes faster and can block the event loop if called recursively, whereas `setImmediate()` yields control back to the loop after each callback.

### Q2: What is the Libuv Thread Pool and how does it relate to network I/O?
*   The Libuv thread pool executes blocking operations (such as cryptography, compression, DNS resolution, and local file I/O) that do not have standard, cross-platform non-blocking system calls.
*   **Network I/O does NOT use the Libuv Thread Pool.** Instead, it uses OS-native asynchronous event notification APIs (e.g. `epoll` on Linux, `kqueue` on macOS) to handle connections on the main thread, making it more memory and CPU efficient.

### Q3: Why does `dns.lookup()` behave differently than `dns.resolve()` under load?
*   **`dns.lookup()`** is a blocking operation. Under the hood, it calls the standard OS system library function `getaddrinfo()`, which runs synchronously. Node.js offloads this call to the Libuv thread pool. Under heavy network request loads, this can exhaust the thread pool (default size 4), blocking file reads and crypto operations.
*   **`dns.resolve()`** executes network calls asynchronously. It does not use the system configuration files (like `/etc/hosts`) and instead queries DNS name servers directly using a non-blocking network socket, bypassing the thread pool.

### Q4: Explain the difference between `cluster` and `worker_threads`.
*   `cluster` forks the main Node.js process. Each worker process has its own pid, memory space, and port-sharing proxy. It is best for scaling standard web API applications to maximize multi-core CPU usage.
*   `worker_threads` runs multiple threads within a single process. They share the same process ID and can share memory spaces directly (`SharedArrayBuffer`), avoiding serialization costs. It is best for offloading CPU-intensive JavaScript calculations within a single application.

---

## 💻 Part 2: Practical Coding Challenges

Use these code snippets to study and practice implementation-focused questions.

### Challenge 1: Write a Custom `EventEmitter`
Implement a simple class that mimics Node's native `EventEmitter`. It must support `.on()`, `.emit()`, `.off()`, and `.once()`.

```javascript
class SimpleEventEmitter {
    constructor() {
        this.listeners = {};
    }

    // Subscribe to an event
    on(event, callback) {
        if (!this.listeners[event]) {
            this.listeners[event] = [];
        }
        this.listeners[event].push(callback);
        return this;
    }

    // Publish/Trigger an event
    emit(event, ...args) {
        if (!this.listeners[event]) return false;
        
        // Use a shallow copy to prevent issues if a listener removes itself during execution
        const eventCallbacks = [...this.listeners[event]];
        eventCallbacks.forEach(cb => cb(...args));
        return true;
    }

    // Unsubscribe from an event
    off(event, callback) {
        if (!this.listeners[event]) return this;
        this.listeners[event] = this.listeners[event].filter(cb => cb !== callback);
        return this;
    }

    // Subscribe to run only once
    once(event, callback) {
        const wrapper = (...args) => {
            this.off(event, wrapper); // Unsubscribe first
            callback(...args); // Run original callback
        };
        this.on(event, wrapper);
        return this;
    }
}

// Verification:
const emitter = new SimpleEventEmitter();
const greet = (name) => console.log(`Hello, ${name}!`);

emitter.on('greet', greet);
emitter.emit('greet', 'Alice'); // Hello, Alice!
emitter.off('greet', greet);
emitter.emit('greet', 'Bob');   // (Nothing printed)
```

---

### Challenge 2: Write a Concurrency-Limited Task Queue
Write a function or class that executes a series of asynchronous tasks (represented by functions returning promises) with a maximum concurrency limit.

```javascript
class TaskQueue {
    constructor(concurrencyLimit) {
        this.concurrencyLimit = concurrencyLimit;
        this.queue = [];
        this.activeCount = 0;
    }

    // Add task (function returning a Promise)
    push(task) {
        return new Promise((resolve, reject) => {
            this.queue.push({ task, resolve, reject });
            this.next();
        });
    }

    // Process next tasks in queue
    next() {
        if (this.activeCount >= this.concurrencyLimit || this.queue.length === 0) {
            return;
        }

        const { task, resolve, reject } = this.queue.shift();
        this.activeCount++;

        task()
            .then(resolve)
            .catch(reject)
            .finally(() => {
                this.activeCount--;
                this.next(); // Trigger next queue step
            });
    }
}

// Verification:
const delayTask = (id, ms) => () => new Promise(resolve => {
    console.log(`[Start] Task ${id}`);
    setTimeout(() => {
        console.log(`[End] Task ${id}`);
        resolve(id);
    }, ms);
});

const q = new TaskQueue(2); // Max 2 tasks run concurrently
q.push(delayTask(1, 1000));
q.push(delayTask(2, 500));
q.push(delayTask(3, 300)); // Will queue until Task 2 finishes at 500ms
```

---

### Challenge 3: Create a Custom Promise Implementation
Write a simplified version of the ES6 `Promise` class. (Covers constructor, status transitions, resolver callbacks, `.then()`, and asynchronous chaining).

```javascript
const STATE = {
    PENDING: 'pending',
    FULFILLED: 'fulfilled',
    REJECTED: 'rejected'
};

class MyPromise {
    constructor(executor) {
        this.state = STATE.PENDING;
        this.value = undefined;
        this.onFulfilledCallbacks = [];
        this.onRejectedCallbacks = [];

        const resolve = (value) => {
            if (this.state === STATE.PENDING) {
                this.state = STATE.FULFILLED;
                this.value = value;
                // Run queued callbacks in next tick (async behavior)
                queueMicrotask(() => {
                    this.onFulfilledCallbacks.forEach(cb => cb(this.value));
                });
            }
        };

        const reject = (reason) => {
            if (this.state === STATE.PENDING) {
                this.state = STATE.REJECTED;
                this.value = reason;
                queueMicrotask(() => {
                    this.onRejectedCallbacks.forEach(cb => cb(this.value));
                });
            }
        };

        try {
            executor(resolve, reject);
        } catch (err) {
            reject(err);
        }
    }

    then(onFulfilled, onRejected) {
        // Handle optional arguments
        const realOnFulfilled = typeof onFulfilled === 'function' ? onFulfilled : val => val;
        const realOnRejected = typeof onRejected === 'function' ? onRejected : err => { throw err; };

        // Return a new Promise for chaining
        return new MyPromise((resolve, reject) => {
            const handleCallback = (callback) => {
                try {
                    const result = callback(this.value);
                    if (result instanceof MyPromise) {
                        result.then(resolve, reject);
                    } else {
                        resolve(result);
                    }
                } catch (err) {
                    reject(err);
                }
            };

            if (this.state === STATE.FULFILLED) {
                queueMicrotask(() => handleCallback(realOnFulfilled));
            } else if (this.state === STATE.REJECTED) {
                queueMicrotask(() => handleCallback(realOnRejected));
            } else {
                // Queue callbacks if promise is pending
                this.onFulfilledCallbacks.push(() => handleCallback(realOnFulfilled));
                this.onRejectedCallbacks.push(() => handleCallback(realOnRejected));
            }
        });
    }

    catch(onRejected) {
        return this.then(null, onRejected);
    }
}

// Verification:
new MyPromise((resolve) => setTimeout(() => resolve('Fulfilled!'), 100))
    .then(val => {
        console.log(val); // 'Fulfilled!'
        return 'Chained!';
    })
    .then(val => console.log(val)); // 'Chained!'
```
