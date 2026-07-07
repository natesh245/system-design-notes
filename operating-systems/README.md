# Operating Systems for Systems & Backend Engineers

This module covers the core operating systems principles necessary for designing high-performance backend applications, understanding Node.js execution internals, and passing system design/architecture interviews. 

As a backend engineer, you don't need to write a kernel, but you must know how your code interacts with the kernel, CPU, memory, storage, and network interface.

---

## 🗺️ Module Curriculum

This module is structured into three primary deep-dives:

| Chapter | Topic | Key Focus Areas |
| :--- | :--- | :--- |
| **01** | [Processes, Threads & IPC](./01-processes-threads-ipc.md) | Virtual Memory separation, context switching costs, Thread synchronization, Sockets, Pipes, and Shared Memory. |
| **02** | [I/O Multiplexing & System Calls](./02-io-multiplexing-syscalls.md) | User/Kernel space boundary, System Calls, Blocking vs. Non-blocking I/O, `epoll`, `kqueue`, and `IOCP` multiplexing. |
| **03** | [Memory, Storage & File Descriptors](./03-memory-storage-fds.md) | Virtual Memory, Page Cache mechanics, File Descriptors, `ulimit` tuning, and memory-mapped files (`mmap`). |

---

## 💡 Why OS Matters in Backend & System Design

1. **High Concurrency & I/O:** Scalable web servers (like Nginx, Node.js, and Netty) achieve their massive throughput not by spawning a million OS threads, but by utilizing OS event demultiplexing APIs (`epoll` or `kqueue`) to handle connections asynchronously.
2. **Database Performance:** High-performance database storage engines (like RocksDB, PostgreSQL, or LMDB) are heavily optimized to work with the OS **Page Cache**, direct disk access, and memory mapping (`mmap`).
3. **Resource Saturation & Troubleshooting:** When a server experiences high CPU latency, out-of-memory (OOM) crashes, or "too many open files" errors, diagnosing the problem requires a concrete understanding of OS limits, file descriptors, and context switching.
