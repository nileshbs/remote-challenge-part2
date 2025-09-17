"""
API route handlers.
Contains route definitions separated by domain/feature.
"""
from fastapi import APIRouter, Request, Depends, HTTPException, status
from models import (
    LoginRequest, LoginResponse, UsersResponse, 
    DogResponse, SecretDataResponse, ErrorResponse
)
from auth import auth_service
from services import user_service, secret_data_service, ExternalAPIService


# Create router instances
auth_router = APIRouter(prefix="/auth", tags=["authentication"])
users_router = APIRouter(prefix="/users", tags=["users"])
content_router = APIRouter(prefix="/content", tags=["content"])


@auth_router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """
    Authenticate user and return access token.
    """
    if not auth_service.authenticate_user(request.username, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    token = auth_service.create_access_token(request.username)
    secret_data_service.set_last_login_user(request.username)
    
    return LoginResponse(token=token, user=request.username)


@users_router.get("", response_model=UsersResponse)
async def get_users(request: Request):
    """
    Get list of users from external API.
    Requires authentication.
    """
    # Authenticate user
    username = auth_service.require_auth(request)
    
    try:
        # Fetch users from service
        users = await user_service.get_users()
        simplified_users = user_service.get_simplified_users(users)
        
        return UsersResponse(
            items=simplified_users,
            count=len(simplified_users)
        )
    
    except HTTPException:
        # Re-raise HTTP exceptions from service layer
        raise
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error: {str(e)}"
        )


@content_router.get("/dog", response_model=DogResponse)
async def get_random_dog():
    """
    Get a random dog image from external API.
    This endpoint is public (no authentication required).
    """
    try:
        async with ExternalAPIService() as api_service:
            return await api_service.fetch_random_dog()
    
    except Exception as e:
        # Return fallback response for any errors
        return DogResponse(
            image="https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg",
            status="error",
            error=str(e)
        )


@content_router.get("/secret-data", response_model=SecretDataResponse)
async def get_secret_data(request: Request):
    """
    Get secret data for authenticated user.
    Requires authentication.
    """
    # Authenticate user
    username = auth_service.require_auth(request)
    
    return secret_data_service.get_secret_data()


# Health check endpoint
health_router = APIRouter(tags=["health"])

@health_router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "message": "API is running"}
