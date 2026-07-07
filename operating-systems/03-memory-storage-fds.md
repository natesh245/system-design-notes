# Chapter 3: Memory, Storage & File Descriptors

To design data-intensive backend systems, configure databases, or debug performance scaling limits, you must understand virtual memory mechanics, storage buffering, and file descriptor resource tracking.

---

## 🧠 Virtual Memory, Pages & Page Faults

Applications do not interact with physical RAM addresses directly. Instead, they operate in a **Virtual Memory Space** created and managed by the operating system kernel and CPU hardware.

```text
+-----------------------+                    +-----------------------+
|  VIRTUAL ADDRESSES    |                    |   PHYSICAL RAM        |
|  (Process Memory)     |                    |   (Page Frames)       |
|                       |    [ MMU / Page ]  |                       |
|  - Page 0 (4KB) ──────┼───►[  Table Translation ]───► Page Frame 1 |
|  - Page 1 (4KB) ──────┼───►[            ]  |  - Page Frame 2       |
|  - Page 2 (4KB) [Unmapped]                 |  - Page Frame 3       |
+-----------------------+                    +-----------------------+
            │                                            ▲
            └──────────[ MAJOR PAGE FAULT ]──────────────┘
                    (Read from Swap/Disk into RAM)
```

### 1. The Paged Memory Model
* **Virtual Pages:** The OS divides virtual memory into fixed-size blocks called **Pages** (typically **4KB** on modern architectures).
* **Physical Page Frames:** Physical RAM is similarly divided into blocks of the same size.
* **Page Tables:** The kernel maintains a lookup table for each process that maps its virtual pages to physical page frames in RAM.
* **Memory Management Unit (MMU):** A hardware component in the CPU that uses the page tables to instantly translate virtual addresses used by code into physical RAM addresses.

### 2. Page Faults
A **page fault** occurs when a thread tries to access a virtual page that is not currently mapped to a physical page frame in physical RAM.

* **Minor Page Fault:** 
  * The data is already loaded in physical memory (e.g., it is in the OS Page Cache or shared by another process), but the process's page table has not been updated with the mapping yet.
  * **Cost:** Extremely fast. The CPU updates the process page table and resumes execution.
* **Major Page Fault:**
  * The requested page is not in physical RAM at all. It must be fetched from storage (either a file on disk or swapped out memory).
  * **Cost:** Extremely slow (milliseconds vs. nanoseconds). The kernel suspends the thread, initiates disk I/O to read the page into RAM, updates the page table, and wakes the thread up. This blocks execution.

### 3. Memory Thrashing
If a system runs out of physical RAM, the kernel starts writing inactive page frames to disk (a process called **Swapping** or Paging) to free up RAM. 
* If active programs require more memory than physical RAM available, the OS spends all its time reading pages from disk and writing other pages back to disk.
* The CPU utilization drops because all threads are blocked on disk I/O, yet the machine feels completely locked up. This state is called **Thrashing**.

---

## 💾 The OS Page Cache & Storage Buffering

Reading and writing directly to physical disks (HDDs or SSDs) is hundreds of times slower than accessing RAM. To hide this latency, the OS kernel implements the **Page Cache** (also known as the Buffer Cache).

### 1. Read Operations & Caching
When an application calls `read(fd, buffer)`:
1. The kernel checks if the requested file block is in the **Page Cache** (RAM).
2. **Cache Hit:** If present, the kernel copies the data directly from kernel space (Page Cache) to user space (application buffer). **No disk access occurs.**
3. **Cache Miss:** If absent, the kernel blocks the thread, reads the file block from disk into the Page Cache, and then copies it to user space.

### 2. Write Operations & Dirty Pages
When an application calls `write(fd, buffer)`:
1. The kernel copies the data from the application buffer into the Page Cache.
2. The page containing the written data is marked as **"Dirty"** (modified but not yet written to disk).
3. The `write()` system call returns **immediately**, allowing the application to continue.
4. **Flusher Threads:** Background kernel threads periodically flush dirty pages to physical disk.
5. **Durability Challenge:** If the server loses power before the dirty pages are flushed, **the data is lost**.
6. **`fsync()`:** To guarantee durability (e.g., in database transaction commits), applications run the `fsync()` syscall, which forces the kernel to write all dirty pages for a file to disk and blocks until the write completes.

---

## ⚡ Memory-Mapped Files (`mmap`)

`mmap` is a powerful system call that maps the contents of a file directly into a process's virtual memory address space.

```text
Standard Read/Write:
[ Disk ] ──► [ Page Cache (Kernel Space) ] ──(Copy Buffer)──► [ User Space Buffer ]

mmap (Memory Mapped):
[ Disk ] ──► [ Page Cache ] ◄──[ Memory Map Translation ]─── [ User Space Code ]
                                (Direct Pointer Access)
```

### How it works:
* Instead of using `read()` or `write()` to copy file chunks back and forth, the program accesses the file via memory pointers (arrays/structs) in virtual memory.
* If the accessed region of the file is not yet in RAM, a **Major Page Fault** occurs, and the kernel transparently loads the page from disk into the Page Cache.

### Key Advantages:
1. **Zero-Copy I/O:** Avoids copying data between kernel space (Page Cache) and user space buffers. The application reads and writes directly to the Page Cache pages.
2. **Shared Memory:** Sibling processes mapping the same file share the same page frames, saving massive memory.
3. **Use in Databases:** High-performance database storage engines (like RocksDB, LMDB, MongoDB WiredTiger, and Elasticsearch) map indexes or data files using `mmap` to let the OS handle caching and disk fetching automatically.

---

## 📂 File Descriptors & Limits

A **File Descriptor (FD)** is a non-negative integer returned by the kernel when a process opens a file, network socket, pipe, or character device.

### 1. The File Descriptor Table
* Every process has its own isolated **File Descriptor Table** managed by the kernel.
* The integer (e.g., `0`, `1`, `2` for standard input, output, and error; `3` or higher for custom files/sockets) is a pointer to the kernel's global open file table.

### 2. Limits and Production Crashes (The `EMFILE` Error)
Operating systems impose strict limits on the number of open file descriptors a single process can have (often a default of **1024** or **256** on macOS/Linux).

In high-concurrency Node.js servers, every:
* Incoming HTTP client connection (TCP socket)
* Outgoing database connection (TCP socket)
* Read/write stream to a file
...uses up **one File Descriptor**.

If your Node.js application attempts to accept a 1025th TCP connection when the limit is 1024, the kernel rejects the connection, and Node.js throws:
```text
Error: EMFILE: too many open files
```

### 3. Tuning FD Limits
To prevent production crashes under heavy traffic, you must increase these limits:

* **View limits:** `ulimit -n`
* **Temporary increase (current shell):** `ulimit -n 65535`
* **Permanent configuration (Linux):**
  Edit `/etc/security/limits.conf`:
  ```text
  * soft nofile 65535
  * hard nofile 65535
  ```
