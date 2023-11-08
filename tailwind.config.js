/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./public/**/*.{html,js}",
  ],
  plugins: [
    require("rippleui"),
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['"Plus Jakarta Sans"'],
      },
      backgroundImage: {
        'hero-pattern': "url('bg.jpg')",
      }
    }
  },
}

