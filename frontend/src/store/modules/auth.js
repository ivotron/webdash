import axios from 'axios'

const state = {
  token: null,
  profile: {},
  validation: { email: true },
  user: null,
  authError: false
}

const getters = {}

const mutations = {
  setToken(state, payload) {
    state.token = payload
  },
  setProfile (state, payload) {
    state.profile = payload
  },
  setValidationEmail (state, bool) {
    state.validation.email = bool
  },
  setAuthError (state, bool) {
    state.authError = bool
  },
  setUser (state, payload) {
    state.user = payload
  }
}
const actions = {
  logout(context) {
    context.commit('setToken', null)
  },
  postRegister (context, payload) {
    return axios.post('/api/users/register/', payload)
      .then(response => {
        if (response.data.status === 210) {
          context.commit('setValidationEmail', false)
        } else {
          context.commit('setValidationEmail', true)
          context.commit('login')
          context.commit('setProfile', response.data)
        }
      })
      .catch(e => { console.log(e) })
  },
  getProfile (context) {
    return axios.get('/api/users/profile')
      .then(response => {
        context.commit('login')
        context.commit('setProfile', response.data)
      })
      .catch(e => {
        context.commit('logout')
        console.log(e)
      })
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
