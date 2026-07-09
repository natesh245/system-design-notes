# Chapter 3: Memory & State Management

An agent must maintain state to execute multi-step plans. Without memory, every request is a stateless API call, making it impossible to handle long-running workflows, user profiles, or multi-turn execution history.

---

## 🧠 Memory Taxonomies

Agent memory is split into three main categories based on scope, lifespan, and retrieval:

```text
               +--------------------------------------+
               |             Agent Memory             |
               +--------------------------------------+
                 /                |                 \
  +------------------+   +------------------+   +------------------+
  |    Short-Term    |   |    Long-Term     |   |      Entity      |
  | (Context Window) |   |   (Vector DB)    |   |    (KV Store)    |
  +------------------+   +------------------+   +------------------+
  - Current chat hist-   - Past sessions    -   - Facts & profiles -
  - Active tool logs     - Docs & manuals   -   - Static settings  -
```

---

## 1. Short-Term Memory (Context Window Management)

Short-term memory stores the active conversation messages, system prompt, and intermediate tool responses. Since context windows have strict token limits and incur direct cost, you cannot feed an infinite log to the LLM.

### Optimization Strategies:
1.  **Sliding Window:** Keep only the last $N$ messages, discarding older messages.
2.  **Summarization:** Every time the chat context reaches a threshold (e.g., 2000 tokens), feed the oldest messages to an LLM to generate a summary. Replace those old messages with the single summary block in the system prompt.
3.  **Buffer Truncation:** Hard-prune old messages starting from the top, ensuring system instructions are never deleted.

---

## 2. Long-Term Memory (Semantic Retrieval)

Long-term memory is used to remember events, facts, or instructions across different days, sessions, or processes. 

### How it works under the hood:
1.  **Writing:** The agent writes notes about its performance or user preferences (e.g., "User prefers TypeScript over JavaScript").
2.  **Vectorization:** These notes are passed through an embedding model to generate numerical vectors.
3.  **Storage:** The vectors are stored in a **Vector Database** (Chroma, Pinecone, Milvus, pgvector).
4.  **Retrieval:** When a user sends a prompt, the agent searches the vector database for the most semantically similar memories, injecting them into the current prompt as background context.

---

## 3. Entity & Key-Value Memory

Instead of searching text semantically, some information should be structured as key-value pairs (e.g., `user_timezone: "PST"`, `preferred_model: "gemini-1.5-pro"`). 
*   The agent has a tool like `update_user_profile(key, value)`.
*   During conversation, if the user mentions something relevant, the agent invokes this tool to save structured facts to a database table or JSON file.

---

## 💾 State Persistence (Agent Resume/Audit)

For production applications, agent runs are long-lived and asynchronous. The entire execution graph (state) must be serializable to a database (like SQLite or Postgres).

### This enables:
1.  **Checkpointing:** If the server crashes mid-plan, the agent can be resumed from the exact state of its last completed step.
2.  **Human-in-the-Loop:** Pausing the agent when it reaches a sensitive step (e.g., charging a card), waiting for manual approval, and resuming execution once the approval is registered.

---

## 🏋️ Coding Challenge: Build a Summary Memory Buffer

Implement an agent runner class in Python or JavaScript that handles automated summarization.

### Requirements:
1.  Keep a list of conversation messages.
2.  Write a check: if the total token count of the messages exceeds `3000 tokens`, trigger a summarization step.
3.  Run a secondary LLM request that summarizes the oldest messages into a concise paragraph.
4.  Remove the summarized messages from the list and insert the summary paragraph as a new system instruction at the beginning of the context window.
