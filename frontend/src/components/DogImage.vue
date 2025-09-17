<template>
  <section class="dog-section">
    <h2>Random Dog</h2>
    <div class="section-actions">
      <button @click="handleLoadDog" :disabled="isLoading">
        {{ isLoading ? 'Loading...' : 'Refresh' }}
      </button>
      <span v-if="error" class="error-message">{{ error }}</span>
    </div>
    
    <div v-if="dogImage" class="dog-image-container">
      <img :src="dogImage" alt="Random dog" class="dog-image" />
    </div>
    
    <div v-else-if="!isLoading && !error" class="empty-state">
      Click "Refresh" to load a random dog image
    </div>
  </section>
</template>

<script>
import { useContent } from '../stores/content'

export default {
  name: 'DogImage',
  setup() {
    const { dogImage, isLoading, error, fetchRandomDog, clearError } = useContent()

    const handleLoadDog = async () => {
      clearError()
      try {
        await fetchRandomDog()
      } catch (err) {
        console.error('Failed to load dog image:', err)
      }
    }

    return {
      dogImage,
      isLoading,
      error,
      handleLoadDog,
    }
  }
}
</script>

<style scoped>
.dog-section {
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
  background-color: #17a2b8;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.section-actions button:hover:not(:disabled) {
  background-color: #138496;
}

.section-actions button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

.dog-image-container {
  text-align: center;
}

.dog-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.dog-image:hover {
  transform: scale(1.02);
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
