<template>
  <div class="app">
    <AppHeader />
    
    <main class="main-content">
      <div v-if="!isAuthenticated" class="auth-container">
        <LoginForm />
      </div>
      
      <div v-else class="authenticated-container">
        <UsersList />
        <DogImage />
        <SecretData />
        
        <div class="debug-info">
          <small>Token: {{ token }}</small>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import { useAuth } from './stores/auth'
import AppHeader from './components/AppHeader.vue'
import LoginForm from './components/LoginForm.vue'
import UsersList from './components/UsersList.vue'
import DogImage from './components/DogImage.vue'
import SecretData from './components/SecretData.vue'

export default {
  name: 'App',
  components: {
    AppHeader,
    LoginForm,
    UsersList,
    DogImage,
    SecretData,
  },
  setup() {
    const { token, isAuthenticated } = useAuth()

    return {
      token,
      isAuthenticated,
    }
  }
}
</script>

<style>
/* Global styles */
* {
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
  color: #343a40;
  line-height: 1.6;
}

.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
  min-height: 100vh;
}

.main-content {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.auth-container {
  padding: 2rem;
}

.authenticated-container {
  padding: 1rem;
}

.debug-info {
  margin-top: 2rem;
  padding: 1rem;
  background-color: #f8f9fa;
  border-radius: 4px;
  opacity: 0.7;
  font-size: 0.8rem;
  word-break: break-all;
}

/* Responsive design */
@media (max-width: 768px) {
  .app {
    padding: 0.5rem;
  }
  
  .authenticated-container {
    padding: 0.5rem;
  }
}
</style>
