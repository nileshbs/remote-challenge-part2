<template>
  <header class="app-header">
    <h1>{{ appName }}</h1>
    <div v-if="isAuthenticated" class="user-info">
      <span class="user-name">Welcome, {{ user }}!</span>
      <button @click="handleLogout" class="logout-btn">Logout</button>
    </div>
  </header>
</template>

<script>
import { useAuth } from '../stores/auth'
import config from '../config'

export default {
  name: 'AppHeader',
  setup() {
    const { user, isAuthenticated, logout } = useAuth()

    const handleLogout = () => {
      logout()
    }

    return {
      appName: config.app.name,
      user,
      isAuthenticated,
      handleLogout,
    }
  }
}
</script>

<style scoped>
.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 2px solid #e9ecef;
  margin-bottom: 2rem;
}

.app-header h1 {
  margin: 0;
  color: #343a40;
  font-size: 1.8rem;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-name {
  color: #6c757d;
  font-weight: 500;
}

.logout-btn {
  padding: 0.5rem 1rem;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  transition: background-color 0.2s;
}

.logout-btn:hover {
  background-color: #c82333;
}
</style>
