# Chapter 1: Node.js Core Architecture & Event Loop

To design high-throughput Node.js applications, you must master its execution model. Interviews often test your deep understanding of how Node.js achieves concurrency using a single main thread, and how it handles asynchronous operations under the hood.

---

## 🏗️ Node.js Architecture: V8 & Libuv

Node.js is not a programming language; it is a runtime environment that wraps the **Google V8 JavaScript Engine** and the **Libuv asynchronous I/O library**, exposing C++ bindings to JavaScript.

```text
+-------------------------------------------------+
|               Node.js Core API                  |
|          (path, fs, http, crypto, etc.)         |
+-------------------------------------------------+
|             Node.js Bindings (C++)              |
+------------------------+------------------------+
|  V8 Engine (Google)    |      Libuv (C)         |
|  - Call Stack          |  - Event Loop          |
|  - Memory Heap         |  - Thread Pool (4)     |
|  - Garbage Collector   |  - Non-blocking I/O    |
+------------------------+------------------------+
|                 Operating System                |
|         (epoll, kqueue, IOCP, Syscalls)         |
+-------------------------------------------------+
```

### 1. The V8 Engine
*   **Role:** Compiles JavaScript source code to native machine code before executing it, manages memory allocation (Heap), and executes JavaScript (Call Stack).
*   **Single-Threaded:** V8 has one Call Stack. Only one line of JavaScript code can run at any given moment on this main thread.

### 2. The Libuv Library
*   **Role:** A multi-platform C library that handles non-blocking asynchronous I/O operations, provides the **Event Loop**, and manages the background **Thread Pool**.
*   **Multi-Threaded:** While JS runs on a single thread, Libuv is highly multi-threaded, executing system tasks, cryptography, and disk reads in the background.

---

## 🔄 The Event Loop: Detailed Phase-by-Phase

The Event Loop is Libuv’s mechanism for scheduling and executing asynchronous callbacks. It runs continuously as long as there are pending tasks (handles or requests).

```text
                  +--------------------------------+
                  |         START OF LOOP          |
                  +--------------------------------+
                                  |
            +---------------------v---------------------+
     +----> | 1. TIMERS                                 | (setTimeout, setInterval)
     |      +---------------------+---------------------+
     |                            |
     |      +---------------------v---------------------+
     |      | 2. PENDING CALLBACKS                      | (Deferred TCP errors, etc.)
     |      +---------------------+---------------------+
     |                            |
     |      +---------------------v---------------------+
     |      | 3. IDLE / PREPARE                         | (Internal Libuv use)
     |      +---------------------+---------------------+
     |                            |  [Blocks if poll queue is empty
     |      +---------------------v---------------------+   & no immediate/timers pending]
     |      | 4. POLL                                   | <--- Incoming I/O (net, fs)
     |      +---------------------+---------------------+
     |                            |
     |      +---------------------v---------------------+
     |      | 5. CHECK                                  | (setImmediate)
     |      +---------------------+---------------------+
     |                            |
     |      +---------------------v---------------------+
     |      | 6. CLOSE CALLBACKS                        | (socket.on('close'), etc.)
     |      +---------------------+---------------------+
     |                            |
     +---------------------[ More work? ]---------------+
                                  | No
                  +---------------v----------------+
                  |          EXIT PROCESS          |
                  +--------------------------------+
```

### Phase Details

1.  **Timers:** Executes callbacks scheduled by `setTimeout()` and `setInterval()` whose thresholds have expired.
2.  **Pending Callbacks:** Executes I/O callbacks deferred from the previous loop iteration (e.g., a TCP socket receives an `ECONNREFUSED` error; some Unix systems defer reporting this error).
3.  **Idle, Prepare:** Used internally by Libuv for system state preparation. No user JavaScript runs here.
4.  **Poll:** 
    *   Retrieves new I/O events (network connections, data reads, file system changes).
    *   Executes callbacks for almost all I/O events.
    *   *Blocking Behavior:* If the poll queue is empty, the Event Loop will block (wait) in this phase for new events to arrive. However, if there are pending `setImmediate` scripts or expired timers, it will exit the Poll phase to execute them.
5.  **Check:** Executes callbacks registered via `setImmediate()`.
6.  **Close Callbacks:** Executes teardown callbacks for closed handles (e.g., `socket.on('close', ...)`).

---

## ⚡ Microtask Queues: nextTick & Promises

A critical source of interview questions is the execution order of microtasks versus the Event Loop phases. **Microtasks are not part of the Libuv Event Loop.** Instead, they are managed by the V8 engine and executed inside Node.js.

### The Two Microtask Queues:
1.  **`process.nextTick()` Queue:** The highest priority queue.
2.  **Promise Queue:** Resolves callbacks from `Promise.resolve().then()` and `async/await` steps.

