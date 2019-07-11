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
Vue.use(VueAuthenticate, {
  baseUrl: 'http://127.0.0.1:8000', // Your API domain
  tokenPath: 'key',
  providers: {
    github: {
      clientId: 'cc102efd3cc9c51922cb',
      redirectUri: 'http://127.0.0.1:8000/auth/github/' // Your client app URL
    }
  }
})

new Vue({
  router,
  store,

  render: h => h(App)
}).$mount('#app')
