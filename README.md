# FastAPI Blog Application

A modern, high-performance web API built using **FastAPI**, offering user authentication and blog operations with SQLAlchemy and Pydantic.

---

## 🚀 Features
- **Automatic API Docs** via Swagger UI and ReDoc
- **Pydantic** for data validation and serialization
- **Dependency Injection** powered by FastAPI
- **Secure Authentication** with Passlib (bcrypt)
- CRUD operations for Blogs
- SQLAlchemy ORM for DB interactions
- Extendable for OAuth2, JWT, and API Key security

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-blog-app.git
cd fastapi-blog-app
```

### 2. Create a Virtual Environment
```bash
python3 -m venv fastapi-env
source fastapi-env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Save Requirements
```bash
pip freeze > requirements.txt
```

### 5. Setup `.gitignore`
```
__pycache__/
fastapi-env/
.env
```

---

## 🗂 Project Structure
```
fastapi-blog-app/
├── main.py                  # Entry point
├── models/                  # SQLAlchemy models
├── schemas/                 # Pydantic schemas
├── db/                      # DB session/config
├── routers/                 # Blog/User routes
├── auth/                    # Password hashing
├── requirements.txt
└── README.md
```

---

## ▶️ Running the Application
```bash
uvicorn main:app --reload
```

### Visit:
- Swagger UI → `http://127.0.0.1:8000/docs`
- ReDoc → `http://127.0.0.1:8000/redoc`

---

## 💻 Tech Stack
- **FastAPI** — Web framework
- **SQLAlchemy** — ORM
- **Pydantic** — Data validation
- **Passlib (bcrypt)** — Password hashing
- **Uvicorn** — ASGI server

---

## 🔐 Security
- Password encryption via bcrypt
- Optional extensions:
  - OAuth2 with Password Flow & JWT
  - API Keys via header, query, or cookie

---

## 💡 FastAPI Highlights
- Type-safe development (Python 3.6+)
- OpenAPI standard support
- WebSocket & GraphQL compatibility
- Background tasks, lifecycle events

