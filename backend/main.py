"""
Main FastAPI application.
Refactored to follow SOLID principles and best practices.
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from config import settings
from middleware import setup_cors_middleware, setup_logging_middleware
from routers import auth_router, users_router, content_router, health_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title=settings.app_name,
        description="A refactored FastAPI application following SOLID principles",
        version="1.0.0",
        debug=settings.debug
    )
    
    # Setup middleware
    setup_cors_middleware(app)
    setup_logging_middleware(app)
    
    # Include routers
    app.include_router(health_router)
    app.include_router(auth_router)
    app.include_router(users_router)
    app.include_router(content_router)
    
    # Global exception handler
    @app.exception_handler(Exception)
    async def global_exception_handler(request, exc):
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error", "error_code": "INTERNAL_ERROR"}
        )
    
    return app


# Create the app instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )


