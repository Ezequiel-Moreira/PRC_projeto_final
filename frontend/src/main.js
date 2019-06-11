import Vue from 'vue'
import vueHeadful from 'vue-headful'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false
Vue.component('vue-headful', vueHeadful)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
