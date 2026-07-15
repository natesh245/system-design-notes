# Node.js Learning & Interview Preparation Guide

Welcome to the Node.js Backend Engineering & Interview Preparation roadmap. This guide is designed to take you from a basic understanding of JavaScript/Node.js to a deep, production-level engineering mastery, covering the core systems, architecture, internals, and performance tuning strategies expected in senior engineering interviews.

---

## 🗺️ Curriculum Overview

This module is split into 7 key chapters, each focusing on a fundamental pillar of Node.js systems engineering:

| Chapter | Topic | Key Focus Areas |
| :--- | :--- | :--- |
| **01** | [Event Loop & Architecture](./01-event-loop-architecture.md) | V8 vs. Libuv, Event Loop Phases, Microtask queues (`nextTick`, Promises), Thread Pool tuning. |
| **02** | [Asynchronous Control & Streams](./02-asynchronous-patterns-streams.md) | Promises, Event Emitters, Buffers, Streams (Readable/Writable/Transform), Backpressure handling. |
| **03** | [Concurrency & Multiprocessing](./03-concurrency-multiprocessing.md) | Single-thread limits, Child Processes (`spawn`/`fork`), Clusters (Round-Robin sharing), Worker Threads. |
| **04** | [Performance, Memory & GC](./04-performance-memory-gc.md) | V8 Heap spaces, Garbage Collection algorithms, Heap Limits, Memory Leaks, CPU flame graphs, Profiling. |
| **05** | [Networking & Security](./05-networking-frameworks-security.md) | Express vs. Koa design patterns, Prototype Pollution, ReDoS, CORS, Rate Limiting, Helmet, HTTPS. |
| **06** | [Interview & Coding Practice](./06-interview-questions-coding-challenges.md) | Core senior Q&As, custom Promise implementation, custom EventEmitter, rate limiters, task queues. |
| **07** | [NestJS Architecture & DI](./07-nestjs-architecture-di.md) | Controllers, Providers, Modules, Inversion of Control (IoC), Dependency Injection lifecycle, Request Lifecycle. |

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
### 📅 July 9, 2026
* **Completed:** Chapter 2 in its entirety, including all revision quizzes (Promises, error handling, EventEmitters, off-heap Buffers, Streams, backpressure, and pipeline).
* **Key Topics Covered:**
  * Microtask Queue priority (V8 Promise queue vs. process.nextTick vs. Libuv I/O macrotasks) and immediate draining lifecycle (after each macrotask completes).
  * Express v4 async error-handling limitation (lack of automatic promise rejection catching, leading to hanging client connections).
  * EventEmitter reference chain cleanup: manual `.off()` vs. wrapper-based `.once()` execution mechanics.
  * V8 Mark-and-Sweep Garbage Collection vs. Reference Counting (tracing from roots, handling circular references).
  * Off-heap Buffer allocation (raw C++ memory outside the V8 heap, zero-copy, GC pressure bypass, V8 memory boundary bypass).
  * Stream backpressure handling: how `writable.write()` returns `false` when hitting the `highWaterMark`, and the `'drain'` event to resume reading.
  * Flaws of `.pipe()` (leaks resource handles on error) vs. safety of `stream.pipeline()` (auto-destroying all streams upon failure).
### 📅 July 10, 2026
* **Completed:** Chapter 2 final review quiz and **Chapter 3: Concurrency & Multiprocessing** in its entirety (including revision quiz).
* **Key Topics Covered:**
  * **Chapter 2 Revision:**
    * V8 heap allocation limits vs. off-heap C++ allocations for Buffers.
    * Memory overflow and process crash mechanics of synchronous/fully-buffered reads (`fs.readFile`) vs. chunk-based streams.
    * Default `highWaterMark` sizes (64KB for Readable vs 16KB for Writable) and their role in initiating stream backpressure.
  * **Chapter 3 (Concurrency & Multiprocessing):**
    * Multi-process boundaries: process memory isolation and separate V8 instances under `child_process` / `cluster` vs. multi-threading under `worker_threads`.
    * Child process creation: streaming performance of `spawn()` vs. buffered limits (200KB maxBuffer crash) of `exec()`, direct non-shell binaries in `execFile()`, and Node.js process-spawning in `fork()`.
    * Port Sharing & Load Balancing: how the primary process binds to the server port and hands off raw OS file descriptors (socket handles) to workers over IPC to prevent `EADDRINUSE` errors and load balance via Round-Robin.
    * V8 Isolates: thread-isolated stack, heap, and event loops in `worker_threads`.
    * Memory sharing: copying variables using the Structured Clone Algorithm vs. sharing raw memory slots using `SharedArrayBuffer` (and protecting against data race conditions using `Atomics`).
