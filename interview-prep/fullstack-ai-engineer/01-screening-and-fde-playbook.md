# Module 01: FDE Mindset, AI Tooling & Context Management

This module details the core competencies of a **Generative AI Forward Deployed Engineer (FDE)** and provides screening interview answers, AI context scoping strategies, and token optimization protocols.

---

## 🚀 1. What is a Forward Deployed Engineer (FDE)?

Unlike traditional internal product engineers or advisory consultants, a **Forward Deployed Engineer (FDE)** is a high-agency builder who embeds directly within client/enterprise environments to bridge the gap between AI prototypes and production-grade software.

```
┌─────────────────────────────────┐
│  AI Prototypes / PoC Models     │
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│ Forward Deployed Engineer (FDE) │  <-- Resolves Data Readiness, Latency, State & Security
└────────────────┬────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│ Enterprise Production System    │
└─────────────────────────────────┘
```

### Core FDE Responsibilities:
- **Productionization:** Turning fragile prompt chains into resilient, low-latency microservices.
- **Context Scoping:** Structuring enterprise codebases and vector stores to ensure AI tools operate deterministically.
- **Feedback Loop:** Transforming real-world client deployment blockers into product features.

---

## 🛠️ 2. AI CLI & Context Scoping Protocol (AntiGravity, Claude Code, Cursor)

When executing multi-file refactors using AI-native CLI or editor tools, preventing **token bloat** and **hallucinations** is critical.

### The 4-Pillar Context Architecture

```
.agents/AGENTS.md           <-- Workspace-wide behavioral rules & constraints
skills/                    <-- Specialized instructions for domain tasks
architecture.md            <-- Module boundary mapping & API specs
```

#### Rule 1: Workspace Rule File (`.agents/AGENTS.md`)
Define strict global rules:
- *'Never infer third-party API schemas without inspecting the definition file.'*
- *'No dummy fallback values or swallowed exceptions during error handling.'*
- *'Verify runtime compilation/tests after code mutations.'*

#### Rule 2: Explicit File Reference (`@file`)
Never dump full workspace directories into context. Explicitly reference only target files (`@src/components/Chat.tsx`) and line ranges.

#### Rule 3: 4-Step Refactoring Execution Loop
1. **Plan:** Ask the AI tool to inspect target schemas and output an `implementation_plan.md`.
2. **Schema Update:** Update underlying TypeScript types or Pydantic models first.
3. **Refactor:** Modify call sites incrementally.
4. **Verify:** Run type-checkers or unit test commands.

---

## 💬 3. Standard Screening Question Answer Scripts

### Screening Question: AI Context Management
> *"How do you manage codebase context in AI tools to prevent hallucinations and token bloat during multi-file refactors?"*

**Answer Script:**
> "I manage codebase context using a 4-tier strategy:
> 1. **Structured Workspace Rules:** I maintain explicit rule files (`.agents/AGENTS.md`) defining module boundaries and style constraints.
> 2. **Explicit File Scoping:** I avoid auto-indexing large directories or build artifacts, passing only explicit file links (`@file`) to the context window.
> 3. **Interface-First Refactoring:** I have the tool inspect and update data schemas/types before touching implementation files.
> 4. **Empirical Verification:** I require the AI tool to run test suites after modifications rather than assuming generated code works."
