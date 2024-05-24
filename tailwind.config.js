/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        "primary-blue":  "rgb(70,155,216)",
        "primary-blue-dark": "rgb(41,40,93)",
        "primary-gold": "rgb(244,180,73)",
        "primary-gold-light": "rgb(253,240,218,0.9)",
        
      },
      fontFamily: {
        'helvetica-compressed': "helvetica-compressed"
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}

