# Chapter 4: Multi-Agent Systems & Coordination

A single agent loaded with 50 tools often fails. The model struggles to select the correct tool, suffers from context window dilution, and gets easily derailed. For complex software engineering or business workflows, you must divide the task among multiple, specialized cooperative agents.

---

## 🏗️ Multi-Agent Design Patterns

Breaking problems down into distinct agent roles improves reliability, testability, and token efficiency. Here are the three dominant patterns:

### 1. Orchestrator-Worker (Supervisor / Routing)
A central "Supervisor" agent receives the task, decides which specialized "Worker" agent is best suited, delegates the work, reads the result, and decides what to do next.

```text
               +-----------------------+
               |   Supervisor Agent    |
               +-----------------------+
                /          |          \
     (Delegate) /          | (Delegate)\ (Delegate)
               v           v            v
        [Coder Agent] [QA Agent] [Docs Agent]
```

### 2. Sequential Chains (Choreography)
A linear pipeline where the output of one agent becomes the direct input of the next:
`Research Agent` ➔ `Writer Agent` ➔ `Editor Agent` ➔ `Translator Agent`.

### 3. Bidirectional Collaboration (Creator-Critic / PM-Dev-QA)
Agents interact dynamically to refine outputs. For example, a **Developer Agent** writes code and feeds it to a **QA Agent**. The QA Agent runs tests, catches errors, and sends the errors *back* to the Developer Agent, repeating this loop until the code passes.

---

## 💾 State Sharing Architectures

When multiple agents cooperate, they must share information. There are two primary sharing models:

1.  **Message Passing:** Agents talk to each other through direct messaging. The conversation log contains all messages exchanged, which is fed to the next agent in line.
2.  **Shared State (Blackboard Pattern):** A single global memory object (like a shared database record) is accessible to all agents. E.g., the state contains `{ code: "", testResults: [], status: "writing" }`. Each agent reads from this state, updates their respective fields, and saves it back.

---

## 🛠️ Multi-Agent Frameworks

To coordinate agent loops, state transitions, and cycles, you can use specialized frameworks:

### 1. Graph-Based Routing (e.g., LangGraph)
*   Treats agent workflows as a state graph (Nodes = Agents or Functions, Edges = Transitions/Routing logic).
*   Enables cycles (e.g., looping between Dev and QA until tests pass).
*   Ensures deterministic state transitions while allowing the LLM to control logic pathways.

### 2. Conversational Agent Chats (e.g., AutoGen)
*   Focuses on conversation-driven agent execution.
*   Agents act as "chat participants" that can send messages to other agents to resolve tasks.

### 3. Role-Based Crews (e.g., CrewAI)
*   Focuses on role-playing agents (PMs, Researchers, Writers) tasked with executing specific backstories, goals, and tasks.

---

## 🏋️ Coding Challenge: Build a Developer/QA Iterative Loop

Write a Python script that orchestrates a Developer Agent and a QA Agent.

### Requirements:
1.  **Developer Agent:** Takes a prompt describing a function (e.g., "Write a function that reverses a string") and outputs Python code.
2.  **QA Agent:** Takes the generated code, executes it inside a safe context, evaluates whether it works correctly, and outputs either `"PASS"` or `"FAIL: [reason/errors]"`.
3.  **Loop:** Run the Developer Agent. Send its output to the QA Agent. If the QA Agent returns `"FAIL"`, send the feedback back to the Developer Agent so it can rewrite the function. Loop until the QA Agent outputs `"PASS"` or the iteration count exceeds 5.
