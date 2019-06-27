<template>
  <div class="centered-container">
    <md-content class="md-elevation-3">

      <div class="title">
        <div class="md-title">Blackswan</div>
        <div class="md-body-1">Sign in to Github to continue to Blackswan</div>
      </div>

      <div class="actions md-layout md-alignment-center-space-between">
        <md-button class="md-raised md-primary" href="https://github.com/login/oauth/authorize?client_id=cc102efd3cc9c51922cb&redirect_uri=http://127.0.0.1/auth/github/">Log in</md-button>
      </div>

      <div class="loading-overlay" v-if="loading">
        <md-progress-spinner md-mode="indeterminate" :md-stroke="2"></md-progress-spinner>
      </div>

    </md-content>
    <div class="background" />
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      loading: false,
      login: {
        email: "",
        password: ""
      }
    };
  },
  methods: {
    auth() {
      this.$store.dispatch('login', {email:this.login.email, password:this.login.password})
        .then(() => {
          console.log(this.$store)
          this.$router.push({ name:'projects', params: { user:this.$store.state.auth.user.email }})
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
