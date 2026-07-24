# Module 02: System Design — Real-time SSE Token Streaming

This document details the architectural design for a high-performance, real-time LLM token streaming system built with **FastAPI / Node.js**, **Server-Sent Events (SSE)**, **Google Cloud Vertex AI**, and **Next.js / React**.

---

## 🏛️ High-Level System Architecture

```
                                  [ USER BROWSER ]
                                         │
                         (HTTP/2 SSE: text/event-stream)
                                         ▼
                             ┌───────────────────────┐
                             │  Next.js Edge Server  │
                             └───────────┬───────────┘
                                         │
                                   (REST / SSE)
                                         ▼
                           ┌───────────────────────────┐
                           │   FastAPI / Node.js API   │
                           │   Async Event Router      │
                           └─────────────┬─────────────┘
                                         │
                                  (gRPC / Stream)
                                         ▼
                             ┌───────────────────────┐
                             │ Vertex AI LLM Endpoint│
                             └───────────────────────┘
```

---

## 🔑 Technical Component Breakdown

### 1. Backend Stream Producer (FastAPI / Python)

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from google.cloud import aiplatform
import asyncio
import json

app = FastAPI()

async def generate_llm_stream(prompt: str):
    """
    Asynchronously stream tokens from Vertex AI to client via SSE.
    """
    # Initialize Vertex AI Model stream
    endpoint = aiplatform.Endpoint(endpoint_name="projects/YOUR_PROJECT/locations/us-central1/endpoints/YOUR_ENDPOINT")
    
    # Simulate async streaming chunks from Vertex AI SDK
    async for chunk in endpoint.stream_predict_async(instances=[{"prompt": prompt}]):
        token_data = json.dumps({"token": chunk.predictions[0]})
        # Standard SSE format: "data: <content>\n\n"
        yield f"data: {token_data}\n\n"
        await asyncio.sleep(0.01) # Yield control back to event loop

    yield "data: [DONE]\n\n"

@app.get("/api/v1/chat/stream")
async def chat_stream(prompt: str):
    return StreamingResponse(
        generate_llm_stream(prompt),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no" # Disable NGINX buffering for instant token delivery
        }
    )
```

---

### 2. Frontend Stream Consumer (Next.js / React)

```typescript
import { useState, useEffect } from 'react';

export function ChatStreamComponent() {
  const [messages, setMessages] = useState<string>('');
  const [isStreaming, setIsStreaming] = useState<boolean>(false);

  const startStream = (prompt: string) => {
    setIsStreaming(true);
    setMessages('');

    const eventSource = new EventSource(`/api/v1/chat/stream?prompt=${encodeURIComponent(prompt)}`);

    eventSource.onmessage = (event) => {
      if (event.data === '[DONE]') {
        eventSource.close();
        setIsStreaming(false);
        return;
      }

      const parsed = JSON.parse(event.data);
      setMessages((prev) => prev + parsed.token);
    };

    eventSource.onerror = (err) => {
      console.error('SSE connection error:', err);
      eventSource.close();
      setIsStreaming(false);
    };
  };

  return (
    <div className="p-6 max-w-2xl mx-auto bg-gray-900 text-white rounded-xl shadow-lg">
      <h2 className="text-xl font-bold mb-4">Real-time Token Stream</h2>
      <div className="min-h-[200px] p-4 bg-gray-800 rounded-lg whitespace-pre-wrap font-mono">
        {messages || 'Awaiting prompt input...'}
      </div>
      <button
        onClick={() => startStream('Explain Vector Search on GCP')}
        disabled={isStreaming}
        className="mt-4 px-6 py-2 bg-blue-600 hover:bg-blue-500 rounded-lg font-semibold"
      >
        {isStreaming ? 'Streaming...' : 'Send Query'}
      </button>
    </div>
  );
}
```

---

## ⚡ Performance Optimization & Edge Cases

| Challenge | Solution |
| :--- | :--- |
| **Proxy Buffering (NGINX / Cloudflare)** | Add header `X-Accel-Buffering: no` to prevent proxy nodes from holding tokens until buffer fills. |
| **Client Disconnection** | Monitor socket closure on backend using FastAPI `request.is_disconnected()` or Node.js `res.on('close')` to immediately abort Vertex AI stream and save tokens. |
| **High Concurrency** | Use HTTP/2 multiplexing so browsers don't hit HTTP/1.1 6-connection domain limits for SSE connections. |
