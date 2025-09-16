# Refactor Me - FastAPI + Vue

A tiny full-stack app that uses public APIs. It works, and it's intentionally simple.

## What it does
- Backend (FastAPI):
  - `/login` authenticates a user and returns a token
  - `/users` fetches users from JSONPlaceholder
  - `/dog` returns a random dog image from Dog CEO API
  - `/secret-data` returns a small protected payload
- Frontend (Vue 3 + Vite):
  - One page to log in, list users, show a random dog image, and load a secret payload

## Prerequisites
- Python 3.10+
- Node.js 18+

## Running the backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python main.py
```
API: `http://127.0.0.1:8000`

## Running the frontend
```bash
cd frontend
npm install
npm run dev
```
App: `http://127.0.0.1:5173`

## Notes
- The frontend expects the backend at `http://127.0.0.1:8000`.
- If ports are occupied, update the configs accordingly.

## License
MIT


