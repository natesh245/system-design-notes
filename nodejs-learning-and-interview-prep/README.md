# Node.js Learning & Interview Preparation Guide

Welcome to the Node.js Backend Engineering & Interview Preparation roadmap. This guide is designed to take you from a basic understanding of JavaScript/Node.js to a deep, production-level engineering mastery, covering the core systems, architecture, internals, and performance tuning strategies expected in senior engineering interviews.

---

## 🗺️ Curriculum Overview

This module is split into 6 key chapters, each focusing on a fundamental pillar of Node.js systems engineering:

| Chapter | Topic | Key Focus Areas |
| :--- | :--- | :--- |
| **01** | [Event Loop & Architecture](./01-event-loop-architecture.md) | V8 vs. Libuv, Event Loop Phases, Microtask queues (`nextTick`, Promises), Thread Pool tuning. |
| **02** | [Asynchronous Control & Streams](./02-asynchronous-patterns-streams.md) | Promises, Event Emitters, Buffers, Streams (Readable/Writable/Transform), Backpressure handling. |
| **03** | [Concurrency & Multiprocessing](./03-concurrency-multiprocessing.md) | Single-thread limits, Child Processes (`spawn`/`fork`), Clusters (Round-Robin sharing), Worker Threads. |
| **04** | [Performance, Memory & GC](./04-performance-memory-gc.md) | V8 Heap spaces, Garbage Collection algorithms, Heap Limits, Memory Leaks, CPU flame graphs, Profiling. |
| **05** | [Networking & Security](./05-networking-frameworks-security.md) | Express vs. Koa design patterns, Prototype Pollution, ReDoS, CORS, Rate Limiting, Helmet, HTTPS. |
| **06** | [Interview & Coding Practice](./06-interview-questions-coding-challenges.md) | Core senior Q&As, custom Promise implementation, custom EventEmitter, rate limiters, task queues. |

---

## ⚡ The Node.js Core Philosophy (For Interviews)

When interviewing for Node.js roles, keep these three structural principles at the front of your mind:

1.  **Non-Blocking I/O:** Node.js delegates I/O operations (network, disk, database) to the operating system kernel or Libuv's thread pool, freeing the single main thread to continue executing application JavaScript.
2.  **Single-Threaded Event Loop:** JavaScript executes in a single main thread. However, the *runtime* (V8, Libuv, C++ APIs) is highly multi-threaded. Your code must never perform heavy CPU-bound computation on this main thread, or the entire application will stall.
3.  **Event-Driven Architecture:** System events (incoming connections, finished file reads, socket closure) trigger callbacks registered in the event loop, acting as the nervous system of the application.

---

## 📚 General Interview Tips for Node.js Candidates

*   **Avoid "Magic" Explanations:** Don't just say `async/await` "makes code asynchronous". Explain that it is syntactic sugar over Promises, which utilize V8's microtask queue to yield control back to the call stack once resolved.
*   **Understand Under the Hood:** Be prepared to explain exactly *where* a socket read occurs (OS kernel via epoll/kqueue) vs. where a cryptographic hash is calculated (Libuv thread pool).
*   **Know Your Tooling:** Interviews often involve troubleshooting. Know how to capture a heap snapshot using `--inspect` and compare them in Chrome DevTools to trace a memory leak, or explain how to generate a CPU profile to debug 100% CPU usage.

---

## 📈 Study Log & Progress

### 📅 July 6, 2026
* **Completed:** Deep-dive study and Q&A on **Chapter 1: Node.js Core Architecture & Event Loop**.
* **Key Topics Covered:**
  * Single-threaded JS execution (one Call Stack per thread) vs. multi-threaded Node.js runtime internals (V8 threads, Libuv thread pool).
  * V8 JIT Compilation Pipeline (Parsing ➔ AST ➔ Ignition Interpreter Bytecode ➔ Turbofan Compiler Native Machine Code ➔ Deoptimization loop).
  * RAM Memory Spaces: Bytecode stored as managed objects in the **V8 Heap**, while native machine code resides in the executable **Code Space**.
  * Hardware CPU execution of bytecode (running interpreter's machine code instructions as a translation middleman) vs. direct native machine code execution.
  * Structure of a **Stack Frame** (parameters, local variables, return address) and how it keeps execution context on the Call Stack.
* **Documentation Updated:** Expanded [01-event-loop-architecture.md](file:///Users/natesh/projects/system-design/nodejs-learning-and-interview-prep/01-event-loop-architecture.md) to fully capture these low-level compilation and execution mechanics.
### 📅 July 7, 2026
* **Completed:** Remainder of **Chapter 1: Node.js Core Architecture & Event Loop**.
* **Key Topics Covered:**
  * Detailed Event Loop phases (Timers, Pending, Idle/Prepare, Poll, Check, Close Callbacks) and the blocking behavior of the Poll phase.
  * Non-deterministic order of top-level `setTimeout` vs. `setImmediate` vs. guaranteed execution inside I/O callbacks.
  * Microtask execution priority (`process.nextTick` vs. Promise queues) and the draining mechanics.
  * Libuv Thread Pool offloading vs. OS Kernel native asynchronous mechanisms (`epoll`/`kqueue`/`IOCP`).
  * Event loop blocking detection (e.g., `--blocked-loop-threshold`) and solutions (partitioning, payload limiting, worker threads).
* **Next Steps (Context for Tomorrow):**
  * **Start with a revision quiz:** Ask diagnostic questions covering:
    1. Event Loop phases and microtask queue priority rules.
    2. Libuv Thread Pool vs. OS Kernel offloading rules.
    3. The V8 Execution & Hardware Boundary Q&A from [01-event-loop-architecture.md](./01-event-loop-architecture.md#L214-L235).
  * Move to **Chapter 2: Asynchronous Control & Streams** ([02-asynchronous-patterns-streams.md](./02-asynchronous-patterns-streams.md)) to cover Promises, Event Emitters, Buffers, Streams, and backpressure handling.




