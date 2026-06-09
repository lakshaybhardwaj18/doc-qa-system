# Doc QA System

A production-grade document Q&A backend built with FastAPI, PostgreSQL, Redis, and Docker.
Users can register, authenticate, and upload documents. Week 2 will add LLM-powered Q&A.

## Architecture

[you'll add diagram here — Step 3]

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| API Framework | FastAPI | REST API with automatic docs |
| Database | PostgreSQL + SQLAlchemy | Persistent document storage |
| Cache | Redis | Fast document retrieval |
| Auth | JWT + bcrypt | Secure authentication |
| Containerization | Docker + docker-compose | Consistent deployment |

## Features

- User registration and login with JWT authentication
- Password hashing with bcrypt
- Document CRUD with PostgreSQL persistence
- Redis caching layer with cache hit/miss logging
- Rate limiting on auth endpoints
- CORS configured for frontend integration
- Global error handling
- Fully dockerized — runs with one command

## Getting Started

### Prerequisites
- Docker Desktop installed and running

### Run the project

```bash
git clone <your-repo-url>
cd doc-a-qa-system
docker-compose up --build
```

API available at: http://localhost:8000
Docs available at: http://localhost:8000/docs

### Environment Variables

| Variable | Description |
|---|---|
| DATABASE_URL | PostgreSQL connection string |
| SECRET_KEY | JWT signing secret |
| ALGORITHM | JWT algorithm (HS256) |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiry |
| REDIS_URL | Redis connection string |

## API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | /auth/register | No | Register new user |
| POST | /auth/login | No | Login, returns JWT |
| POST | /documents/ | Yes | Create document |
| GET | /documents/{id} | Yes | Get document (cached) |
| GET | /health | No | Health check |

## Project Structure
app/
├── main.py           # App setup, middleware, routers
├── database.py       # DB engine and session
├── auth_utils.py     # JWT and password utilities
├── cache.py          # Redis cache helpers
├── middleware.py     # Global error handlers
├── models/
│   ├── document.py   # Document DB model
│   └── user.py       # User DB model
└── routes/
├── auth.py       # Register and login routes
└── documents.py  # Document CRUD routes

## System Design Decisions

**Why Redis caching?**
Document reads are frequent. Caching avoids repeated DB queries for the same document.
Cache TTL is 300 seconds — balances freshness with performance.

**Why JWT over sessions?**
Stateless auth scales horizontally. No server-side session storage needed.

**Why Docker?**
Eliminates environment inconsistencies. One command runs the full stack anywhere.