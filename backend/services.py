"""
Business logic services.
Contains the core business logic separated from route handlers.
"""
import asyncio
from typing import List, Optional
import aiohttp
from fastapi import HTTPException, status
from models import User, DogResponse, SecretDataResponse
from config import settings


class ExternalAPIService:
    """Service for interacting with external APIs."""
    
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        """Async context manager entry."""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=10),
            headers={
                "Accept": "application/json",
                "User-Agent": "RefactorMe/1.0"
            }
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.session:
            await self.session.close()
    
    async def fetch_users(self) -> List[User]:
        """Fetch users from JSONPlaceholder API."""
        if not self.session:
            raise RuntimeError("Service not properly initialized")
        
        try:
            async with self.session.get(settings.json_placeholder_url) as response:
                if response.status != 200:
                    raise HTTPException(
                        status_code=status.HTTP_502_BAD_GATEWAY,
                        detail=f"External API returned status {response.status}"
                    )
                
                data = await response.json()
                return [User(**user) for user in data]
        
        except aiohttp.ClientError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Failed to fetch users: {str(e)}"
            )
    
    async def fetch_random_dog(self) -> DogResponse:
        """Fetch a random dog image from Dog CEO API."""
        if not self.session:
            raise RuntimeError("Service not properly initialized")
        
        try:
            async with self.session.get(settings.dog_api_url) as response:
                if response.status != 200:
                    return DogResponse(
                        image=settings.dog_fallback_url,
                        status="fallback",
                        error=f"upstream:{response.status}"
                    )
                
                data = await response.json()
                image_url = data.get("message")
                
                if not image_url:
                    return DogResponse(
                        image=settings.dog_fallback_url,
                        status="fallback",
                        error="missing-image"
                    )
                
                return DogResponse(
                    image=image_url,
                    status=data.get("status", "ok")
                )
        
        except aiohttp.ClientError as e:
            return DogResponse(
                image=settings.dog_fallback_url,
                status="error",
                error=str(e)
            )


class UserService:
    """Service for user-related business logic."""
    
    def __init__(self):
        self._users_cache: List[User] = []
        self._cache_timestamp: Optional[float] = None
    
    async def get_users(self) -> List[User]:
        """
        Get users with caching.
        Returns cached users if available and not expired.
        """
        import time
        
        # Check if cache is valid
        if (self._users_cache and 
            self._cache_timestamp and 
            time.time() - self._cache_timestamp < settings.cache_ttl_seconds):
            return self._users_cache
        
        # Fetch fresh data
        async with ExternalAPIService() as api_service:
            users = await api_service.fetch_users()
            self._users_cache = users
            self._cache_timestamp = time.time()
            return users
    
    def get_simplified_users(self, users: List[User]) -> List[dict]:
        """Convert User objects to simplified dictionaries for API response."""
        return [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
            for user in users
        ]


class SecretDataService:
    """Service for secret data operations."""
    
    def __init__(self):
        self._last_login_user: Optional[str] = None
    
    def set_last_login_user(self, username: str) -> None:
        """Set the last logged in user."""
        self._last_login_user = username
    
    def get_secret_data(self) -> SecretDataResponse:
        """Get secret data for the current user."""
        return SecretDataResponse(
            owner=self._last_login_user,
            note="This is super secret data stored in memory."
        )


# Global service instances
user_service = UserService()
secret_data_service = SecretDataService()
