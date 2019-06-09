module.exports = {
  root: true,
  env: {
    node: true
  },
  'extends': [
    'plugin:vue/essential',
    '@vue/standard'
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-tabs': 'off',
    'indent': 'off',
    'no-multiple-empty-lines':'off',
    'space-before-blocks':'off',
    'space-before-function-paren':'off',
    'key-spacing':'off',
    'object-curly-spacing':'off',
    'quotes':'off',
    'keyword-spacing':'off',
    'arrow-spacing':'off',
    'comma-spacing':'off',
    'no-trailing-spaces':'off',
    'no-unused-vars':'off'
  },
  parserOptions: {
    parser: 'babel-eslint'
  }
}
