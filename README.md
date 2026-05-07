# 🚀 Multi-Agent Orchestration Research System (MAO)

An advanced AI-powered Multi-Agent Orchestration System that autonomously performs end-to-end research workflows using specialized collaborating agents, distributed communication, memory systems, and LLM orchestration.

---

# Overview

This project simulates a scalable autonomous AI organization where multiple specialized agents collaborate to perform complex research tasks.

The system is capable of:
- searching the web for real-time information
- scraping and processing webpage content
- generating structured research reports
- critiquing and refining outputs
- maintaining contextual memory across workflows

The architecture is inspired by modern autonomous AI systems and emerging standards such as:
- MCP (Model Context Protocol)
- A2A (Agent-to-Agent Communication)
- Memory-Augmented AI Systems

---

# Core Features

## 🔹 Multi-Agent Architecture

Specialized AI agents collaborate under a centralized orchestrator:

| Agent | Responsibility |
|---|---|
| Search Agent | Retrieves web data |
| Reader Agent | Scrapes and cleans content |
| Writer Agent | Generates reports |
| Critic Agent | Evaluates outputs |
| Orchestrator | Coordinates workflow |

---

## 🔹 Autonomous Orchestration

The orchestrator:
- decomposes tasks
- routes work to agents
- manages workflow state
- controls execution order
- handles retries and coordination

---

## 🔹 Distributed Communication Layer

Implements asynchronous communication using:
- Redis Pub/Sub
- event-driven messaging
- distributed task coordination

---

## 🔹 LLM Abstraction Layer

Supports:
- local LLM inference using Ollama
- cloud models (OpenAI compatible)
- provider-independent architecture

---

## Memory Architecture

### Short-Term Memory
Maintains active session context.

### Working Memory
Stores intermediate workflow results.

### Long-Term Memory
Uses vector databases for semantic retrieval and persistent memory.

---

## Graph-Based Tool Registry

Uses Neo4j to:
- store tool relationships
- rank relevant tools dynamically
- reduce context-window bloat
- improve retrieval efficiency

---

# System Architecture

```text
                ┌────────────────────┐
                │      Frontend      │
                │   (Streamlit UI)   │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   FastAPI Server   │
                │   (Orchestrator)   │
                └─────────┬──────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
 ┌────────────┐   ┌────────────┐   ┌────────────┐
 │ Search     │   │ Reader     │   │ Writer     │
 │ Agent      │   │ Agent      │   │ Agent      │
 └────┬───────┘   └────┬───────┘   └────┬───────┘
      │                │                │
      ▼                ▼                ▼
   Web APIs      BeautifulSoup      LLM Model
                                      │
                                      ▼
                              ┌────────────┐
                              │ Critic     │
                              │ Agent      │
                              └────┬───────┘
                                   │
                                   ▼
                         ┌──────────────────┐
                         │ Memory Layer     │
                         │ (FAISS + Logs)   │
                         └──────────────────┘
