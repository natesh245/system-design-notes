# Module 04: Dual-Stack Backend Mastery (Python & Node.js)

This module provides technical explanations, concurrency mechanics, and stream handling for **Python (FastAPI / `asyncio`)** and **Node.js (TypeScript / V8 / `libuv`)**.

---

## 🐍 1. Python Concurrency & FastAPI Mechanics

- **`asyncio` Event Loop:** Cooperative single-threaded loop. Async functions yield execution at `await`.
- **Global Interpreter Lock (GIL):** Prevents parallel execution of Python bytecode across multiple threads.
- **CPU Offloading:** CPU-heavy tasks (vector calculations, data transformations) must be offloaded to `concurrent.futures.ProcessPoolExecutor` or worker queues to prevent blocking the event loop.

```python
import asyncio
from concurrent.futures import ProcessPoolExecutor

def compute_heavy_embeddings(data: list) -> list:
    return [x * 2 for x in data]

async def process_request(data: list):
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, compute_heavy_embeddings, data)
    return result
```

---

## 🟢 2. Node.js V8 & `libuv` Event Loop

Node.js executes JavaScript on a single thread using the V8 engine, while asynchronous I/O operations (file system, network) are offloaded to the C++ `libuv` thread pool (default size = 4).

### Key Event Loop Phases
1. **Timers:** Executes `setTimeout` and `setInterval` callbacks.
2. **Pending Callbacks:** Executes deferred I/O callbacks.
3. **Poll:** Retrieves new I/O events.
4. **Check:** Executes `setImmediate()` callbacks.

---

## ⚖️ 3. Python vs Node.js Comparison Matrix

| Dimension | Python (FastAPI / `asyncio`) | Node.js (TypeScript / Express) |
| :--- | :--- | :--- |
| **Concurrency** | Single-threaded `asyncio` + GIL | Single-threaded V8 loop + `libuv` I/O threads |
| **Data Validation** | Pydantic V2 (Rust core, fast parsing) | Zod / TypeBox (Compile & runtime TS validation) |
| **Streaming Primitive**| `StreamingResponse(async_generator)` | `TransformStream`, `ReadableStream`, Piping |
