/**
 * API service for handling HTTP requests
 * Centralized API communication with proper error handling
 */
import axios from 'axios'
import config from '../config'

class ApiService {
  constructor() {
    this.client = axios.create({
      baseURL: config.api.baseURL,
      timeout: config.api.timeout,
      headers: {
        'Content-Type': 'application/json',
      },
    })

    this.setupInterceptors()
  }

  setupInterceptors() {
    // Request interceptor
    this.client.interceptors.request.use(
      (config) => {
        console.log(`API Request: ${config.method?.toUpperCase()} ${config.url}`)
        return config
      },
      (error) => {
        console.error('Request error:', error)
        return Promise.reject(error)
      }
    )

    // Response interceptor
    this.client.interceptors.response.use(
      (response) => {
        console.log(`API Response: ${response.status} ${response.config.url}`)
        return response
      },
      (error) => {
        console.error('Response error:', error)
        return Promise.reject(this.handleError(error))
      }
    )
  }

  handleError(error) {
    if (error.response) {
      // Server responded with error status
      return {
        message: error.response.data?.detail || 'Server error',
        status: error.response.status,
        data: error.response.data,
      }
    } else if (error.request) {
      // Request was made but no response received
      return {
        message: 'Network error - please check your connection',
        status: 0,
        data: null,
      }
    } else {
      // Something else happened
      return {
        message: error.message || 'Unknown error occurred',
        status: 0,
        data: null,
      }
    }
  }

  // Authentication methods
  async login(credentials) {
    const response = await this.client.post('/auth/login', credentials)
    return response.data
  }

  // User methods
  async getUsers(token) {
    const response = await this.client.get('/users', {
      headers: { Authorization: `Bearer ${token}` }
    })
    return response.data
  }

  // Content methods
  async getRandomDog() {
    const response = await this.client.get('/content/dog')
    return response.data
  }

  async getSecretData(token) {
    const response = await this.client.get('/content/secret-data', {
      headers: { Authorization: `Bearer ${token}` }
    })
    return response.data
  }

  // Health check
  async healthCheck() {
    const response = await this.client.get('/health')
    return response.data
  }
}

// Export singleton instance
export const apiService = new ApiService()
export default apiService
