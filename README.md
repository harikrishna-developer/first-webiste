# FastAPI Order Management System

A backend application built using **Python, FastAPI, PostgreSQL, and SQLAlchemy**. This project focuses on building REST APIs with a modular architecture, database integration, and CRUD operations.

## Tech Stack

- **Programming Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy 2.0
- **Database Driver:** Psycopg2
- **Validation:** Pydantic
- **Environment Management:** Python dotenv
- **Version Control:** Git and GitHub

## Project Structure

```text
fastapi-order-management/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── user_router.py
│   │
│   └── services/
│       ├── __init__.py
│       └── user_service.py
│
├── .gitignore
├── .env
└── README.md
```

## Features

### User Management APIs

- Create a new user.
- Retrieve all users.
- Retrieve a user by ID.
- Update user information.
- Delete a user.

### Database Integration

- PostgreSQL database connectivity.
- SQLAlchemy ORM for database operations.
- Database session management.
- Environment-based database configuration.

### Application Architecture

- Separate models, schemas, routers, and services.
- Pydantic request and response validation.
- Dependency injection for database sessions.
- Modular and maintainable code structure.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/harikrishna-developer/first-webiste.git
```

### 2. Navigate to the Project Directory

```bash
cd first-webiste
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy psycopg2-binary python-dotenv
```

### 6. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/order_management_db
```

Replace the username and password with your PostgreSQL credentials.

### 7. Run the Application

```bash
uvicorn app.main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI provides interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Available API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Create a user |
| GET | `/users` | Retrieve all users |
| GET | `/users/{user_id}` | Retrieve a user by ID |
| PATCH | `/users/{user_id}` | Update user information |
| DELETE | `/users/{user_id}` | Delete a user |

## Future Enhancements

- Product management APIs.
- Order management APIs.
- Order and user relationship management.
- Authentication and authorization using JWT.
- Redis caching.
- Pagination and filtering.
- Unit testing using Pytest.
- Docker integration.

## Version Control

This project uses Git and GitHub for version control.

```bash
git add .
git commit -m "Your commit message"
git push
```

---

**Project Status:** User Management CRUD APIs implemented and tested with PostgreSQL.

**Purpose:** Hands-on learning and implementation of backend development concepts using FastAPI and PostgreSQL.

## Upcoming Features

- Product Management API