### 📅 July 11, 2026
* **Completed:** Comprehensive review and quiz session covering Chapters 1, 2, and 3.
* **Key Topics Covered:**
  * JIT execution pipelines (AST ➔ bytecode in heap ➔ optimized native machine code in Code Space) and type-feedback deoptimization.
  * Microtask queue priorities (`process.nextTick` vs Promise queues) and Event Loop starvation mechanics.
  * Express v4 async error-handling limitations (hanging sockets on unhandled rejections).
  * EventEmitter memory leak analysis (closures retaining scopes) and `.once()` wrapper unsubscription mechanics.
  * Off-heap Buffer memory limits (`alloc` vs `allocUnsafe` zero-filling and data leakage risks).
  * System-level socket handle (File Descriptor) passing over IPC in clustered Node.js processes.
  * Process vs. Thread concurrency boundaries and lightweight background execution trade-offs in `worker_threads` vs. `cluster`.
### 📅 July 14, 2026
* **Completed:** Comprehensive revision quiz on Chapters 1–3 and first half of **Chapter 4: V8 Memory Management, GC & Profiling** (up to memory leaks).
* **Key Topics Covered:**
  * V8 vs. Node.js runtime responsibility for microtask queues (Node's `process.nextTick` queue vs V8's Promise microtask queue).
  * Express v4 async route handler unhandled rejection hanging requests and the custom `asyncHandler` error-propagation wrapper.
  * Unix File Descriptors (FDs) and `cluster` port sharing via FD-delegation (client socket passing vs. listening socket passing over IPC).
  * V8 Scavenger GC (From/To semi-space copying mechanics) and promotion age threshold conditions.
  * Heap allocation of V8 Context objects for closures and JIT scope analysis optimization (excluding unused variables unless sibling closures share the Context—the Meteor leak pattern).
### 📅 July 15, 2026
* **Completed:** Remainder of **Chapter 4: V8 Memory Management, GC & Profiling** and revision quiz.
* **Key Topics Covered:**
  * Programmatic heap snapshots and Chrome DevTools Comparison View (using # Delta and Size Delta to identify leaks).
  * Tracing references back to GC roots using the Retainers pane to pinpoint closures/constructors.
  * Analysis of common leak patterns, such as the EventEmitter closure leak, and unsubscription remediation patterns.
  * CPU performance diagnostic profiling using Node.js native profiler and the Clinic.js suite (`doctor`, `flame` graphs, `bubbleprof`).

---

## 🧠 Focus Areas & Weakness Analysis

To achieve senior-level systems engineering mastery, focus on strengthening your understanding of these specific low-level boundary points:

### 1. V8 Shared Context Object Lifecycle
* **The Gap:** Understanding when variables inside a closure are garbage collected vs when they leak.
* **Key Concept:** V8 creates a single shared Context object for all closures declared within the same parent scope. If one closure references a large variable, that variable is kept in the shared Context, causing it to leak even if other active closures do not reference it.

---

* **Next Steps (Context for Tomorrow):**
  * **Start from Chapter 1: Node.js Core Architecture & Event Loop ([01-event-loop-architecture.md](./01-event-loop-architecture.md)) with a comprehensive revision quiz.**
  * Probe deeply with event loop phases, microtask queue execution order, thread pool offloading vs. kernel asynchronous mechanisms.
