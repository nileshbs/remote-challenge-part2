"""
Authentication and authorization module.
Handles token generation, validation, and user authentication.
"""
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from config import settings
from database_service import DatabaseServiceFactory, DatabaseError


class AuthService:
    """Service class for handling authentication operations."""
    
    def __init__(self):
        self.security = HTTPBearer()
        self.users_db = DatabaseServiceFactory.create_users_service()
    
    def create_access_token(self, username: str) -> str:
        """Create a JWT access token for the given username."""
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
        to_encode = {
            "sub": username,
            "exp": expire,
            "iat": datetime.utcnow()
        }
        return jwt.encode(to_encode, settings.secret_key, algorithm="HS256")
    
    def verify_token(self, token: str) -> Optional[str]:
        """Verify JWT token and return username if valid."""
        try:
            payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
            username: str = payload.get("sub")
            if username is None:
                return None
            return username
        except jwt.JWTError:
            return None
    
    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticate user credentials.
        In a real application, this would check against a database.
        For this demo, we use hardcoded credentials.
        """
        # TODO: Replace with proper database authentication

        users = self.users_db.find_by_field('username', username)

        for user in users:
            if user.get('password') == password:
                return True
    
    def get_token_from_request(self, request: Request) -> Optional[str]:
        """Extract token from request headers or query parameters."""
        # Check Authorization header first
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            return auth_header.split(" ", 1)[1]
        
        # Fallback to query parameter
        return request.query_params.get("token")
    
    def require_auth(self, request: Request) -> str:
        """
        Require authentication and return username.
        Raises HTTPException if authentication fails.
        """
        token = self.get_token_from_request(request)
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing authentication token"
            )
        
        username = self.verify_token(token)
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid or expired token"
            )
        
        return username


# Global auth service instance
auth_service = AuthService()
