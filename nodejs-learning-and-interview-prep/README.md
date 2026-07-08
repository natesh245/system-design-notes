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
  * Move to **Chapter 2: Asynchronous Control & Streams** ([02-asynchronous-patterns-streams.md](./02-asynchronous-patterns-streams.md)) to cover Promises, Event Emitters, Buffers, Streams, and backpressure handling.
### 📅 July 8, 2026
* **Completed:** Chapter 1 revision quiz and first half of **Chapter 2: Asynchronous Control & Streams** (up to Event Emitters).
* **Key Topics Covered:**
  * **Chapter 1 Revision:**
    * CPU/OS-level Thread definition (execution context with registers/PC/Stack vs. static instruction sequences).
    * V8 Call Stack vs. Program Counter (instruction-level tracking via PC register vs. function-level return address tracking in stack frames).
    * Subroutine and procedure execution models at the machine code level (`CALL`/`RET` and jumps).
    * V8 Ignition Bytecode interpreter and pre-compiled machine code handlers (emulated execution).
    * RAM separation: managed V8 Heap (Read/Write, garbage-collected) vs. executable Code Space (Read/Execute, non-writable/security-hardened).
    * V8 Stack Frame structure: receivers, contexts, JSFunction closure references (heap lookup to find bytecode/machine code), and local variables.
    * Physical CPU execution rules: Optimized code is executed directly as native instructions, while Bytecode is processed as data by the interpreter program.
    * Blocking nature of synchronous JS code and the necessity of an empty call stack for the event loop to proceed.
  * **Chapter 2 (Asynchronous Control & Streams):**
    * Why Node.js is optimized for I/O-bound apps: single-threaded event loop, non-blocking delegation to OS kernel (`epoll`/`kqueue`/`IOCP`), and offloading to Libuv thread pool.
    * Asynchronous control flow evolution: Callbacks (error-first) ➔ Promises ➔ Async/Await.
    * EventEmitter memory leaks: reference chains (`Root` ➔ global emitter ➔ listener list ➔ callback ➔ closure scope ➔ short-lived requestData objects) preventing garbage collection.
    * V8 GC Mark-and-Sweep algorithm: Why local emitters do not leak (forming unreachable cycles that V8 sweeps), whereas global emitters do.
    * Unsubscribe mechanisms: breaking reference chains using `.once()` or manual `.off()`/`removeListener()` cleanups (e.g. on response `'finish'` events).
* **Next Steps (Context for Tomorrow):**
  * **Start with a revision quiz (Format Rules: Ask exactly 1 question at a time. Probe with follow-up questions based on the answers before moving to the next):**
    * **Specific User Questions to Quiz:**
      1. *"What is the difference under the hood in terms of execution queue priority between an asynchronous I/O callback (e.g., in fs.readFile) and a Promise callback (e.g., in .then() or await)?"*
      2. *"Explain the unhandledRejection event. When does V8 emit it, and why does Node.js recommend a graceful shutdown upon receiving it?"*
      3. *"Explain the reference chain that causes a memory leak when a callback enclosing local variables is registered to a long-lived EventEmitter."*
      4. *"Why does a local EventEmitter inside a route handler NOT cause a memory leak, while a global EventEmitter does? (Explain in terms of V8's Mark-and-Sweep GC tracing from the root)."*
      5. *"How do `.once()` and `.off()` prevent memory leaks in EventEmitters?"*
  * Continue **Chapter 2: Asynchronous Control & Streams** ([02-asynchronous-patterns-streams.md](./02-asynchronous-patterns-streams.md)) starting with **Buffers vs. Streams** (alloc vs. allocUnsafe) and **Backpressure**.






