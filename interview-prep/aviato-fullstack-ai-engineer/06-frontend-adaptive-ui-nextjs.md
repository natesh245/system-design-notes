# Module 06: Adaptive Frontend Architecture (Next.js, React, Tailwind CSS & SSE)

This module covers the frontend requirements from the Aviato job description: building responsive, adaptive UIs using **React**, **Next.js**, **Tailwind CSS**, dynamic AI-generated component modules, and **Server-Sent Events (SSE)** for real-time LLM token streaming.

---

## 🎨 1. Next.js App Router Architecture for AI Apps

### Server vs. Client Component Boundary
In Next.js (App Router), static content and initial data fetching are executed on the server, while interactive token-streaming state lives in Client Components.

```
app/
├── chat/
│   ├── page.tsx          <-- Server Component (Metadata, Shell, Initial Layout)
│   └── ChatInterface.tsx <-- "use client" (SSE EventSource, State, Token Accumulator)
```

```tsx
// app/chat/page.tsx (Server Component)
import { ChatInterface } from './ChatInterface';

export const metadata = {
  title: 'AI Agent Studio | Aviato Consulting',
  description: 'Real-time AI Agent Interface powered by GCP & Vertex AI',
};

export default function ChatPage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      <header className="border-b border-slate-800 p-4 font-semibold text-lg flex items-center justify-between">
        <span>⚡ Aviato AI Command Center</span>
        <span className="text-xs bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 px-2 py-1 rounded-full">
          Vertex AI Online
        </span>
      </header>
      <ChatInterface />
    </main>
  );
}
```

---

## 🌊 2. Real-Time Token Streaming Hook with Auto-Scroll & Abort Handling

```tsx
// app/chat/useSSEStream.ts
'use client';
import { useState, useRef, useCallback } from 'react';

export function useSSEStream() {
  const [content, setContent] = useState('');
  const [isStreaming, setIsStreaming] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const abortControllerRef = useRef<AbortController | null>(null);

  const streamResponse = useCallback(async (prompt: string) => {
    setIsStreaming(true);
    setContent('');
    setError(null);

    // Allow user cancellation
    abortControllerRef.current = new AbortController();

    try {
      const response = await fetch(`/api/v1/chat/stream?prompt=${encodeURIComponent(prompt)}`, {
        signal: abortControllerRef.current.signal,
      });

      if (!response.ok || !response.body) {
        throw new Error(`HTTP error ${response.status}`);
      }

      const reader = response.body.getReader();
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
            try {
              const parsed = JSON.parse(dataStr);
              setContent((prev) => prev + (parsed.token || ''));
            } catch {
              // Fallback for raw text chunks
              setContent((prev) => prev + dataStr);
            }
          }
        }
      }
    } catch (err: any) {
      if (err.name !== 'AbortError') {
        setError(err.message || 'Stream connection failed');
      }
    } finally {
      setIsStreaming(false);
    }
  }, []);

  const stopStream = useCallback(() => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
      setIsStreaming(false);
    }
  }, []);

  return { content, isStreaming, error, streamResponse, stopStream };
}
```

---

## 🧩 3. Rendering Dynamic AI-Generated Components

In modern AI-native frontends, the backend often emits structured component metadata alongside text. Below is how to render dynamic UI modules dynamically using React and Tailwind.

```tsx
// Component Registry for AI-rendered widgets
import { CodeBlock } from '@/components/CodeBlock';
import { MetricsChart } from '@/components/MetricsChart';

const COMPONENT_REGISTRY: Record<string, React.ComponentType<any>> = {
  code_block: CodeBlock,
  metrics_chart: MetricsChart,
};

interface AIComponentPayload {
  type: string;
  props: Record<string, any>;
}

export function DynamicAIComponentRenderer({ payload }: { payload: AIComponentPayload }) {
  const Component = COMPONENT_REGISTRY[payload.type];

  if (!Component) {
    return <div className="text-amber-400 text-xs font-mono">Unknown AI Component Widget</div>;
  }

  return (
    <div className="my-3 p-4 rounded-xl border border-slate-800 bg-slate-900/50 backdrop-blur-md">
      <Component {...payload.props} />
    </div>
  );
}
```

---

## 💅 4. Premium Design Aesthetics (Tailwind CSS Best Practices)
- **Glassmorphism & Backdrop Filters:** `bg-slate-900/60 backdrop-blur-xl border border-slate-800/80`
- **Dynamic Accent Colors:** Custom HSL tokens (`#0B9ED9` matching Aviato brand identity).
- **Typography:** `font-sans` using Google Font Inter, with `font-mono` code blocks.
- **Micro-Animations:** Smooth pulse loading indicators (`animate-pulse`), transitions (`transition-all duration-300 ease-in-out`).

---

## ❓ Common Frontend Interview Questions

### Q: Why use Fetch with ReadableStream instead of raw EventSource for SSE in React/Next.js?
**Answer:**
The native browser `EventSource` API only supports `GET` requests and cannot pass custom Authorization HTTP headers (`Bearer token`). Using `fetch()` with `response.body.getReader()` allows sending `POST` requests with JSON payloads (e.g. system messages, conversation history) and custom HTTP headers, while still decoding streaming chunks.
