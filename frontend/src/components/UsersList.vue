<template>
  <section class="users-section">
    <h2>Users (JSONPlaceholder)</h2>
    <div class="section-actions">
      <button @click="handleLoadUsers" :disabled="isLoading">
        {{ isLoading ? 'Loading...' : 'Load Users' }}
      </button>
      <span v-if="error" class="error-message">{{ error }}</span>
    </div>
    
    <div v-if="users.length > 0" class="users-list">
      <ul>
        <li v-for="user in users" :key="user.id" class="user-item">
          <strong>{{ user.name }}</strong> - {{ user.email }}
        </li>
      </ul>
    </div>
    
    <div v-else-if="!isLoading && !error" class="empty-state">
      Click "Load Users" to fetch user data
    </div>
  </section>
</template>

<script>
import { useUsers } from '../stores/users'
import { useAuth } from '../stores/auth'

export default {
  name: 'UsersList',
  setup() {
    const { users, isLoading, error, fetchUsers, clearError } = useUsers()
    const { token } = useAuth()

    const handleLoadUsers = async () => {
      clearError()
      try {
        await fetchUsers(token.value)
      } catch (err) {
        console.error('Failed to load users:', err)
      }
    }

    return {
      users,
      isLoading,
      error,
      handleLoadUsers,
    }
  }
}
</script>

<style scoped>
.users-section {
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
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.section-actions button:hover:not(:disabled) {
  background-color: #218838;
}

.section-actions button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

.users-list ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.user-item {
  padding: 0.5rem;
  border-bottom: 1px solid #eee;
  transition: background-color 0.2s;
}

.user-item:hover {
  background-color: #f8f9fa;
}

.user-item:last-child {
  border-bottom: none;
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
