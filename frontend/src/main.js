import { createApp, ref, onMounted } from 'vue'
import axios from 'axios'

// Intentionally poor structure: everything in one file, globals, hardcoded URLs,
// mixed responsibilities, no components, no stores.

const BACKEND = 'http://127.0.0.1:8000' // hardcoded, should be env
const HARDCODED_TOKEN = 'secrettoken' // mirrors backend token incorrectly

const App = {
  setup() {
    const username = ref('admin')
    const password = ref('password123')
    const token = ref('')
    const loginError = ref('')
    const users = ref([])
    const dogUrl = ref('')
    const secret = ref('')

    const doLogin = async () => {
      loginError.value = ''
      try {
        const r = await axios.post(`${BACKEND}/login`, { username: username.value, password: password.value })
        token.value = r.data.token
      } catch (e) {
        loginError.value = (e.response && e.response.data && e.response.data.detail) || 'Login failed'
      }
    }

    const loadUsers = async () => {
      try {
        const r = await axios.get(`${BACKEND}/users`, {
          headers: { Authorization: `Bearer ${token.value || HARDCODED_TOKEN}` },
          params: { token: token.value ? token.value : undefined }, // confusing double auth path
        })
        users.value = r.data.items
      } catch (e) {
        users.value = []
      }
    }

    const loadDog = async () => {
      const r = await axios.get(`${BACKEND}/dog`)
      dogUrl.value = r.data.image
    }

    const loadSecret = async () => {
      const r = await axios.get(`${BACKEND}/secret-data`, {
        headers: { Authorization: `Bearer ${token.value || HARDCODED_TOKEN}` },
      })
      secret.value = `${r.data.owner}: ${r.data.note}`
    }

    onMounted(() => {
      // auto-load a dog image on mount for visual sanity
      loadDog()
    })

    return { username, password, token, loginError, users, dogUrl, secret, doLogin, loadUsers, loadDog, loadSecret }
  },
  template: `
    <div style="font-family: sans-serif; margin: 1rem; max-width: 800px;">
      <h1>Refactor Me - Vue + FastAPI</h1>

      <section style="border: 1px solid #ddd; padding: 1rem; margin-bottom: 1rem;">
        <h2>Login</h2>
        <div style="display:flex; gap: 0.5rem; align-items: center; flex-wrap: wrap;">
          <input placeholder="username" v-model="username" />
          <input placeholder="password" type="password" v-model="password" />
          <button @click="doLogin">Login</button>
          <span v-if="token">Token: {{ token }}</span>
          <span v-if="loginError" style="color:red;">{{ loginError }}</span>
        </div>
      </section>

      <section style="border: 1px solid #ddd; padding: 1rem; margin-bottom: 1rem;">
        <h2>Users (JSONPlaceholder)</h2>
        <button @click="loadUsers">Load Users</button>
        <ul>
          <li v-for="u in users" :key="u.id">{{ u.name }} - {{ u.email }}</li>
        </ul>
      </section>

      <section style="border: 1px solid #ddd; padding: 1rem; margin-bottom: 1rem;">
        <h2>Random Dog</h2>
        <button @click="loadDog">Refresh</button>
        <div v-if="dogUrl">
          <img :src="dogUrl" alt="random dog" style="max-width: 100%; height: auto;" />
        </div>
      </section>

      <section style="border: 1px solid #ddd; padding: 1rem;">
        <h2>Secret Data</h2>
        <button @click="loadSecret">Load Secret</button>
        <div v-if="secret">{{ secret }}</div>
      </section>
    </div>
  `
}

createApp(App).mount('#app')


