# 🚀 The Recommended Learning Order for AI & Agentic Engineering

When mastering modern AI systems engineering, learning these 5 disciplines in the correct order is critical. Each step builds directly upon the concepts, constraints, and mental models of the previous step.

---

## 🧭 The 5-Step Learning Pathway Overview

> [!NOTE]
> Make sure you review [**00-prerequisites.md**](./00-prerequisites.md) for foundational software engineering, async programming, and vector search concepts before starting Step 1.

```
┌───────────────────────────┐
│ 1. Prompt Engineering     │  (Atomic Foundation: LLM Behavior & Output Formatting)
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ 2. Context Engineering    │  (Working Memory: Information Retrieval, Token Budgeting & State)
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ 3. Loop Engineering       │  (Execution Control Flow: ReAct Cycles, Reflection & Stop Conditions)
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ 4. Harness Engineering    │  (Infrastructure & Runtime: Sandboxing, Tooling, Evals & Security)
└─────────────┬─────────────┘
              │
              ▼
┌───────────────────────────┐
│ 5. Agentic Engineering    │  (Macro Systems Design: Multi-Agent Topologies, Orchestration & Production)
└───────────────────────────┘
```

---

## 1. Prompt Engineering (The Atomic Foundation)
- **What it is**: The art and science of formulating single-shot or few-shot instructions, system prompts, role definitions, and structured output constraints (e.g., JSON Schema/Pydantic) to steer raw base/chat model behavior predictably.
- **Key Concepts**: System instructions, Chain-of-Thought (CoT), Few-shot examples, JSON mode/Structured outputs, Guardrails within prompts, Temperature & sampling parameter tuning.
- **Why Learn First?**: Before you can build loops or systems, you must deeply understand how the core engine (the LLM) responds to instructions, where it fails, how context layout affects attention, and how to get deterministic, parseable outputs.

---

## 2. Context Engineering (The Working Memory Layer)
- **What it is**: Managing what exact tokens enter the model's context window at any given turn. It spans dynamic context assembly, vector retrieval (RAG), context pruning, transcript summarization, and token budget management.
- **Key Concepts**: Dynamic RAG & Chunking, Prompt Caching, Sliding Context Windows, Short-term vs. Long-term Memory, Token Budgeting, Context Pruning/Compression, System prompt vs User prompt formatting.
- **Why Learn Second?**: An LLM is stateless; its "memory" is only what fits in the context window. Once you know how to write effective prompts, you must learn how to dynamically assemble, hydrate, and maintain relevant context across multi-turn interactions without exhausting token limits or diluting attention (needle-in-a-haystack issue).

---

## 3. Loop Engineering (The Autonomous Control Flow)
- **What it is**: Designing stateful, iterative execution loops that transform an LLM from a single turn text-in/text-out function into an autonomous agent capable of solving multi-step tasks.
- **Key Concepts**: ReAct (Reasoning + Action) loops, Reflection & Self-Correction cycles, Tool-calling loops, Deterministic state machines (e.g., LangGraph/State Machines), Stopping/Termination criteria, Retry & Exception handling loops.
- **Why Learn Third?**: With prompting mastered and context dynamically managed, you can now construct the iterative reasoning cycle. Loop engineering defines how the LLM thinks, acts, inspects tool results, reflects on errors, and decides whether to stop or try another approach.

---

## 4. Harness Engineering (Infrastructure, Runtime & Safety)
- **What it is**: Constructing the host environment, tool interfaces, evaluation harnesses, sandboxing, and safety mechanisms surrounding the execution loop.
- **Key Concepts**: Model Context Protocol (MCP) servers/clients, Docker/Wasm code execution sandboxes, State persistence & checkpointing, Eval harnesses (benchmarks, trajectory logging), Telemetry/Tracing (OpenTelemetry), Permission/Human-in-the-loop gates.
- **Why Learn Fourth?**: A raw loop running on a host machine is dangerous and unreliable. Harness engineering wraps the loop with safe tool execution, sandboxed code interpreters, automated eval suites to measure trajectory performance, and robust state persistence/recovery mechanisms.

---

## 5. Agentic Engineering (Macro Systems Architecture)
- **What it is**: The high-level systems design and architecture of multi-agent networks, autonomous subagent delegation, distributed workflows, and enterprise AI production pipelines.
- **Key Concepts**: Multi-agent topologies (Supervisor-Worker, Hierarchical, Peer-to-Peer Swarms), Subagent spawning & context isolation, Asynchronous agent messaging, Human-in-the-Loop (HITL) workflows, Production deployment, SLA management, Cost & Latency optimization.
- **Why Learn Fifth?**: Agentic engineering represents the macro systems level. It synthesizes all previous layers—individual agents (Loops + Harnesses) equipped with memory (Context) and honed prompts (Prompt Engineering) orchestrated together to solve complex enterprise problems.
