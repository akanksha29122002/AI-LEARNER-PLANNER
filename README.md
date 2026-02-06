# 🎓 Adaptive AI Learning Planner

An intelligent agentic workflow designed to generate, evaluate, and adapt structured learning roadmaps. It uses a **multi-agent system** to break down complex goals into daily schedules and iterates based on feasibility checks and human feedback.

---

## 📖 Overview

The **Adaptive AI Learning Planner** is not just a simple prompt wrapper. It is a stateful application built with **LangGraph** that orchestrates three distinct AI agents:
1.  **Decomposer Agent:** Breaks high-level goals (e.g., "Learn React in 10 days") into granular technical topics.
2.  **Scheduler Agent:** Maps topics to a calendar based on user constraints (hours/day).
3.  **Evaluator Agent:** Acts as a critic to ensure the plan is realistic before showing it to the user.

---

## 🏗️ Architecture

The system follows a cyclic graph architecture allowing for self-correction and human-in-the-loop adaptation.

```mermaid
graph TD
    Start([User Input]) --> Decomposer
    Decomposer[Decomposition Agent] --> Scheduler
    Scheduler[Scheduler Agent] --> Evaluator
    Evaluator[Evaluator Agent] -- "Not Feasible" --> Scheduler
    Evaluator -- "Feasible" --> HumanReview
    HumanReview[Streamlit UI] -- "Request Changes" --> Scheduler
    HumanReview -- "Approve" --> End([Final Plan])
