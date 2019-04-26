// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Vue from 'vue'
import App from './App'
import VueParticles from 'vue-particles'
import router from './router'
import axios from 'axios'
import {
  fabric
} from 'fabric'

Vue.use(ElementUI)
Vue.use(VueParticles)
Vue.use(fabric)
Vue.config.productionTip = false

Vue.prototype.$http = axios
Vue.prototype.HOST = '/api'
axios.defaults.baseURL = 'http://127.0.0.1:8000'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed'
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {
    App
  },
  template: '<App/>'
})
