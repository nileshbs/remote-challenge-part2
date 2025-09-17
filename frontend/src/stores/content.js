/**
 * Content store
 * Manages content data state and operations (dog images, secret data)
 */
import { ref } from 'vue'
import apiService from '../services/api'

// Reactive state
const dogImage = ref('')
const secretData = ref('')
const isLoading = ref(false)
const error = ref('')

// Actions
const fetchRandomDog = async () => {
  isLoading.value = true
  error.value = ''
  
  try {
    const response = await apiService.getRandomDog()
    dogImage.value = response.image || ''
    return response
  } catch (err) {
    error.value = err.message || 'Failed to fetch dog image'
    throw err
  } finally {
    isLoading.value = false
  }
}

const fetchSecretData = async (token) => {
  isLoading.value = true
  error.value = ''
  
  try {
    const response = await apiService.getSecretData(token)
    secretData.value = `${response.owner}: ${response.note}`
    return response
  } catch (err) {
    error.value = err.message || 'Failed to fetch secret data'
    secretData.value = ''
    throw err
  } finally {
    isLoading.value = false
  }
}

const clearContent = () => {
  dogImage.value = ''
  secretData.value = ''
  error.value = ''
}

const clearError = () => {
  error.value = ''
}

export function useContent() {
  return {
    // State
    dogImage,
    secretData,
    isLoading,
    error,
    
    // Actions
    fetchRandomDog,
    fetchSecretData,
    clearContent,
    clearError,
  }
}
