# FastAPI Wallet Assignment

## Setup (local)

1. create virtualenv and install

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

# FastAPI Wallet Project

A simple wallet management API built using FastAPI. This project demonstrates user registration, wallet management, transactions, and basic security features.

---

## Features

- User registration and authentication
- Wallet creation and management
- Deposit and withdrawal functionality
- Transaction history tracking
- RESTful API endpoints with FastAPI
- Optional Docker support for containerized deployment

---

## Technologies Used

- Python 3.10+
- FastAPI
- SQLite/MySQL (for database)
- Docker (optional)
- Uvicorn (ASGI server)
- Pytest (for testing)

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/username/fastapi-wallet.git
cd fastapi-wallet
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv venv
# Activate environment:
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
pip install -r requirements.txt
Run database migrations / seed data (if any):

bash
Copy code
python seed_data.py
Run the FastAPI server:

bash
Copy code
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000.

API Endpoints
POST /users/register - Register a new user

POST /users/login - User login

GET /wallets - List all wallets

POST /wallets/deposit - Deposit money

POST /wallets/withdraw - Withdraw money

GET /transactions - View transaction history


Running Tests
pytest tests/

Example Requests
curl -X POST "http://127.0.0.1:8000/users/register" \
-H "Content-Type: application/json" \
-d '{"username": "john", "password": "1234"}'

Authors

Priyankaaa Bommani

```
