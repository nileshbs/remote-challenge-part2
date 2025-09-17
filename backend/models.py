"""
Data models and schemas for the application.
Defines Pydantic models for request/response validation.
"""
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Login request model."""
    username: str
    password: str


class LoginResponse(BaseModel):
    """Login response model."""
    token: str
    user: str


class User(BaseModel):
    """User model from external API."""
    id: int
    name: str
    email: EmailStr
    username: Optional[str] = None
    phone: Optional[str] = None
    website: Optional[str] = None


class UsersResponse(BaseModel):
    """Users API response model."""
    items: List[User]
    count: int


class DogResponse(BaseModel):
    """Dog API response model."""
    image: str
    status: str
    error: Optional[str] = None


class SecretDataResponse(BaseModel):
    """Secret data response model."""
    owner: Optional[str]
    note: str


class ErrorResponse(BaseModel):
    """Error response model."""
    detail: str
    error_code: Optional[str] = None
