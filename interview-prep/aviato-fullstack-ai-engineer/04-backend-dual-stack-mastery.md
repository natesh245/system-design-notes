# Module 04: Dual-Stack Backend Mastery (Python & Node.js)

This document provides deep technical explanations, code patterns, and runtime mechanics for both **Python (FastAPI / `asyncio`)** and **Node.js (TypeScript / V8 / Event Loop)** tailored for AI engineering interviews.

---

## 🐍 Part 1: Python Concurrency & FastAPI

### 1. `asyncio` Event Loop vs Multiprocessing
- **Single-Threaded Event Loop:** Python's `asyncio` runs a single-threaded cooperative event loop. Non-blocking I/O operations (network calls to Vertex AI, vector DB queries) yield execution to other tasks via `await`.
- **Global Interpreter Lock (GIL):** CPU-bound tasks (e.g., local matrix multiplication or embedding transformations) block the `asyncio` event loop! 
- **Solution for CPU-bound tasks:** Offload to `concurrent.futures.ProcessPoolExecutor` or background worker tasks (Celery / Cloud Tasks).

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

def heavy_cpu_matrix_transform(data: list) -> list:
    # CPU-heavy computation
    return [x * 2 for x in data]

async def handle_request(raw_data: list):
    loop = asyncio.get_running_loop()
    # Offload CPU work to a separate process to avoid blocking the asyncio loop!
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, heavy_cpu_matrix_transform, raw_data)
    return result
```

---

## 🟢 Part 2: Node.js Architecture & Concurrency

### 1. V8 Isolate & `libuv` Event Loop Phases
Node.js processes run inside a single **V8 Isolate**. Non-blocking asynchronous I/O is offloaded to the C++ `libuv` thread pool (default 4 threads).

```
   ┌──────────────────────────┐
┌─>│          Timers          │ (setTimeout, setInterval)
│  └────────────┬─────────────┘
│  ┌────────────┴─────────────┐
│  │     Pending Callbacks    │ (I/O callbacks deferred)
│  └────────────┬─────────────┘
│  ┌────────────┴─────────────┐
│  │      Idle, Prepare       │ (Internal use)
│  └────────────┬─────────────┘
│  ┌────────────┴─────────────┐
│  │           Poll           │ (Fetch new I/O events)
│  └────────────┬─────────────┘
│  ┌────────────┴─────────────┐
│  │           Check          │ (setImmediate callbacks)
│  └────────────┬─────────────┘
│  ┌────────────┴─────────────┐
└──┤      Close Callbacks     │ (socket.on('close'))
   └──────────────────────────┘
```

### 2. Node.js Streaming API (Handling Token Streams)

```typescript
import { Transform, Readable } from 'stream';

export function createTokenTransformStream() {
  return new Transform({
    transform(chunk, encoding, callback) {
      try {
        const text = chunk.toString();
        const jsonPayload = JSON.stringify({ data: text, timestamp: Date.now() });
        this.push(`data: ${jsonPayload}\n\n`);
        callback();
      } catch (err) {
        callback(err as Error);
      }
    }
  });
}
```

---

## ⚖️ Python vs Node.js Core Comparison

| Dimension | Python (FastAPI / `asyncio`) | Node.js (TypeScript / Express / Fastify) |
| :--- | :--- | :--- |
| **Concurrency Model** | Single-threaded `asyncio` event loop + GIL | Single-threaded V8 loop + `libuv` I/O thread pool |
| **Best For in AI** | LLM orchestrations, PyTorch/TensorFlow, Pydantic schemas | High-throughput web routing, real-time WebSocket/SSE services |
| **Streaming Mechanism** | `StreamingResponse(generator())` | Readable / Transform Streams, Response Piping |
