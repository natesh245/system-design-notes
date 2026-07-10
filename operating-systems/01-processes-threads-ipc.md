# Chapter 1: Processes, Threads & IPC

To architect high-performance backend systems and debug production bottlenecks, you must understand how the operating system schedules work, separates memory, and facilitates communication between isolated execution units.

---

## 🧵 Process vs. Thread

Operating systems manage execution using two core abstractions: **Processes** and **Threads**.

```text
+-----------------------------------------------------------+
|                      OS PROCESS                           |
|  [Memory Space: Code, Data, Heap]                         |
|  [System Resources: File Descriptors, Network Sockets]    |
|                                                           |
|  +------------------------+    +-----------------------+  |
|  |     OS THREAD A        |    |      OS THREAD B      |  |
|  |  - Registers / PC      |    |  - Registers / PC     |  |
|  |  - Private Stack       |    |  - Private Stack      |  |
|  +------------------------+    +-----------------------+  |
+-----------------------------------------------------------+
```

### 1. The Process (The Container)
A **process** is an active, running instance of a program. It is the primary unit of resource allocation in an operating system.
* **Isolation:** Every process has its own isolated, virtual address space. Process A cannot read or write to the memory of Process B. If Process A crashes, Process B remains unaffected.
* **Allocated Resources:** The kernel allocates specific resources to a process, including:
  * A unique Process ID (PID).
  * A dedicated **Virtual Memory Address Space** (containing the program's code, static variables, and Heap).
  * A **File Descriptor Table** (tracking open files, network sockets, database connections, etc.).
  * User credentials and security permissions.

### 2. The Thread (The Execution Unit)
A **thread** is the smallest unit of execution that the OS kernel can schedule on a CPU core. Every process has at least one thread (the main thread).
* **Shared Memory:** All threads belonging to the same process share that process’s virtual memory space (including the Heap and global variables) and system resources (like the File Descriptor Table).
* **Private Resources:** Each thread retains its own:
  * **Program Counter (PC):** Points to the address of the current instruction being executed on the CPU core.
  * **Registers:** Dedicated CPU register storage for immediate values.
  * **Stack Space:** Private, local LIFO (Last In, First Out) memory storage for function calls, arguments, local variables, and return addresses.
* **Risk:** If a thread performs an invalid memory operation (e.g., segment fault) or encounters an unhandled exception, it will crash the **entire process** and terminate all sibling threads.

#### 🗂️ The Anatomy of a Stack Frame (Hardware-Level Function Calls)
When a thread calls a function, a block of memory called a **Stack Frame** is pushed onto the thread's private stack. It does *not* store the compiled function code itself, but rather the execution state for that specific call:
* **Function Arguments/Parameters:** Inputs passed to the function.
* **Local Variables:** Variables declared inside the function's scope.
* **Return Address:** A pointer indicating the exact memory address in the *caller* function where the CPU should jump back to and resume execution once this function returns.

At the assembly level, invoking a function is done using a jump/branch instruction (like `CALL` in x86 or `BL` in ARM) which pushes the next instruction address onto the stack. Exiting the function is done using `RET` (Return), which pops the address off the stack and loads it back into the Program Counter (PC).

#### ⚙️ How the CPU Executes Code: Machine Code vs. Bytecode
The CPU's physical Program Counter (PC) only points to native, executable machine code instructions. It cannot read high-level code or bytecode directly:
* **Optimized Machine Code Execution:** The PC points directly to the JIT-compiled binary machine code (e.g., in the Code Space in RAM). The CPU reads these bytes directly as native **instructions** (executable commands) and runs them at hardware speed.
* **Bytecode / Interpreted Execution:** The PC points to the pre-compiled machine code of the **Interpreter program** (e.g., V8 Ignition). The CPU executes the interpreter's code. The interpreter then fetches the virtual bytecode from the Heap as **data** (reading it into registers to parse and decode) and executes its own pre-compiled machine code handlers corresponding to each bytecode instruction.

---

## 🧠 Memory Organization: Stack vs. Heap

| Feature | Stack Memory | Heap Memory |
| :--- | :--- | :--- |
| **Scope** | **Thread-private**. Accessible only to the owning thread. | **Process-shared**. Accessible to all threads in the process. |
| **Allocation** | Managed automatically by the CPU using push/pop operations. | Allocated and deallocated dynamically (manually or by GC). |
| **Access Speed** | **Extremely fast** (highly localized in L1/L2 CPU caches). | **Slower** (requires pointer lookup and dereferencing). |
| **Structure** | LIFO (Last In, First Out) stack structure. | Large, unstructured pool of memory. |
| **Errors** | Stack Overflow (nested/recursive calls exceed stack size). | Out of Memory (OOM) or fragmentation errors. |

---

## 🔄 Context Switching Overhead

A **context switch** is the process of storing the state (context) of a running thread or process so that it can be paused, and restoring the state of another thread or process to resume its execution. This is how the OS schedules concurrency on a limited number of CPU cores.

Context switching is a **highly expensive** hardware/kernel operation.

### Process Context Switch vs. Thread Context Switch

#### Process Context Switch (Extremely Expensive)
When the OS switches execution from Process A to Process B:
1. **Save CPU State:** Saves CPU registers, stack pointers, and the Program Counter of Process A's current thread.
2. **Switch Page Tables:** The OS changes the MMU (Memory Management Unit) pointer to use Process B’s page tables (restructuring virtual-to-physical memory maps).
3. **TLB Invalidation (The biggest cost):** The Translation Lookaside Buffer (TLB)—a hardware cache storing virtual-to-physical memory mappings—is completely invalidated. As Process B begins executing, it suffers massive **TLB misses** and memory access latency.
4. **Cache Thrashing:** The physical CPU caches (L1, L2, L3) are filled with Process A's data. As Process B runs, CPU cache misses spike as the cache is overwritten with Process B's data.

#### Thread Context Switch (Relatively Lightweight)
When the OS switches from Thread A to Thread B *within the same process*:
1. **Save/Restore CPU Registers:** The OS saves registers and the Program Counter for Thread A, and loads them for Thread B.
2. **No Memory Space Change:** Since both threads share the same process memory space, **the page tables do not change, and the TLB cache remains intact**. This results in significantly lower cache and memory access overhead.

---

## 🔀 Inter-Process Communication (IPC)

Because processes have completely isolated memory spaces, they cannot communicate by reading/writing to shared variables. Instead, they must use OS-provided **Inter-Process Communication (IPC)** mechanisms:

### 1. Pipes (Unnamed & Named)
* **Unnamed Pipes:** A unidirectional data channel created in RAM. Used for communication between a parent process and its child (e.g., standard shell piping `ls | grep "node"`).
* **Named Pipes (FIFOs):** Represented as a special file in the file system. Allows unrelated processes to communicate by writing to/reading from the pipe file.

### 2. Unix Domain Sockets (UDS)
* **How it works:** A bidirectional data communication channel represented as a socket file in the file system.
* **Why it's fast:** Unlike network sockets (which route data through the TCP/IP network loopback stack), Unix Domain Sockets route data entirely in kernel memory. This bypasses IP headers, checksums, TCP handshakes, and routing tables.
* **Best Use:** Local IPC (e.g., Nginx communicating with a Node.js process running on the same server).

### 3. Shared Memory
* **How it works:** Multiple processes map the same physical block of RAM into their virtual memory address spaces.
* **Why it's fast:** It is the **fastest IPC mechanism** because data is written directly to memory without routing through the OS kernel or copying buffers.
* **Synchronization Requirement:** Since multiple processes write to the same memory, they must use synchronization structures like **Mutexes** or **Semaphores** to prevent race conditions and memory corruption.

### 4. Message Queues
* **How it works:** A system-wide message queue managed by the OS kernel. Processes can write structured messages to the queue and read them in a FIFO (First-In, First-Out) or priority order.
* **Benefits:** Asynchronous, decoupled communication. The receiving process does not need to be active when the message is sent.

---

## 🟢 Relevance to Node.js & Backend Architecture

Node.js is designed around a single-threaded JS execution model, but it relies heavily on OS process and thread abstractions to handle scale.

### 1. Child Processes (`child_process` module)
Used to offload CPU-heavy operations or run external shell commands.
* **`spawn`:** Launches a new process. Streams data (`stdout`/`stderr`) back to Node.js. Best for processing large datasets or long-running shell scripts without loading all data into memory at once.
* **`exec` / `execFile`:** Runs a process and buffers the entire output in memory before passing it to a callback. Best for fast command-line utilities returning small payloads.
* **`fork`:** A specialized version of `spawn` that creates a new Node.js process. It automatically opens an **IPC channel** between the parent and child process, allowing you to pass messages (`process.send()`) and even transfer socket handles.

### 2. Worker Threads (`worker_threads` module)
Introduced to allow CPU-bound JavaScript execution within the same Node.js process without blocking the main event loop.
* **Lightweight Concurrency:** Instead of spawning a new process (which requires separate memory space and high context-switching overhead), you spawn a thread inside the same Node.js process.
* **Shared Memory:** Sibling threads can share binary memory arrays using `SharedArrayBuffer`, bypassing the serialization/deserialization overhead of process IPC messages.

### 3. The Cluster Module
Node.js applications running on a single core cannot fully utilize multi-core processors. The `cluster` module allows you to spin up multiple worker processes.
* **Process Model:** The master process spawns worker processes (usually one per CPU core) using `child_process.fork()`.
* **Port Sharing:** The master process binds to the HTTP port (e.g., port 3000) and routes incoming TCP connections to worker processes using a **Round-Robin** scheduling algorithm (on Linux/macOS) or delegates connection handling to the workers (on Windows).
* **Fault Tolerance:** If a worker process encounters an unhandled exception and crashes, the master process can catch the `exit` event and instantly spin up a new worker, maintaining zero downtime.
