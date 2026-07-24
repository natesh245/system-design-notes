# Module 02: System Design — Real-Time SSE Token Streaming Architecture

This module details the architectural design for real-time LLM token streaming using **Server-Sent Events (SSE)** across **FastAPI**, **Node.js**, and **React / Next.js**.

---

## 🏛️ 1. Architecture Overview

```
                                  [ USER BROWSER ]
                                         │
                         (HTTP/2 SSE: text/event-stream)
                                         ▼
                             ┌───────────────────────┐
                             │ Next.js Client App    │
                             └───────────┬───────────┘
                                         │
                                   (REST / SSE)
                                         ▼
                           ┌───────────────────────────┐
                           │   FastAPI / Node.js API   │
                           │   Async Token Router      │
                           └─────────────┬─────────────┘
                                         │
                                  (gRPC / Stream)
                                         ▼
                             ┌───────────────────────┐
                             │   LLM Inference API   │
                             └───────────────────────┘
```

---

## ⚡ 2. Backend Implementation Patterns

### Python FastAPI SSE Producer

```python
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import asyncio
import json

app = FastAPI()

async def event_generator(prompt: str, request: Request):
    """
    Asynchronously yields SSE formatted tokens to the client.
    """
    for i in range(10):
        # Check if client disconnected mid-stream
        if await request.is_disconnected():
            print("Client disconnected, aborting LLM stream.")
            break

        data = json.dumps({"token": f"chunk_{i} ", "index": i})
        yield f"data: {data}\n\n"
        await asyncio.sleep(0.05)

    yield "data: [DONE]\n\n"

@app.get("/api/v1/stream")
async def stream_tokens(prompt: str, request: Request):
    return StreamingResponse(
        event_generator(prompt, request),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )
```

---

## 🌊 3. SSE vs. WebSockets Comparison Matrix

| Metric | Server-Sent Events (SSE) | WebSockets |
| :--- | :--- | :--- |
| **Data Flow** | Unidirectional (Server ➔ Client) | Bidirectional (Server ⇆ Client) |
| **Protocol** | Standard HTTP/1.1 or HTTP/2 | Custom WS/WSS protocol over TCP |
| **Auto-Reconnect** | Native browser handling (`EventSource`) | Requires custom JavaScript reconnect logic |
| **Best For** | LLM token streaming, notification feeds | Real-time chat apps, multiplayer gaming |
