// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  extends: ['plugin:vue/essential', 'plugin:prettier/recommended'],
  rules: {
    'no-console': 0,
    'prettier/prettier': [
      'error',
      {
        singleQuote: true,
        trailingComma: 'none',
        bracketSpacing: true
      }
    ]
  }
}
