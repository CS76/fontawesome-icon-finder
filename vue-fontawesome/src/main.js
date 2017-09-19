import Vue from 'vue'
import App from './App.vue'
import VueClipboard from 'vue-clipboard2'

Vue.use(VueClipboard);

new Vue({
  el: '#app',
  render: h => h(App)
})
