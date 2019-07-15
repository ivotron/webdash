import Vue from 'vue'
import store from './store'
import router from '@/router'

import axios from 'axios'

import VueRaven from 'vue-raven'

import VueAxios from 'vue-axios'
import VueAuthenticate from 'vue-authenticate'

import App from '@/App.vue'
import './registerServiceWorker'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false

// Sentry for logging frontend errors
if (process.env.NODE_ENV === 'production') {
  Vue.use(VueRaven, { dsn: process.env.VUE_APP_SENTRY_PUBLIC_DSN })
}

// more info: https://github.com/MatteoGabriele/vue-analytics
/*Vue.use(VueAnalytics, {
  id: process.env.VUE_APP_GOOGLE_ANALYTICS,
  router
})*/

Vue.use(VueAxios, axios)
console.log(process.env)

export var vueAuth = new VueAuthenticate.factory(Vue.prototype.$http, {
  baseUrl: process.env.VUE_APP_BASE_URL, // Your API domain
  tokenPath: 'key',
  tokenType: 'Token',
  logoutUrl: '/auth/logout/',
  storageType: null,
  providers: {
    github: {
      clientId: process.env.VUE_APP_CLIENT_ID,
      redirectUri: process.env.VUE_APP_CALLBACK_URL // Your client app URL
    }
  }
})
Vue.use(vueAuth)

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
