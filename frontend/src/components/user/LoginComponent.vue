<template>
  <div class="centered-container">
    <md-content class="md-elevation-3">

      <div class="title md-layout-item ">
        <div class="md-title">Blackswan</div>
        <div class="md-body-1">Sign in to Github to continue to Blackswan</div>
      </div>

      <div class="actions md-layout md-gutter md-alignment-center-space-between">
        <div class="md-layout-item md-size-35"></div>
        <md-button class="md-raised md-primary md-layout-item" @click="authenticate('github')">Log in</md-button>
            <div class="md-layout-item md-size-35"></div>
      </div>

      <div class="loading-overlay" v-if="loading">
        <md-progress-spinner md-mode="indeterminate" :md-stroke="2"></md-progress-spinner>
      </div>

    </md-content>
    <div class="background" />
  </div>
</template>

<script>
import {vueAuth} from '../../main'
console.log(vueAuth)
export default {
  name: "App",
  data() {
    return {
      loading: false
    };
  },
  methods: {
    authenticate: function (provider) {
      vueAuth.authenticate(provider).then((response) => {
        const token = response.data.key
        this.$store.commit('setToken', token)
        console.log(token);
        sessionStorage.setItem('user-token', token)
        return this.$store.dispatch('getUser')
      }).then(() => {
        return this.$router.push({ name:'projects', params: { user:this.$store.state.auth.user.username}})
      }).catch((e) => {
        console.error(e)
      })
    }
  }
};
</script>

<style lang="scss">
.centered-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  height: 100vh;
  .title {
    text-align: center;
    margin-bottom: 30px;
  }
  .actions {
    .md-button {
      margin: 0;
    }
  }
  .form {
    margin-bottom: 60px;
  }
  .md-content {
    z-index: 1;
    padding: 40px;
    width: 100%;
    max-width: 400px;
    position: relative;
  }
  .loading-overlay {
    z-index: 10;
    top: 0;
    left: 0;
    right: 0;
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(255, 255, 255, 0.9);
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
