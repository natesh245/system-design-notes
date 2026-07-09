# Agentic AI Engineering Curriculum

Welcome to the Agentic AI Engineering Roadmap. This curriculum is designed to take you from a solid understanding of LLMs to building, evaluation, and scaling production-grade autonomous agentic systems.

---

## 🗺️ Curriculum Overview

The roadmap is structured into 5 logical pillars, moving from single-agent concepts to multi-agent choreography and production guardrails.

| Chapter | Topic | Key Focus Areas |
| :--- | :--- | :--- |
| **01** | [Foundations & Reasoning Patterns](./01-foundations-reasoning.md) | Prompt Engineering for Agents, Chain-of-Thought (CoT), ReAct pattern, and Structured Outputs. |
| **02** | [Tool Execution & Sandboxing](./02-tool-execution-sandboxing.md) | Function calling, API translation, tool schema generation, and secure runtime sandboxing. |
| **03** | [Memory & State Management](./03-memory-state-management.md) | Short-term context management, Long-term memory (vector search, semantic memory), and state persistence. |
| **04** | [Multi-Agent Systems & Coordination](./04-multi-agent-coordination.md) | Orchestrator-worker patterns, routing, consensus, and frameworks (e.g., LangGraph, AutoGen). |
| **05** | [Evaluation, Guardrails & Production](./05-evaluation-guardrails-production.md) | Agent evaluation, trajectory tracing, rate-limiting, and preventing agent loops / prompt injections. |

---

## 📚 Chapter Breakdown

### 🧩 Chapter 1: Agentic Foundations & Reasoning
To build agents, you must move beyond simple Q&A prompting. This chapter covers how LLMs reason, plan, and invoke actions.
*   **Concepts:**
    *   **ReAct (Reason/Act) Loop:** The fundamental loop of choosing an action, observing the result, and reasoning about the next step.
    *   **Self-Correction:** Getting the LLM to inspect its own outputs (e.g., "Review your code for syntax errors before returning it").
    *   **Structured Output Generation:** Using JSON Schema, Pydantic, or native model formatting to ensure the agent outputs parsable arguments for tools.
*   **Practical Project:** Implement a raw Python/Node.js script that runs a CLI loop: taking user input, generating a tool-calling action, and running a math evaluation tool manually without any agent framework.

---

### 🛠️ Chapter 2: Tool Integration & Execution
Agents are only useful if they can affect the external world. This chapter focuses on how agents interface with code, databases, and APIs.
*   **Concepts:**
    *   **Function Calling:** Model-native tool binding (e.g., OpenAI Tool Calling, Gemini Function Calling).
    *   **Schema Definition:** Translating functions into OpenAPI or JSON Schema so models understand *when* and *how* to call them.
    *   **Secure Execution Environment:** Running arbitrary code securely (Docker containers, WASM sandboxes, e2b, gVisor) to prevent malicious actions on host systems.
*   **Practical Project:** Build an agent that can interact with a SQL database, automatically generating queries, executing them, and refining the queries if the database returns an error.

---

### 🧠 Chapter 3: State & Memory Architectures
A stateless model cannot perform long-running workflows. This chapter covers how agents remember past states, execution paths, and user history.
*   **Concepts:**
    *   **Short-Term Memory:** Conversational context and system prompt size optimization (sliding windows, summarizing past context).
    *   **Long-Term Semantic Memory:** Storing experiences in Vector Databases (Chroma, Pinecone, pgvector) using embeddings, retrieving relevant historical solutions when facing a similar task.
    *   **Entity Memory:** Dynamically updating a database of facts about entities (e.g., remembering a user's name or preferred programming language across sessions).
*   **Practical Project:** Build a customer support agent that reads user history from a vector store, updates its profile state dynamically during the conversation, and saves a summary of the session upon exit.

---

### 🤝 Chapter 4: Multi-Agent Systems & Choreography
For complex tasks, a single agent often gets confused. Breaking the problem down into a team of specialized agents is the standard industry pattern.
*   **Concepts:**
    *   **Orchestrator-Worker Pattern:** One central supervisor agent directs work to multiple specialist sub-agents.
    *   **Routing & State Machines:** Graph-based agent paths (e.g., LangGraph) where execution routes from writer agent ➔ critic agent ➔ publisher agent based on defined states.
    *   **Agent Communication Protocols:** How agents exchange messages, negotiate contracts, and achieve consensus.
*   **Practical Project:** Create a software development team: a **Product Manager Agent** (creates specs), a **Developer Agent** (writes code), and a **QA Agent** (reviews and runs tests). Run them in a loop until the QA Agent approves the code.

---

### 🛡️ Chapter 5: Monitoring, Evaluation & Guardrails
Deploying autonomous code to production requires rigorous testing and guardrails to prevent infinite loops, astronomical API bills, and security breaches.
*   **Concepts:**
    *   **Agent Evaluation (Eval Suites):** LLM-as-a-judge, deterministic tests, and testing agent trajectories (did it take the most efficient path?).
    *   **Tracing:** Log and visualize entire agent execution graphs (using tools like LangSmith, Phoenix, or OpenTelemetry).
    *   **Guardrails:** Request rate limits, budget ceilings ($ USD limits per task), token thresholds, and prompt injection filters.
*   **Practical Project:** Implement a task runner agent equipped with safety middleware that halts execution if the cumulative cost of API calls for a single task exceeds $2.00, or if the agent executes more than 15 tool steps (detecting infinite loops).
