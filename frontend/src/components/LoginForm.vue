<template>
  <section class="login-section">
    <h2>Login</h2>
    <form @submit.prevent="handleLogin" class="login-form">
      <div class="form-group">
        <input
          v-model="username"
          type="text"
          placeholder="Username"
          required
          :disabled="isLoading"
        />
      </div>
      <div class="form-group">
        <input
          v-model="password"
          type="password"
          placeholder="Password"
          required
          :disabled="isLoading"
        />
      </div>
      <div class="form-actions">
        <button type="submit" :disabled="isLoading">
          {{ isLoading ? 'Logging in...' : 'Login' }}
        </button>
        <span v-if="error" class="error-message">{{ error }}</span>
      </div>
      <div>
        <p>Use <strong>admin</strong> / <strong>password123</strong> to log in as sample account.</p>
      </div>
    </form>
  </section>
</template>

<script>
import { ref } from 'vue'
import { useAuth } from '../stores/auth'

export default {
  name: 'LoginForm',
  setup() {
    const { login, isLoading, error, clearError } = useAuth()
    const username = ref('')
    const password = ref('')

    const handleLogin = async () => {
      clearError()
      try {
        await login({
          username: username.value,
          password: password.value
        })
      } catch (err) {
        // Error is handled by the store
        console.error('Login failed:', err)
      }
    }

    return {
      username,
      password,
      isLoading,
      error,
      handleLogin,
    }
  }
}
</script>

<style scoped>
.login-section {
  border: 1px solid #ddd;
  padding: 1rem;
  margin-bottom: 1rem;
  border-radius: 8px;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group input {
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.form-group input:focus {
  outline: none;
  border-color: #007bff;
  box-shadow: 0 0 0 2px rgba(0, 123, 255, 0.25);
}

.form-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.form-actions button {
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.form-actions button:hover:not(:disabled) {
  background-color: #0056b3;
}

.form-actions button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

.error-message {
  color: #dc3545;
  font-size: 0.9rem;
}
</style>
