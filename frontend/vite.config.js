import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    host: true, // Allow external connections
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
  },
  define: {
    // Enable Vue devtools in development
    __VUE_PROD_DEVTOOLS__: false,
  }
})


