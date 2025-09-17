/**
 * Authentication store
 * Manages authentication state and operations
 */
import { ref, computed } from 'vue'
import apiService from '../services/api'

// Reactive state
const token = ref(localStorage.getItem('auth_token') || '')
const user = ref(null)
const isLoading = ref(false)
const error = ref('')

// Computed properties
const isAuthenticated = computed(() => !!token.value)
const hasError = computed(() => !!error.value)

// Actions
const login = async (credentials) => {
  isLoading.value = true
  error.value = ''
  
  try {
    const response = await apiService.login(credentials)
    token.value = response.token
    user.value = response.user
    
    // Persist token
    localStorage.setItem('auth_token', response.token)
    
    return response
  } catch (err) {
    error.value = err.message || 'Login failed'
    throw err
  } finally {
    isLoading.value = false
  }
}

const logout = () => {
  token.value = ''
  user.value = null
  error.value = ''
  localStorage.removeItem('auth_token')
}

const clearError = () => {
  error.value = ''
}

// Initialize from localStorage
if (token.value) {
  user.value = 'admin' // In a real app, you'd decode the token or fetch user info
}

export function useAuth() {
  return {
    // State
    token,
    user,
    isLoading,
    error,
    
    // Computed
    isAuthenticated,
    hasError,
    
    // Actions
    login,
    logout,
    clearError,
  }
}
