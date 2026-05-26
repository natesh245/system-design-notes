# Chapter 2: Asynchronous Patterns & Streams

Node.js is optimized for I/O-bound applications. To prevent performance bottlenecks, you must master asynchronous control flow and the mechanics of streaming data, which allow you to process massive datasets with a minimal memory footprint.

---

## ⏳ Asynchronous Control Flow Evolution

Node.js has evolved through three major paradigms for handling asynchronous logic:

### 1. Callbacks (Error-First)
Historically, the standard in Node.js. The first parameter is reserve for an error object (`err`), and subsequent parameters are for data.
```javascript
const fs = require('fs');

fs.readFile('data.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Failed to read file:', err);
        return;
    }
    console.log('File content:', data);
});
```
*   **Drawback:** Nested asynchronous operations lead to **Callback Hell** (Pyramid of Doom), making error handling and code readability difficult.

### 2. Promises
Introduced in ES6 to solve callback nesting. Represents the eventual completion (or failure) of an asynchronous operation.
```javascript
const fs = require('fs').promises;

fs.readFile('data.txt', 'utf8')
    .then(data => console.log('File content:', data))
    .catch(err => console.error('Error:', err));
```
*   **Unhandled Rejections:** If a promise fails and has no `.catch()` handler, Node.js throws an `unhandledRejection` event. By default, recent Node versions will terminate the process:
    ```javascript
    process.on('unhandledRejection', (reason, promise) => {
        console.error('Unhandled Rejection at:', promise, 'reason:', reason);
        // Recommended: gracefully shut down the server
    });
    ```

### 3. Async / Await
Syntactic sugar built on top of Promises. Allows asynchronous code to be written in a synchronous-looking style using `try/catch` blocks.
```javascript
const fs = require('fs').promises;

async function readFileContent() {
    try {
        const data = await fs.readFile('data.txt', 'utf8');
        console.log(data);
    } catch (err) {
        console.error(err);
    }
}
```

---

## 📢 The Event Emitter Pattern

The `EventEmitter` class (from the built-in `events` module) is the core of Node’s event-driven architecture. Many core modules (e.g., HTTP servers, Streams) inherit from it.

### Basic Usage
```javascript
const EventEmitter = require('events');
const myEmitter = new EventEmitter();

// 1. Subscribe
myEmitter.on('userSignUp', (userId) => {
    console.log(`Sending welcome email to user ${userId}`);
});

// 2. Publish
myEmitter.emit('userSignUp', 42);
```

### Event Emitter Memory Leaks
If you subscribe a callback to an event emitter, the emitter holds a reference to that callback. If the subscribing object is short-lived but the emitter is long-lived (like a global router), the subscribing object cannot be garbage collected, creating a **Memory Leak**.

> [!WARNING]
> By default, if more than **10** listeners are added to a single event on an emitter, Node.js outputs a warning to stderr to prevent potential leaks.

#### Prevention:
*   Unsubscribe listeners when they are no longer needed:
    ```javascript
    const onData = (data) => console.log(data);
    stream.on('data', onData);
    
    // Later when cleaning up:
    stream.off('data', onData); // Or stream.removeListener('data', onData);
    ```
*   Use `once()` if you only need the event to fire once; Node automatically unsubscribes it after execution.

---

## 💾 Buffers vs. Streams

When processing data (like files or network requests), loading the entire file into memory before processing is inefficient.

| Feature | Buffers | Streams |
| :--- | :--- | :--- |
| **Concept** | Temporarily stores a chunk of binary data in memory. | Processes data in sequential chunks over time. |
| **Memory** | Allocates space equal to the size of the whole payload. | Uses a fixed, small buffer memory footprint (e.g. 16KB). |
| **Data Size** | Good for small files/metadata. Limited by V8 Max String/Buffer Size. | Ideal for massive files (GBs), video streaming, or socket data. |
| **Location** | Raw C++ memory (outside the V8 Heap). | Uses Buffer chunks internally to pass data. |

