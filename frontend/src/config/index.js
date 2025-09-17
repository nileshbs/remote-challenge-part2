/**
 * Application configuration
 * Centralized configuration management
 */

const config = {
  // API Configuration
  api: {
    baseURL: import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000',
    timeout: 10000,
  },
  
  // Application Configuration
  app: {
    name: 'Refactor Me - Vue + FastAPI',
    version: '1.0.0',
  },
  
  // UI Configuration
  ui: {
    theme: 'light',
    maxWidth: '800px',
  }
}

export default config
