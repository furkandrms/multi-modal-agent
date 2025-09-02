# 🚀 Backend — Agentic Architecture

## 🧠 Project Overview

This project is a **FastAPI** application powered by an **agentic architecture** (multi-agent system), **LLM-based task routing**, **session/memory management**, and **MongoDB integration**, all running in a Dockerized environment.

At its core, the **PeerAgent** autonomously routes each task to specialized agents (Code, Content, Search, or General) using **OpenAI-powered LLMs**. Every conversation is tracked by session and stored in MongoDB for full traceability.

---

## 🔧 Key Features

* 🧠 Smart task routing via **LangChain agentic framework**
* 🤖 Response generation using **LLMs (OpenAI / GPT)** for code, content, summaries, or web search
* 💾 **Session & Memory Management**: maintains context-aware conversations
* 📦 **MongoDB Logging**: every task and response saved with session IDs
* 🧩 **Fallback Agent**: graceful handling of unsupported requests
* 🐳 **Full Docker Support** (Dockerfile + docker-compose)
* 📜 **Prompt Engineering & Error Handling**
* 🧪 **Testable API with automated test coverage**

---

## 🏗️ Architecture Diagram

```
       +-----------------------+
       |        User           |
       +----------+------------+
                  |
                  v
       +-----------------------+
       |      FastAPI API      |
       +----------+------------+
                  |
                  v
       +-----------------------+
       |     PeerAgent         |  ← LangChain Router
       +-----+----+-----+------+
             |    |     |
             v    v     v
       +-----+ +-----+ +-----+
       |Code | |Content| |Search|
       |Agent| |Agent  | |Agent |
       +-----+ +-------+ +-----+
             \    |    /
              \   v   /
              +--------+
              |General |
              |Agent   |   (Fallback)
              +--------+

                  |
                  v
       +-----------------------+
       |     MongoDB Logs      |
       +-----------------------+
```

---

## 🗂️ Project Structure

```
Backend/
│
├── api/
│   └── routes.py                # FastAPI route definitions
│
├── agents/
│   ├── peer_agent.py            # Main router agent
│   ├── code_agent.py            # Code generation & analysis agent
│   ├── content_agent.py         # Content/blog/article generation agent
│   ├── search_agent.py          # Web search agent using SerpAPI
│   └── general_agent.py         # Fallback agent for unsupported tasks
│
├── database/
│   └── mongodb.py               # MongoDB connection & logging
│
├── services/
│   └── llm_service.py           # LLM invocation layer (OpenAI, etc.)
│
├── tests/
│   └── test_api.py              # API test suite (pytest)
│
├── main.py                      # App entry point
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker image setup
├── docker-compose.yml           # API + MongoDB composition
├── .env                         # Environment variables
└── README.md                    # This file
```

---

## ⚙️ Setup

### 1. Create a `.env` file

```env
OPENAI_API_KEY=sk-xxx
SERPAPI_API_KEY=xxx
MONGO_URI=mongodb://mongo:27017/
```

> 🔐 Get your keys from [OpenAI](https://platform.openai.com/) and [SerpAPI](https://serpapi.com/) (free plan available).

---

## 🐳 Run with Docker

> All dependencies are listed in `requirements.txt`.

```bash
docker-compose build --no-cache
docker-compose up
```

---

## 🛠️ API Usage

### Example Request

```http
POST /v1/agent/execute
Content-Type: application/json

{
  "task": "Write a Python function to calculate the sum of a list of numbers."
}
```

### Example Response

```json
{
  "session_id": "e3451cf8-2ba5-4c57-bf1c-95e3e1faed1c",
  "task": "Write a Python function to calculate the sum of a list of numbers.",
  "response": "...code and explanation here...",
  "memory_summary": "...conversation context here..."
}
```

---

## 🤖 Supported Agents

| Agent            | Description                                          |
| ---------------- | ---------------------------------------------------- |
| **CodeAgent**    | Python code generation, functions, classes, examples |
| **ContentAgent** | Blog posts, technical writing, descriptive content   |
| **SearchAgent**  | Web search & summarization via SerpAPI               |
| **GeneralAgent** | Fallback for unsupported or ambiguous tasks          |

---

## 🧠 Session & Memory Management

* A random `session_id` is generated at app startup and used throughout.
* Session ID is managed internally; the user doesn't need to provide it.
* Full conversation history is tracked and passed to the agent as context.
* MongoDB stores all tasks and responses with metadata.

---

## ✅ Testing

The test suite is located in `tests/test_api.py` and includes:

* Valid requests (happy paths)
* Edge cases (empty input, unsupported tasks, fallback behavior)

### Run Tests:

```bash
pytest
```

---

## 🧠 Prompt Engineering

* Each agent receives tailored instructions and conversation context.
* Example directives:

  * "Explain what this code does and give an example"
  * "Summarize the search result with at least 2 sources"
* **GeneralAgent** handles unsupported tasks gracefully with helpful messages.

---

## 👤 Author

**Furkan Durmuş**\


