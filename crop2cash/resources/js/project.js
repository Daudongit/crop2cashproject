// import Vue from 'vue'
// Vue.component('app', require('./components/App.vue').default)
// let vue = new Vue({
//     //
//   }).$mount('#app')

import Vue from 'vue'
import router from './router'
import App from './components/App'
import './plugins'
import './components'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  router,
  ...App
})