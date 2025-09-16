from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests

# Intentionally poor architecture on purpose for refactoring exercise.
# - Hardcoded secrets
# - Business logic inside route handlers
# - Synchronous HTTP calls in async-capable framework
# - Duplicate code and mixed concerns

app = FastAPI(title="Refactor Me API")

# Intentionally permissive CORS (bad)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hardcoded secrets (bad)
HARDCODED_USERNAME = "admin"
HARDCODED_PASSWORD = "password123"
HARDCODED_TOKEN = "secrettoken"

# Scattered magic strings (bad)
JSON_PLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/users"
DOG_API_URL = "https://dog.ceo/api/breeds/image/random"

# Global mutable state (bad)
STATE = {"last_login_user": None, "users_cache": []}


@app.post("/login")
def login(payload: dict):
    # Doing auth here with hardcoded credentials (bad)
    username = payload.get("username")
    password = payload.get("password")
    if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
        STATE["last_login_user"] = username
        return {"token": HARDCODED_TOKEN, "user": username}
    # Leaking info in error (bad)
    raise HTTPException(status_code=403, detail="Invalid credentials for user: %s" % username)


def _get_token_from_request(req: Request) -> str:
    # Accepting token via query string or bearer header, with precedence rules (bad)
    token = req.query_params.get("token")
    if not token:
        auth = req.headers.get("Authorization", "")
        if auth.startswith("Bearer "):
            token = auth.split(" ", 1)[1]
    return token


@app.get("/users")
def get_users(request: Request):
    # Ad-hoc auth check inline (bad)
    token = _get_token_from_request(request)
    if token != HARDCODED_TOKEN:
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    # Synchronous external call (bad for async server)
    try:
        resp = requests.get(JSON_PLACEHOLDER_URL, timeout=10)
        # Ignoring non-200 statuses (bad)
        data = resp.json()
        # Cache without any eviction (bad)
        STATE["users_cache"] = data
        # Do presentation shaping here (bad)
        simplified = [{"id": u.get("id"), "name": u.get("name"), "email": u.get("email")} for u in data]
        return {"items": simplified, "count": len(simplified)}
    except Exception as e:
        # Swallowing exceptions and returning partial data (bad)
        return {"items": STATE.get("users_cache", []), "error": str(e)}


@app.get("/dog")
def get_random_dog(request: Request):
    # This endpoint doesn't even check auth (inconsistent)
    try:
        resp = requests.get(DOG_API_URL, timeout=10)
        payload = resp.json()
        return {"image": payload.get("message"), "status": payload.get("status", "ok")}
    except Exception as e:
        return {"image": None, "status": "error", "error": str(e)}


@app.get("/secret-data")
def secret_data(request: Request):
    # Duplicate auth check logic (bad)
    token = _get_token_from_request(request)
    if token != HARDCODED_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Business logic inline (bad)
    return {
        "owner": STATE.get("last_login_user"),
        "note": "This is super secret data stored in memory.",
    }


if __name__ == "__main__":
    # Running via python main.py (not recommended, but convenient)
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