### Buffers: `alloc` vs `allocUnsafe`
*   `Buffer.alloc(size)`: Allocates a buffer of the specified size and fills it with zeros. **Safe, but slower** because it writes to memory first.
*   `Buffer.allocUnsafe(size)`: Allocates a buffer of the specified size **without** clearing the memory. It is **faster**, but the buffer might contain old, sensitive data from previously freed memory, which could lead to data leakage if exposed.

---

## 🌊 Streams: The 4 Core Types

Node.js features 4 main categories of streams:

1.  **Readable:** Streams from which data can be consumed (e.g., `fs.createReadStream`, `http.IncomingMessage`).
2.  **Writable:** Streams to which data can be written (e.g., `fs.createWriteStream`, `http.ServerResponse`).
3.  **Duplex:** Streams that are both Readable and Writable (e.g., TCP sockets, `net.Socket`).
4.  **Transform:** Duplex streams that modify or transform data as it is written and read (e.g., `zlib.createGzip` for compression, `crypto.createCipheriv` for encryption).

---

## 🛑 Backpressure: How to Handle It

Backpressure is a common problem in data streams. It occurs when a **Readable stream** produces data much faster than the **Writable stream** can consume/write it.

If left unhandled, the system will buffer excess data in memory (RAM), eventually exhausting available system memory and crashing the Node.js process with an **Out Of Memory (OOM)** error.

```text
                  [ READABLE STREAM ] (Produces 10MB/s)
                           |
                           v (Pushing chunks)
                === INTERNAL BUFFER === (highWaterMark: 16KB)
                           |
                           v (Attempting to write)
                  [ WRITABLE STREAM ] (Consumes 1MB/s)
                           |
         +-----------------+-----------------+
         | If internal buffer exceeds limit: |
         | 1. Writable.write() returns false |
         | 2. Readable.pause() is called     |
         | 3. Writable empties, emits 'drain'|
         | 4. Readable.resume() is called    |
         +-----------------------------------+
```

### The Backpressure Control Flow (Manual Implementation):
1.  The Readable stream reads data and writes it to the Writable stream: `writable.write(chunk)`.
2.  If the Writable stream's internal queue exceeds its `highWaterMark` (typically 16KB), `write()` returns **`false`**.
3.  The Readable stream must listen to this return value and temporarily pause itself: **`readable.pause()`**.
4.  The Writable stream continues to write its buffered data to the destination.
5.  Once the Writable stream has cleared its buffer queue, it emits a **`'drain'`** event.
6.  The Readable stream listens for the `'drain'` event and resumes fetching data: **`readable.resume()`**.

### Example Code: Manual Backpressure Handling
```javascript
const fs = require('fs');

const readStream = fs.createReadStream('source_large.mp4');
const writeStream = fs.createWriteStream('destination.mp4');

readStream.on('data', (chunk) => {
    // Write data chunk to Writable stream
    const canAcceptMoreData = writeStream.write(chunk);
    
    // If writable's internal buffer is full, pause the read stream
    if (!canAcceptMoreData) {
        readStream.pause();
    }
});

// Once writable has flushed its buffer, resume reading
writeStream.on('drain', () => {
    readStream.resume();
});

readStream.on('end', () => {
    writeStream.end();
});
```

### The Modern Way: `.pipe()` and `pipeline`
Instead of writing manual backpressure checks, use `.pipe()`, which handles it automatically:
```javascript
readStream.pipe(writeStream);
```

However, `.pipe()` does not automatically destroy streams if an error occurs, leading to memory leaks. For production environments, use the built-in **`pipeline`** utility from the `stream` module, which manages cleanup and forwards errors correctly:
```javascript
const { pipeline } = require('stream');
const fs = require('fs');
const zlib = require('zlib');

pipeline(
    fs.createReadStream('large_file.txt'),
    zlib.createGzip(),
    fs.createWriteStream('large_file.txt.gz'),
    (err) => {
        if (err) {
            console.error('Pipeline failed:', err);
        } else {
            console.log('Pipeline succeeded.');
        }
    }
);
```
