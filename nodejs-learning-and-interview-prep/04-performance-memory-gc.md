# Chapter 4: V8 Memory Management, GC & Profiling

To build stable, enterprise-scale Node.js applications, you must understand how the V8 engine manages memory, how garbage collection operates, and how to identify memory leaks and CPU bottlenecks under production workloads.

---

## 💾 V8 Heap Memory Structure

The V8 memory pool is divided into two primary segments: **Resident Set (RSS)** (the total memory allocated to the Node process by the OS) and the **Heap Memory** (managed directly by V8).

```text
+-------------------------------------------------------------+
|                     Resident Set (RSS)                      |
|                                                             |
|   +-----------------------+   +--------------------------+  |
|   |    C++ Memory/APIs    |   |      V8 Heap Memory      |  |
|   |    (Buffers, Node Core|   |                          |  |
|   |     Libuv handles)    |   |  - New Space (Scavenge)  |  |
|   +-----------------------+   |  - Old Space (Mark-Sweep)|  |
|                               |  - Large Object Space    |  |
|                               |  - Code Space            |  |
|                               |  - Map Space             |  |
|                               +--------------------------+  |
+-------------------------------------------------------------+
```

### The V8 Heap Spaces:

1.  **New Space (Young Generation):**
    *   A small, highly active buffer (typically 1MB to 64MB) where all new objects are initially allocated.
    *   Managed by the fast **Scavenger** garbage collector.
2.  **Old Space (Old Generation):**
    *   Contains objects that survived multiple cycles in the New Space and were promoted.
    *   Managed by the **Mark-Sweep-Compact** collector.
    *   Divided into:
        *   *Old Pointer Space:* Contains objects that have pointers to other objects.
        *   *Old Data Space:* Contains raw data objects (strings, numbers, raw byte arrays).
3.  **Large Object Space:**
    *   Allocated for objects exceeding the size limit of the other spaces.
    *   V8 never moves these objects during garbage collection cycles (to avoid high copying overhead).
4.  **Code Space:**
    *   Where the JIT compiler stores compiled machine code blocks.
5.  **Map Space (Cell/Property Space):**
    *   Stores "Hidden Classes" (Shapes) of objects, which V8 uses for property access optimization.

---

## 🧹 V8 Garbage Collection Mechanics

V8 uses a **generational garbage collection** strategy based on the generational hypothesis: *most objects die young*.

```text
                  +--------------------------------+
                  |    Object Allocated in Heap    |
                  +---------------+----------------+
                                  |
                        [ Allocated in New Space ]
                                  |
                         (Runs Scavenger GC)
                        Is object still referenced?
                       /                          \
                     No                            Yes
                     /                              \
            [ Freed / Swept ]             [ Copied to Active Space ]
                                                    |
                                          (Runs 2nd Scavenger)
                                          Still referenced?
                                         /                \
                                       No                  Yes
                                       /                    \
                              [ Swept ]            [ Promoted to Old Space ]
                                                             |
                                                     (Old Space Full?)
                                                             |
                                                (Runs Mark-Sweep-Compact)
```

### 1. The Scavenger GC (New Space)
*   The New Space is divided into two equal-sized semi-spaces: the **From Space** (active) and the **To Space** (inactive).
*   When the From Space fills up, a Scavenge cycle begins:
    1.  V8 traverses the object graph starting from root references.
    2.  Active (referenced) objects are copied to the **To Space**. Unreferenced objects are ignored (swept).
    3.  If an object has already survived one Scavenge cycle, it is promoted directly to the **Old Space**.
    4.  V8 swaps the roles of the spaces (the **To Space** becomes the active **From Space**).
*   **Why it's fast:** The copying overhead depends only on the number of *surviving* objects, which is usually small.

### 2. Mark-Sweep-Compact GC (Old Space)
Runs when the Old Space reaches a threshold capacity. It is slower and consists of three phases:
*   **Marking:** V8 builds a tree of active objects starting from root references (stack pointers, globals). It marks all reachable objects as active.
*   **Sweeping:** V8 iterates through the unreferenced memory addresses and registers them in the "Free List", making the space available for new objects.
*   **Compacting:** Over time, memory becomes fragmented (holes of empty space). V8 shifts remaining active objects together to defragment the heap, preventing allocation errors for large variables.

---

## 🚨 Memory Leaks in Node.js

