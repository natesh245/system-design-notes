# Module 05: Adaptive Frontend Architecture (Next.js, React, Tailwind & SSE)

This module covers frontend architecture for AI applications using **React**, **Next.js App Router**, **Tailwind CSS**, and Server-Sent Events (SSE).

---

## 🎨 1. Next.js App Router Architecture

- **Server Components:** Render on the server, zero bundle size, fetch initial metadata and server state.
- **Client Components (`"use client"`):** Handle dynamic interactive state, SSE token streaming, EventSource listeners, and user inputs.

---

## 🌊 2. Reusable SSE Streaming React Hook

```typescript
'use client';
import { useState, useRef, useCallback } from 'react';

export function useSSEStream() {
  const [text, setText] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  const abortRef = useRef<AbortController | null>(null);

  const startStream = useCallback(async (endpoint: string, prompt: string) => {
    setIsStreaming(true);
    setText('');
    abortRef.current = new AbortController();

    try {
      const res = await fetch(`${endpoint}?prompt=${encodeURIComponent(prompt)}`, {
        signal: abortRef.current.signal,
      });

      if (!res.body) return;
      const reader = res.body.getReader();
      const decoder = new TextDecoder();

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value, { stream: true });
        const lines = chunk.split('\n\n');

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const dataStr = line.replace('data: ', '').trim();
            if (dataStr === '[DONE]') {
              setIsStreaming(false);
              return;
            }
            const parsed = JSON.parse(dataStr);
            setText((prev) => prev + (parsed.token || ''));
          }
        }
      }
    } catch (err) {
      console.error(err);
    } finally {
      setIsStreaming(false);
    }
  }, []);

  return { text, isStreaming, startStream };
}
```

---

## 💅 3. Tailwind CSS Glassmorphism Design Tokens

```tsx
<div className="p-6 bg-slate-900/60 backdrop-blur-xl border border-slate-800/80 rounded-2xl shadow-2xl">
  <h3 className="text-sm font-semibold tracking-wide text-cyan-400 uppercase">AI Output Stream</h3>
  <div className="mt-3 text-slate-200 font-mono text-sm leading-relaxed whitespace-pre-wrap">
    {text || 'Waiting for input...'}
  </div>
</div>
```
