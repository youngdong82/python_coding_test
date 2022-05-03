import App from './components/App.js';

const root = document.querySelector('.App')
console.log('root from index.js',root);
new App({target: root});