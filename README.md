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

# 📁 Project Structure

```text
mao_project/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── orchestrator/
│   │   └── orchestrator.py
│   │
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── search_agent.py
│   │   ├── reader_agent.py
│   │   ├── writer_agent.py
│   │   └── critic_agent.py
│   │
│   ├── tools/
│   │   ├── search_tool.py
│   │   └── scraper_tool.py
│   │
│   ├── memory/
│   │   ├── vector_store.py
│   │   └── memory_manager.py
│   │
│   ├── services/
│   │   └── llm_service.py
│   │
│   ├── schemas/
│   │   │── message_schema.py
│   │
│   │── utils/
│   │    └── logger.py
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│   ├── test_llm.py
│   └── test_agents.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, FastAPI |
| AI Framework | LangChain |
| LLM Runtime | Ollama |
| Models | Mistral, LLaMA |
| Communication | Redis Pub/Sub |
| Graph Database | Neo4j |
| Vector Database | FAISS / Chroma |
| Web Scraping | BeautifulSoup |
| Frontend | Streamlit |
| APIs | Tavily Search API |

---

# Core Computer Science Concepts

## Operating Systems
- process coordination
- asynchronous execution
- resource management

## Distributed Systems
- message queues
- event-driven communication
- decentralized workflows

## DBMS
- graph databases
- vector indexing
- semantic retrieval systems

## Networking
- HTTP APIs
- protocol-based communication
- client-server architecture

## Software Engineering
- modular architecture
- abstraction layers
- scalable system design
- design patterns

## Artificial Intelligence
- LLM orchestration
- autonomous agents
- memory-augmented AI
- retrieval-augmented generation (RAG)

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/Multi-Agent-Orchestration-Research-System.git

cd Multi-Agent-Orchestration-Research-System
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows
```bash
venv\Scripts\activate
```

#### Linux / Mac
```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download:
https://ollama.com/download

---

## 5. Pull Local Model

```bash
ollama pull mistral
```

---

## 6. Configure Environment Variables

Create `.env`

```env
MODEL_PROVIDER=ollama
MODEL_NAME=mistral

TAVILY_API_KEY=your_key_here

GRAPH_DB_PASSWORD=password

REDIS_HOST=localhost
REDIS_PORT=6379
```

---

# Running the Project

## Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

---

# Example Workflow

Input:
```text
Analyze electric vehicle adoption trends in India
```

System Flow:
1. Search Agent retrieves sources
2. Reader Agent extracts webpage content
3. Writer Agent generates report
4. Critic Agent evaluates output
5. Memory Layer stores insights

---

# Future Enhancements

- Full MCP protocol support
- Agent reputation system
- Multi-modal agents
- Kubernetes deployment
- Real-time monitoring dashboard
- Autonomous planning engine

---

# License

MIT License