### Execution Rule:
> [!IMPORTANT]
> The microtask queues are checked and drained **immediately after the current JavaScript operation completes**, regardless of the current phase of the Event Loop. 
> 
> The `process.nextTick` queue is always drained *before* the Promise queue.

### Example Challenge:
```javascript
const fs = require('fs');

fs.readFile(__filename, () => {
    setTimeout(() => console.log('setTimeout'), 0);
    setImmediate(() => console.log('setImmediate'));
    process.nextTick(() => console.log('nextTick'));
    Promise.resolve().then(() => console.log('Promise'));
});
```

#### Order of Execution:
1.  **`nextTick`** (Drained immediately after the `readFile` callback finishes execution, before exiting the Poll phase).
2.  **`Promise`** (Drained immediately after the `nextTick` queue finishes, still before exiting the Poll phase).
3.  **`setImmediate`** (The loop leaves the Poll phase and goes to the Check phase).
4.  **`setTimeout`** (The loop completes the cycle, starts the next iteration, and executes the expired timer in the Timers phase).

*Output:*
```text
nextTick
Promise
setImmediate
setTimeout
```

---

## 🧵 The Libuv Thread Pool

JavaScript execution is single-threaded, but what happens when you read a file from the hard drive or hash a password using bcrypt? These are blocking operations.

Libuv manages a background pool of worker threads to handle synchronous and intensive operations without blocking the main event loop thread.

```text
                  [ MAIN THREAD (Event Loop) ]
                                |
          Does I/O call belong to Thread Pool or OS Kernels?
                     /                      \
      [ Thread Pool Operations ]       [ OS Kernel Operations ]
      - File System (fs.*)             - Network Sockets (TCP/UDP)
      - Crypto (pbkdf2, scrypt)        - HTTP Client/Server requests
      - DNS Lookups (dns.lookup)       - Database connections (network-based)
      - Zlib compression               
                     |                                   |
           +---------+---------+               +---------+---------+
           | Thread | Thread | ...             |  epoll / kqueue   | (OS Event Demultiplexor)
           +---------+---------+               +---------+---------+
```

### Offloaded to Thread Pool
These tasks are passed to Libuv threads because they are CPU-bound or lack universal, non-blocking OS system calls (like disk operations on many platforms):
*   **`fs`:** Asynchronous file operations (e.g., `fs.readFile`).
*   **`crypto`:** CPU-intensive cryptographic tasks (e.g., `pbkdf2`, `scrypt`, `randomBytes`).
*   **`dns.lookup`:** Translating hostnames to IPs via the OS’s blocking `getaddrinfo` system call.
*   **`zlib`:** Compression and decompression tasks.

### Handled directly by OS Kernel (No Thread Pool)
*   **Network I/O:** TCP, UDP, DNS queries (via `dns.resolve` which bypasses `getaddrinfo`), and HTTP connections. 
*   These use native OS event mechanisms (`epoll` on Linux, `kqueue` on macOS, `IOCP` on Windows) which are naturally non-blocking.

### Tuning the Thread Pool
The default size of the Libuv thread pool is **4**. Under heavy loads (e.g., concurrent password hashing or intensive disk writes), these 4 threads can easily saturate, causing incoming file I/O to queue up and stall the event loop.

You can increase the thread pool size at startup using the environment variable:
```bash
export UV_THREADPOOL_SIZE=64
# Or inside code (must run before any asynchronous/threadpool call)
process.env.UV_THREADPOOL_SIZE = 64;
```
*Note:* The maximum thread pool limit is **1024**.

---

## 🚫 Event Loop Blocking: Detection & Prevention

Since JavaScript runs on a single main thread, any CPU-intensive operation or synchronous operation blocks the main thread, freezing the event loop. While blocked, the application cannot respond to incoming HTTP requests, databases, or timers.

### Common Blockers:
*   Synchronous APIs: `fs.readFileSync()`, `crypto.pbkdf2Sync()`, `JSON.parse()` on huge (100MB+) strings.
*   Heavy calculations: Sorting arrays with $O(N^2)$ algorithms, prime number computations, infinite loops.

### How to Detect:
*   **Command Line Flags:** Use `--blocked-loop-threshold=100` (prints stack traces to stderr if the event loop is blocked for more than 100ms).
*   **APIs:** `perf_hooks` Monitor Event Loop Delay.

### How to Solve:
1.  **Partitioning Computation:** Break heavy work into smaller chunks using `setImmediate()` to yield control back to the event loop.
2.  **Offloading:** Delegate CPU-bound tasks to child processes (`child_process.fork()`) or worker threads (`worker_threads`).
