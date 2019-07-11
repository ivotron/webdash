import axios from 'axios'

const state = {
  users: [],
  user: null,
  emailFail: false,
  tokenFail: false,
  token: sessionStorage.getItem('user-token') || '',
  status: '',
}

const getters = {
  isAuthenticated: state => !!state.token,
  authStatus: state => state.status,
  userLoaded: state => !!state.user,
}

const mutations = {
  setUsers (state, users) {
    state.users = users
  },
  setUser (state, user) {
    state.user = user
  },
  setEmailFail (state, bool) {
    state.emailFail = bool
  },
  setTokenFail (state, bool) {
    state.tokenFail = bool
  }
}

const actions = {
  getUsersList (context) {
    return axios.get('/api/users')
      .then(response => { context.commit('setUsers', response.data) })
      .catch(e => { console.log(e) })
  },
  getUser (context) {
    return axios.get('/auth/user/')
      .then(response => { context.commit('setUser', response.data) })
      .catch(e => { console.log(e) })
  },
  logOut (context){
    console.log(context.state)
    return axios.post('/auth/logout/', {}, { headers: { 'Authorization':`Token ${context.state.token}` } })
      .then(response => { sessionStorage.removeItem('user-token') })
      .catch(e => { console.log(e) })
  },
  createUser (context, payload) {
    var avatar = payload.avatar
    delete payload.avatar

    return axios.post('/api/users/', payload)
      .then(response => {
        // Image upload
        if (typeof avatar === 'object') {
          let data = new FormData()
          data.append('avatar', avatar)
          return axios.patch('/api/users/' + response.data.id, data)
        }
      })
      .catch(e => { console.log(e) })
  },
  editUser (context, payload) {
    var avatar = payload.avatar
    delete payload.avatar

    return axios.patch('/api/users/' + payload.id, payload)
      .then(response => {
        // Image upload
        if (typeof avatar === 'object') {
          let data = new FormData()
          data.append('avatar', avatar)
          return axios.patch('/api/users/' + payload.id, data)
        }
      })
      .catch(e => { console.log(e) })
  },
  deleteUser (context, userId) {
    return axios.delete('/api/users/' + userId)
      .then(response => {})
      .catch(e => { console.log(e) })
  },
  passwordReset (context, user) {
    return axios.post('/api/users/password_reset/', user)
      .then(response => { context.commit('setEmailFail', false) })
      .catch(e => { context.commit('setEmailFail', true) })
  },
  passwordChange (context, payload) {
    return axios.post('/api/users/password_change/', payload)
      .then(response => { context.commit('setTokenFail', false) })
      .catch(e => { context.commit('setTokenFail', true) })
  }
}

export default {
  state,
  getters,
  mutations,
  actions
}
