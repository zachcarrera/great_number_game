/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./static/src/**/*.js", "./server.py"],
  theme: {
    extend: {},
  },
  plugins: [require("@tailwindcss/forms")],
};
