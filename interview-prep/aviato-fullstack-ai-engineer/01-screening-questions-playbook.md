# Module 01: Application Screening Questions Playbook

This playbook provides exact response strategies and structured templates for the screening questions asked in the **Aviato Consulting Fullstack AI Engineer / FDE** application.

---

## ❓ Question 1: AI-Native Tooling & Context Scoping Strategy

> *"Which AI-native development or CLI tool (e.g., Cursor, Claude Code, Gemini CLI, Antigravity) do you personally prefer and why? Walk me through exactly how you manage, restrict, and keep your local codebase context structured within that tool when executing multi-file refactors to prevent hallucinations and token bloat?"*

### 💡 Strategy & Breakdown

To stand out, your response must demonstrate **senior engineering rigor**, **token efficiency**, and **deterministic context management**. Avoid giving a generic answer like "I just use Cursor and ask it to write code."

#### 4-Pillar Response Template:

```
1. Tool Selection: AntiGravity / Claude Code (Highlight agentic workspace control)
2. Workspace Context Architecture (.agents/AGENTS.md & skills/ directory)
3. Multi-File Refactoring Protocol (Plan ➔ Scope ➔ Modify ➔ Verify)
4. Anti-Hallucination & Token Optimization Safeguards
```

### 📝 Complete Sample Response:

> "I personally prefer **AntiGravity / Claude Code** for non-trivial engineering tasks because of its deep integration with custom workspace skills, transparent tool logging, and background subagent orchestration.
>
> To keep context structured and prevent token bloat during multi-file refactors, I follow a strict 4-step workflow:
>
> 1. **System-Level Context Directory (`skills/` & `AGENTS.md`):**
>    I configure explicit workspace rules inside standard customization roots (`.agents/AGENTS.md`). I define strict behavioral rules—such as requiring source file verification before code edits, prohibiting silent try-catch fallbacks, and maintaining modular component boundaries.
>
> 2. **Explicit File Scoping (No Wildcard Token Dumps):**
>    Instead of letting the agent index whole directory trees or unneeded dependencies (`node_modules/`, `build/`), I explicitly target individual files (`@file`) and line ranges needed for the task.
>
> 3. **4-Phase Refactoring Protocol:**
>    - **Phase 1 (Inspection & Planning):** Ask the tool to inspect interfaces/types first and output an `implementation_plan.md` without making any code mutations.
>    - **Phase 2 (Type/Interface Definition):** Modify data schemas or backend Pydantic/TypeScript models first.
>    - **Phase 3 (Incremental Refactoring):** Update call sites module-by-module.
>    - **Phase 4 (Empirical Runtime Verification):** Execute unit tests or type-checks immediately after modifications.
>
> 4. **Preventing Hallucinations:**
>    I enforce a strict rule: *'Never infer object schemas or third-party API methods without viewing the authoritative definition file.'* If imported types are missing from context, the tool is required to open the source definition before consuming it."

---

## ❓ Question 2: Video Pitch — "What makes you fit for the role?"

> *Video requirement (1-2 minutes) on why you are the ideal fit for a Generative AI Forward Deployed Engineer.*

### 🎥 90-Second Video Script Blueprint

#### Section 1: The Hook (0 - 15s)
> *"Hi, I’m [Your Name]. As a Senior Fullstack Engineer with over 8 years of experience, I specialize in bridging the gap between raw Generative AI prototypes and enterprise-grade, low-latency production systems on Google Cloud Platform."*

#### Section 2: Technical Mastery & GCP Depth (15 - 45s)
> *"My core strength lies in dual-ecosystem backend engineering across Python and TypeScript—building high-throughput async APIs with FastAPI and Node.js, combined with real-time SSE token streaming to React and Next.js frontends. On GCP, I’ve architected production ML pipelines using Vertex AI, BigQuery, and Dataflow for large-scale data ingestion and vector search."*

#### Section 3: The Forward Deployed Engineer (FDE) Mindset (45 - 75s)
> *"What sets me apart as an FDE is a high-agency, founder-style execution. I don’t just write high-level architecture slides—I embed directly with clients to solve real enterprise blockers like state persistence, data readiness, and deterministic code generation in next-gen AI environments."*

#### Section 4: Culture & Call to Action (75 - 90s)
> *"Aviato’s ex-Google engineering bar and zero-bureaucracy remote culture is exactly the environment where I thrive. I’m excited to build the next generation of autonomous enterprise engines with your team."*

---

## ❓ Question 3: Current CTC & Expected CTC Positioning

* **Strategy:** Frame your expectation based on market standards for Senior Fullstack AI / Forward Deployed Engineers in top remote GCP consulting firms in India (e.g., ₹35L - ₹50L+ depending on seniority & ESOP split).
* **Sample Text:**
  > *"My expected compensation reflects a Senior Fullstack AI Engineer with 8+ years of production experience across Python, TypeScript, and GCP infrastructure. I am looking for a competitive fixed component aligned with standard senior remote rates in India, plus equity/ESOP participation after six months."*
