# Chapter 3: Concurrency & Multiprocessing

Since Node.js executes JavaScript on a single thread, performing CPU-intensive tasks (such as image resizing, PDF generation, or cryptographic operations) will freeze the event loop. To build scalable systems, you must know how and when to offload work using multi-process or multi-thread models.

---

## 🎛️ Concurrency Models in Node.js

Node.js offers three primary strategies for handling concurrent execution outside the main event loop thread:

| Mechanism | Process Model | Memory Sharing | Communication | Best Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **Child Process** | Separate OS process. Runs any shell command or code. | Completely isolated. | Inter-Process Communication (IPC) pipes. | Executing system commands or external scripts (Python, Bash, etc.). |
| **Cluster Module** | Separate Node.js processes running the same script. | Isolated. | IPC pipes (automatic load balancing). | Scaling network web servers (HTTP APIs) across multiple CPU cores. |
| **Worker Threads** | Single process. Runs multiple V8 isolated threads. | Can share memory (`SharedArrayBuffer`). | Message passing (`postMessage`) or Shared Memory. | Heavy CPU-bound computation in JavaScript (math, machine learning, crypto). |

---

## 👶 1. Child Processes (`child_process`)

The `child_process` module allows you to spawn external OS commands and executable binaries.

### Four Methods to Spawn a Child Process:

#### A. `spawn()`
Spawns a process asynchronously. It returns a stream, meaning output data is piped directly in chunks.
*   **Pros:** Highly memory efficient; does not buffer output. Suitable for long-running processes or massive output data (e.g., video transcoding).
*   **Code Example:**
    ```javascript
    const { spawn } = require('child_process');
    const child = spawn('ls', ['-lh', '/usr']);

    child.stdout.on('data', (data) => console.log(`stdout: ${data}`));
    child.stderr.on('data', (data) => console.error(`stderr: ${data}`));
    ```

#### B. `exec()`
Spawns a shell and runs a command, buffering the entire output in memory before calling a callback.
*   **Cons:** Not suitable for large output. The default buffer limit is **200KB**; if the child process outputs more, the program crashes with `maxBuffer exceeded`.
*   **Code Example:**
    ```javascript
    const { exec } = require('child_process');
    exec('ls -lh /usr', (err, stdout, stderr) => {
        if (err) return console.error(err);
        console.log(stdout);
    });
    ```

#### C. `execFile()`
Similar to `exec()`, but runs the executable binary directly **without spawning a shell**.
*   **Pros:** Faster performance, more secure (invulnerable to shell injection attacks).
*   **Code Example:**
    ```javascript
    const { execFile } = require('child_process');
    execFile('/usr/bin/node', ['--version'], (err, stdout, stderr) => {
        console.log(stdout); // Prints node version
    });
    ```

#### D. `fork()`
A special variation of `spawn()` designed specifically to spawn new **Node.js processes**.
*   **Key Feature:** Sets up an IPC (Inter-Process Communication) channel between the parent and child, allowing JSON messages to be passed back and forth.
*   **Parent Code:**
    ```javascript
    const { fork } = require('child_process');
    const child = fork('child_task.js');

    child.send({ task: 'start', data: 42 });
    child.on('message', (result) => console.log('Result from child:', result));
    ```
*   **Child Code (`child_task.js`):**
    ```javascript
    process.on('message', (msg) => {
        console.log('Message from parent:', msg);
        // Process heavy logic
        process.send({ status: 'done', result: msg.data * 2 });
    });
    ```

---

## 🕸️ 2. The Cluster Module

The `cluster` module allows you to scale a single HTTP/TCP server across all available CPU cores by spawning helper worker processes that share the same server port.

```text
                  +--------------------------------+
                  |    PRIMARY PROCESS (Port 80)   |
                  +---------------+----------------+
                                  |
            Distributes requests via Round-Robin IPC
                                  |
         +------------------------+------------------------+
         |                        |                        |
+--------v-------+       +--------v-------+       +--------v-------+
|  Worker 1 (JS) |       |  Worker 2 (JS) |       |  Worker 3 (JS) |
| (Event Loop 1) |       | (Event Loop 2) |       | (Event Loop 3) |
+----------------+       +----------------+       +----------------+
```

### Key Architectural Concepts:
1.  **Port Sharing:** Under the hood, the Primary process binds to the port (e.g., 80) and accepts connections. It then forwards the client file descriptors to workers via internal IPC channels.
2.  **Load Balancing:** By default, the Primary process uses a **Round-Robin** algorithm (on Linux/macOS) to distribute incoming HTTP requests evenly among idle workers.
3.  **High Availability:** If a worker process crashes due to an uncaught exception, the Primary process is notified and can immediately spin up a new worker instance to maintain cluster capacity.

### Production Cluster Code Pattern:
```javascript
const cluster = require('cluster');
const http = require('http');
const numCPUs = require('os').cpus().length;

if (cluster.isPrimary) {
    console.log(`Primary ${process.pid} is running`);

    // Fork workers equal to CPU cores
    for (let i = 0; i < numCPUs; i++) {
        cluster.fork();
    }

    cluster.on('exit', (worker, code, signal) => {
        console.log(`Worker ${worker.process.pid} died. Spawning a replacement...`);
        cluster.fork(); // Resiliency
    });
} else {
    // Workers share the TCP connection port
    http.createServer((req, res) => {
        res.writeHead(200);
        res.end(`Handled by worker ${process.pid}`);
    }).listen(8000);

    console.log(`Worker ${process.pid} started`);
}
```

---

## 🧵 3. Worker Threads (`worker_threads`)

Unlike clusters (which run separate OS processes), the `worker_threads` module allows you to run **multiple JavaScript threads within the same OS process**.

### V8 Isolates:
*   Each Worker thread runs its own **V8 Isolate** (independent V8 instance with its own call stack and heap).
*   However, because they live in the same process, they can share raw memory buffers, bypassing IPC overhead.

```javascript
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');

if (isMainThread) {
    // Parent Thread: Spin up worker thread, pass data
    const worker = new Worker(__filename, {
        workerData: { num: 10 }
    });

    worker.on('message', (result) => {
        console.log(`Result from worker thread: ${result}`);
    });

    worker.on('error', (err) => console.error(err));
    worker.on('exit', (code) => console.log(`Worker stopped with exit code ${code}`));
} else {
    // Worker Thread: Execute CPU-bound computation
    const input = workerData.num;
    const output = fibonacci(input);
    
    // Send result back to main thread
    parentPort.postMessage(output);
}

function fibonacci(n) {
    if (n < 2) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```

### Sharing Memory: `SharedArrayBuffer`
To avoid serialization/copying overhead when passing data to workers, you can pass a `SharedArrayBuffer` which allows both threads to read/write the same region of RAM directly:
```javascript
const sharedBuffer = new SharedArrayBuffer(1024); // 1KB of shared memory
const uint8Array = new Uint8Array(sharedBuffer);

// Pass sharedBuffer to the worker
const worker = new Worker('./worker.js', { workerData: { sharedBuffer } });
```
> [!CAUTION]
> Direct memory sharing introduces **Race Conditions**. To prevent threads from writing to the same memory slot simultaneously, use the **`Atomics`** API to coordinate operations (e.g., `Atomics.store()`, `Atomics.load()`, `Atomics.wait()`).
