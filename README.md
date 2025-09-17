# Refactor Me - FastAPI + Vue

A refactored full-stack application demonstrating SOLID principles, clean architecture, and modern development practices. Originally a simple app with intentionally poor architecture, now transformed into a maintainable, scalable, and well-structured codebase.

## 🏗️ Architecture Overview

### Backend (FastAPI)
- **Clean Architecture**: Separation of concerns with distinct layers
- **SOLID Principles**: Single responsibility, dependency inversion, and more
- **Async/Await**: Proper async handling with aiohttp
- **JWT Authentication**: Secure token-based authentication
- **Configuration Management**: Environment-based configuration
- **Error Handling**: Comprehensive error handling and logging
- **API Documentation**: Auto-generated OpenAPI/Swagger docs

### Frontend (Vue 3 + Vite)
- **Component-Based Architecture**: Modular, reusable components
- **Composition API**: Modern Vue 3 patterns
- **State Management**: Centralized stores for different domains
- **Service Layer**: Abstracted API communication
- **Responsive Design**: Mobile-friendly UI
- **Error Handling**: User-friendly error messages

## 🚀 Features

### Backend API Endpoints
- `POST /auth/login` - User authentication with JWT tokens
- `GET /users` - Fetch users from JSONPlaceholder (authenticated)
- `GET /content/dog` - Get random dog image (public)
- `GET /content/secret-data` - Get secret data (authenticated)
- `GET /health` - Health check endpoint

### Frontend Features
- **Authentication Flow**: Login/logout with token persistence
- **User Management**: Display and manage user data
- **Content Display**: Random dog images and secret data
- **Responsive UI**: Clean, modern interface
- **Error Handling**: Graceful error states and user feedback

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework
- **Pydantic** - Data validation and settings management
- **aiohttp** - Async HTTP client
- **python-jose** - JWT token handling
- **uvicorn** - ASGI server

### Frontend
- **Vue 3** - Progressive JavaScript framework
- **Vite** - Fast build tool and dev server
- **Axios** - HTTP client
- **Composition API** - Modern Vue patterns

## 📋 Prerequisites

- **Python 3.10+**
- **Node.js 18+**
- **npm** or **yarn**

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <repository-url>
cd part2
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

The API will be available at `http://127.0.0.1:8000`
- API Documentation: `http://127.0.0.1:8000/docs`
- Alternative docs: `http://127.0.0.1:8000/redoc`

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The app will be available at `http://127.0.0.1:5173`

## 🔧 Configuration

### Backend Configuration
Create a `.env` file in the `backend` directory:

```env
# Application Configuration
APP_NAME="Refactor Me API"
DEBUG=false
HOST=127.0.0.1
PORT=8000

# Security Configuration
SECRET_KEY=your-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Configuration
CORS_ORIGINS=["http://localhost:5173", "http://127.0.0.1:5173"]

# External API Configuration
JSON_PLACEHOLDER_URL=https://jsonplaceholder.typicode.com/users
DOG_API_URL=https://dog.ceo/api/breeds/image/random
DOG_FALLBACK_URL=https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg

# Cache Configuration
CACHE_TTL_SECONDS=300
```

### Frontend Configuration
Create a `.env` file in the `frontend` directory:

```env
# API Configuration
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## 🏛️ Architecture Details

### Backend Structure
```
backend/
├── main.py              # Application entry point
├── config.py            # Configuration management
├── models.py            # Pydantic models and schemas
├── auth.py              # Authentication service
├── services.py          # Business logic services
├── routers.py           # API route handlers
├── middleware.py        # Custom middleware
└── requirements.txt     # Python dependencies
```

### Frontend Structure
```
frontend/src/
├── main.js              # Application entry point
├── App.vue              # Root component
├── config/
│   └── index.js         # Configuration management
├── services/
│   └── api.js           # API service layer
├── stores/
│   ├── auth.js          # Authentication store
│   ├── users.js         # Users store
│   └── content.js       # Content store
└── components/
    ├── AppHeader.vue    # Application header
    ├── LoginForm.vue    # Login form component
    ├── UsersList.vue    # Users list component
    ├── DogImage.vue     # Dog image component
    └── SecretData.vue   # Secret data component
```

## 🔐 Authentication

The application uses JWT (JSON Web Tokens) for authentication:

1. **Login**: POST credentials to `/auth/login`
2. **Token**: Receive JWT token in response
3. **Authorization**: Include token in `Authorization: Bearer <token>` header
4. **Persistence**: Token is stored in localStorage

### Default Credentials
- **Username**: `admin`
- **Password**: `password123`

## 🧪 Testing

### Backend Testing
```bash
cd backend
# Run with pytest (when tests are added)
pytest
```

### Frontend Testing
```bash
cd frontend
# Run with vitest (when tests are added)
npm run test
```

## 📦 Building for Production

### Backend
```bash
cd backend
# Install production dependencies
pip install -r requirements.txt

# Run with production server
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
# Build for production
npm run build

# Preview production build
npm run preview
```

## 🔍 Code Quality

### SOLID Principles Applied

1. **Single Responsibility Principle (SRP)**
   - Each class/function has one reason to change
   - Separate concerns: auth, services, models, routes

2. **Open/Closed Principle (OCP)**
   - Open for extension, closed for modification
   - Plugin-based middleware and service architecture

3. **Liskov Substitution Principle (LSP)**
   - Derived classes are substitutable for base classes
   - Consistent interfaces across services

4. **Interface Segregation Principle (ISP)**
   - Clients shouldn't depend on unused interfaces
   - Focused, specific service interfaces

5. **Dependency Inversion Principle (DIP)**
   - Depend on abstractions, not concretions
   - Dependency injection and service abstraction

### Best Practices Implemented

- **Configuration Management**: Environment-based settings
- **Error Handling**: Comprehensive error handling and logging
- **Async Programming**: Proper async/await patterns
- **Security**: JWT authentication, CORS configuration
- **Documentation**: Comprehensive code documentation
- **Modularity**: Separation of concerns and modular design
- **Testing Ready**: Structure prepared for unit and integration tests

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   - Backend: Change `PORT` in `.env` or kill process on port 8000
   - Frontend: Change port in `vite.config.js` or kill process on port 5173

2. **CORS Errors**
   - Ensure backend CORS origins include your frontend URL
   - Check that both servers are running

3. **Authentication Issues**
   - Verify JWT secret key is consistent
   - Check token expiration settings

4. **External API Failures**
   - Check internet connection
   - Verify external API endpoints are accessible

## 📝 Development Notes

### Key Improvements Made

1. **Backend Refactoring**:
   - Separated business logic from route handlers
   - Implemented proper async patterns
   - Added comprehensive error handling
   - Created modular service architecture
   - Added JWT authentication
   - Implemented configuration management

2. **Frontend Refactoring**:
   - Broke monolithic component into smaller, focused components
   - Implemented proper state management
   - Added service layer for API communication
   - Improved error handling and user feedback
   - Added responsive design
   - Implemented proper authentication flow

## 📄 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

For questions or issues, please open an issue in the repository.


