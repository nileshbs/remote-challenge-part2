/**
 * Users store
 * Manages user data state and operations
 */
import { ref } from 'vue'
import apiService from '../services/api'

// Reactive state
const users = ref([])
const isLoading = ref(false)
const error = ref('')

// Actions
const fetchUsers = async (token) => {
  isLoading.value = true
  error.value = ''
  
  try {
    const response = await apiService.getUsers(token)
    users.value = response.items || []
    return response
  } catch (err) {
    error.value = err.message || 'Failed to fetch users'
    users.value = []
    throw err
  } finally {
    isLoading.value = false
  }
}

const clearUsers = () => {
  users.value = []
  error.value = ''
}

const clearError = () => {
  error.value = ''
}

export function useUsers() {
  return {
    // State
    users,
    isLoading,
    error,
    
    // Actions
    fetchUsers,
    clearUsers,
    clearError,
  }
}