A memory leak occurs when V8 cannot reclaim memory for unused objects because they are still reachable from global roots.

### Common Memory Leak Patterns:

#### A. Accidental Global Variables
Without strict mode (`'use_strict'`), assigning values to undeclared variables attaches them to the global object (`global`), preventing garbage collection:
```javascript
function processData() {
    leakedData = new Array(1000000); // Leaks: Attached to global.leakedData
}
```

#### B. Forgotten Timers and Intervals
Active timers keep callbacks in memory. Any variables referenced inside a timer closure cannot be garbage collected while the timer runs:
```javascript
function requestHandler() {
    const hugeBuffer = Buffer.alloc(10000000); // 10MB
    setInterval(() => {
        // If this interval is never cleared via clearInterval, 
        // hugeBuffer will leak in memory forever
        console.log('Heartbeat check');
    }, 1000);
}
```

#### C. Closures Retaining Large Scope Variables
A closure retains reference to its parent scope. If a small function returned from a outer scope is kept in memory, it retains the entire parent scope:
```javascript
let leakyCache = null;
function leak() {
    const originalCache = leakyCache;
    const unused = function() {
        if (originalCache) console.log("hi");
    };
    leakyCache = {
        longStr: new Array(1000000).join('*'),
        someMethod: function() {
            // Retains closure environment, including originalCache!
        }
    };
}
setInterval(leak, 100); // Memory usage will climb exponentially
```

---

## 🛠️ How to Debug & Trace Memory Leaks

### Step 1: Programmatic Heap Snapshots
You can write heap snapshots directly to disk when memory usage exceeds a threshold:
```javascript
const v8 = require('v8');
const fs = require('fs');

function takeSnapshot() {
    const snapshotPath = `./heap-${Date.now()}.heapsnapshot`;
    const stream = v8.getHeapSnapshot();
    const writeStream = fs.createWriteStream(snapshotPath);
    stream.pipe(writeStream);
    console.log(`Snapshot saved to ${snapshotPath}`);
}
```

### Step 2: Compare Snapshots in Chrome DevTools
1.  Run your Node process with inspection enabled: `node --inspect index.js`.
2.  Open Google Chrome and navigate to `chrome://inspect`. Click **Inspect** next to your Node process.
3.  Go to the **Memory** tab.
4.  Capture a heap snapshot under a baseline state (Snapshot 1).
5.  Run a load-testing script (e.g., using `autocannon` or `ab` to send 10,000 HTTP requests).
6.  Capture a second heap snapshot (Snapshot 2).
7.  Select **Snapshot 2**, change the view class from *Summary* to **Comparison**, and select *Snapshot 1* as the baseline.
8.  Sort by **# Delta** (the change in object count) or **Size Delta**. Inspect the objects that grew in size to find their constructor references.

---

## 📈 CPU Profiling & Performance Diagnosis

If your application is experiencing 100% CPU usage or latency spikes, you need to identify which JavaScript functions are blocking the event loop.

### Profiling Tools:

#### 1. Node.js Native Profiler
Run your script with the `--prof` flag to write execution ticks to a log file:
```bash
node --prof index.js
# Generate load on the server
# Stop the server, then process the log file:
node --prof-process isolate-0x*-v8.log > processed_profile.txt
```
Analyze `processed_profile.txt` to find which C++ or JavaScript functions occupied the most execution ticks.

#### 2. Clinic.js
A powerful suite for Node.js performance analysis:
```bash
npm install -g clinic
```

*   **`clinic doctor`:** High-level diagnosis. It tracks CPU, Memory, Event Loop Delay, and Active Handles, identifying whether performance bottlenecks are caused by I/O, event loop blocking, or memory leaks.
    ```bash
    clinic doctor -- node index.js
    ```
*   **`clinic flame`:** Generates interactive **Flame Graphs**.
    *   *How to read:* The horizontal axis shows CPU time, and vertical blocks represent call stacks.
    *   **Wider blocks** indicate functions that occupied the thread for longer durations. Look for wide, hot-colored (red/orange) blocks to identify blocking functions.
    ```bash
    clinic flame -- node index.js
    ```
*   **`clinic bubbleprof`:** Visualizes asynchronous call flows. It maps how long execution waited between asynchronous calls (e.g. database reads, network responses), allowing you to optimize slow queueing paths.
    ```bash
    clinic bubbleprof -- node index.js
    ```
