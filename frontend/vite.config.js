import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// Intentionally misusing config: hardcoded backend URL and no envs
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    proxy: {
      // Proxy not actually used by code, left here confusingly
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      }
    }
  }
})


