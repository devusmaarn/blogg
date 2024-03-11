/** @format */
const cssnano = require("cssnano");
const tailwindcss = require('tailwindcss');
const autoprefixer = require('autoprefixer');


  module.exports = {
    plugins: {
      "postcss-import": {},
      "tailwindcss/nesting": {},
      tailwindcss: {},
      autoprefixer: {},
      cssnano: {
        preset: "default",
      },
    },
  };
