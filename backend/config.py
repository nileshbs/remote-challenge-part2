"""
Configuration management for the application.
Handles environment variables and application settings.
"""
import os
from typing import Optional
from pathlib import Path


class Settings:
    """Application settings loaded from environment variables."""
    
    # Application settings
    app_name: str = "Refactor Me API"
    debug: bool = False
    host: str = "127.0.0.1"
    port: int = 8000
    
    # Security settings
    secret_key: str = "your-secret-key-change-in-production"
    access_token_expire_minutes: int = 30
    
    # CORS settings
    cors_origins: list[str] = [
        "http://10.0.0.8:5173",
        "http://localhost:5173", 
        "http://127.0.0.1:5173",
    ]
    
    # External API settings
    json_placeholder_url: str = "https://jsonplaceholder.typicode.com/users"
    dog_api_url: str = "https://dog.ceo/api/breeds/image/random"
    dog_fallback_url: str = "https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg"
    
    # Cache settings
    cache_ttl_seconds: int = 300  # 5 minutes

    # Database Configuration
    DATABASE_DIR: Path = Path(__file__).parent.parent / "database"
    USERS_FILE: Path = DATABASE_DIR / "users.json"

    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
