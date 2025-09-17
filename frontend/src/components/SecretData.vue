<template>
  <section class="secret-section">
    <h2>Secret Data</h2>
    <div class="section-actions">
      <button @click="handleLoadSecret" :disabled="isLoading">
        {{ isLoading ? 'Loading...' : 'Load Secret' }}
      </button>
      <span v-if="error" class="error-message">{{ error }}</span>
    </div>
    
    <div v-if="secretData" class="secret-content">
      {{ secretData }}
    </div>
    
    <div v-else-if="!isLoading && !error" class="empty-state">
      Click "Load Secret" to fetch secret data
    </div>
  </section>
</template>

<script>
import { useContent } from '../stores/content'
import { useAuth } from '../stores/auth'

export default {
  name: 'SecretData',
  setup() {
    const { secretData, isLoading, error, fetchSecretData, clearError } = useContent()
    const { token } = useAuth()

    const handleLoadSecret = async () => {
      clearError()
      try {
        await fetchSecretData(token.value)
      } catch (err) {
        console.error('Failed to load secret data:', err)
      }
    }

    return {
      secretData,
      isLoading,
      error,
      handleLoadSecret,
    }
  }
}
</script>

<style scoped>
.secret-section {
  border: 1px solid #ddd;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
}

.section-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1rem;
  flex-wrap: wrap;
}

.section-actions button {
  padding: 0.5rem 1rem;
  background-color: #6f42c1;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.section-actions button:hover:not(:disabled) {
  background-color: #5a32a3;
}

.section-actions button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

.secret-content {
  background-color: #f8f9fa;
  padding: 1rem;
  border-radius: 4px;
  border-left: 4px solid #6f42c1;
  font-family: monospace;
  word-break: break-word;
}

.empty-state {
  color: #6c757d;
  font-style: italic;
  text-align: center;
  padding: 2rem;
}

.error-message {
  color: #dc3545;
  font-size: 0.9rem;
}
</style>
