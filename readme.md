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
