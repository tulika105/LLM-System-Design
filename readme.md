# 🚀 LLM Gateway – Backend System Design with FastAPI

A production-style LLM Gateway built using **FastAPI** to explore how real-world LLM backends work. It demonstrates authentication,  per-user rate limiting, token-level cost tracking, fallback handling, and persistent usage storage.

This project was built primarily for **learning and understanding backend architecture and system design concepts behind LLM-based systems**.
---

## 🧠 Project Goal

The goal of this project was to understand how scalable LLM backends operate in production environments by implementing core infrastructure components such as authentication, request control, cost tracking, and modular service design.

---

## ✨ Features

- 🔐 **API Key Authentication** (per-user isolation)
- ⏳ **Per-user Rate Limiting** (10 requests per minute)
- 🤖 **Groq LLaMA Model Integration**
- 🔁 **Primary → Fallback Model Strategy**
- 💰 **Token-level Cost Accounting** (input/output pricing simulation)
- 💾 **Persistent Usage Tracking** (JSON-based storage)
- 🧱 **Layered Architecture with Service Abstraction**
- 📄 **Automatic API documentation via Swagger**

---

## 📦 Project Structure

```
LLM-SYSTEM-DESIGN/
│
├── app/                               # Main application package
│   ├── main.py                        # Entry point of FastAPI app; initializes and registers routes
│   │
│   ├── api/
│   │   └── routes.py                  # Defines API endpoints (/chat, /usage, /health) and orchestrates services
│   │
│   ├── services/                      # Business logic layer
│   │   ├── auth_service.py            # Handles API key authentication and user identification
│   │   ├── rate_limit_service.py      # Implements per-user rate limiting (10 requests/min)
│   │   ├── llm_service.py             # Integrates Groq LLaMA models with fallback + token extraction
│   │   └── usage_service.py           # Tracks usage, calculates cost, persists data to JSON
│   │
│   ├── models/
│   │   └── schemas.py                 # Pydantic models for request/response validation
│   │
│   └── storage/
│       └── usage.json                 # Persistent storage for per-user usage & cost tracking
│
├── requirements.txt                   # Python dependencies for the project

```

---
                  
## 📊 Architecture Diagram

```
Client
   │
   ▼
FastAPI Router
   │
   ▼
Authentication Service
   │
   ▼
Rate Limiting Service
   │
   ▼
LLM Service (Groq API)
   │
   ├── Primary Model (LLaMA 70B)
   └── Fallback Model (LLaMA 8B)
   │
   ▼
Usage Service
   │
   ▼
JSON Storage (usage.json)
```

---

## 🏗️ Architecture Overview

```
Client
   ↓
API Layer (routes.py)
   ↓
Service Layer
   ├── auth_service.py
   ├── rate_limit_service.py
   ├── llm_service.py
   └── usage_service.py
   ↓
Storage Layer (usage.json)
```

### Layer Responsibilities

| Layer | Responsibility |
|------|---------------|
| API Layer | Handles HTTP requests & responses |
| Service Layer | Business logic & orchestration |
| Model Layer | Pydantic validation contracts |
| Storage Layer | Persistent usage tracking |

---

## 🔄 Request Flow

1. User sends request to `/chat`
2. API key is authenticated
3. Rate limit is validated
4. Primary LLM model is called
5. If the primary model fails → fallback model is triggered
6. Token usage and simulated cost are calculated
7. Usage data is persisted to storage
8. Structured response is returned to the client

---

# 📡 Example API Usage

## 1️⃣ `/chat` Endpoint

Used to send a prompt to the LLM and receive a response.

### Endpoint

```
POST /chat
```

### Headers

```
X-API-Key: user1-key
```

### Body

```json
{
  "message": "Explain rate limiting in simple terms"
}
```

### Example Response

```json
{
  "response": "Rate limiting is a technique used to control how many requests a user can make to an API within a specific time window...",
  "model_used": "llama3.3-70b-versatile",
  "input_tokens": 42,
  "output_tokens": 100,
  "total_tokens": 142,
  "latency": 1.21
}
```

---

## 2️⃣ `/usage` Endpoint

Used to retrieve usage statistics for the authenticated user.

### Endpoint

```
GET /usage
```

### Headers

```
X-API-Key: user1-key
```

### Example Response

```json
{
  "user_id": "user_1",
  "total_requests": 8,
  "total_tokens": 1120,
  "total_cost": 0.0045
}
```

---

## 🛠 Tech Stack

- **FastAPI**
- **Groq (LLaMA models)**
- **Pydantic**
- **Uvicorn**
- **Python**
- **JSON-based storage (simulated persistence)**

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

## 🎓 What I Learned From This Project

Through building this system, I explored several backend and system design concepts:

- Dependency Injection in FastAPI
- Stateless vs Stateful backend design
- Sync vs Async execution model
- Layered architecture and separation of concerns
- Service abstraction patterns
- Rate limiting implementation
- Token-level cost accounting concepts for LLM systems
- Fallback strategies for system reliability
- Persistent storage design (using JSON to simulate a database)

This project helped me move beyond simply calling LLM APIs and better understand **how scalable AI backend systems are structured and managed**.

---

## 📌 Key Takeaway

This project focuses on **the backend infrastructure required to manage LLM systems reliably**, including request control, usage tracking, modular architecture, and system resilience.

It was built as a learning exercise to understand **how real-world AI systems manage requests, costs, and reliability at the backend level**.

---

⭐ If you find this project interesting, feel free to explore the code and connect!




