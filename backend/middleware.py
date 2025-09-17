"""
Custom middleware for the application.
Handles CORS, logging, and other cross-cutting concerns.
"""
import time
from fastapi import Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from config import settings


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging HTTP requests."""
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        # Log request
        print(f"Request: {request.method} {request.url}")
        
        # Process request
        response = await call_next(request)
        
        # Log response
        process_time = time.time() - start_time
        print(f"Response: {response.status_code} - {process_time:.4f}s")
        
        # Add timing header
        response.headers["X-Process-Time"] = str(process_time)
        
        return response


def setup_cors_middleware(app):
    """Setup CORS middleware with proper configuration."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )


def setup_logging_middleware(app):
    """Setup logging middleware."""
    app.add_middleware(LoggingMiddleware)
