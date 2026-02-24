/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          text:  '#181818',
          body:  '#4b4b4b',
          bg:    '#f3f3f3',
          muted: '#a8a29e',
          gold:  '#cfa935',
          blue:  '#334155',
        }
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Helvetica Neue', 'Arial', 'sans-serif'],
      }
    }
  },
  plugins: [],
}
