<template>
    <div class="page-container md-layout-row">
    <md-app>
      <md-app-toolbar class="md-primary">
        <md-button class="md-icon-button" @click="back">
          <md-icon>keyboard_arrow_left</md-icon>
        </md-button>
        <span class="md-title">{{ $route.meta.title }}</span>
      </md-app-toolbar>

      <md-app-drawer :md-active.sync="menuVisible" md-persistent="mini">
        <md-toolbar class="md-transparent" md-elevation="0">
          Blackswan
        </md-toolbar>

        <md-list class="md-toolbar-section-end">
          <md-list-item @click="goToProjects">
            <md-icon>view_list</md-icon>
          </md-list-item>
          <md-list-item @click="goToSettings">
            <md-icon>settings</md-icon>
          </md-list-item>
          <md-list-item @click="logOut">
            <md-icon>exit_to_app</md-icon>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <router-view></router-view>
      </md-app-content>

    </md-app>
  </div>
</template>

<style lang="scss" scoped>
  .md-toolbar + .md-toolbar {
    margin-top: 16px;
  }
  .md-app {
    min-height: 100vh;
    min-width: 1vh;
    border: 1px solid rgba(#000, 0);
  }
  .md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
  }
</style>

<script>
import axios from 'axios'

export default {
  name: 'PermanentMini',
  data: () => ({
    menuVisible: false
  }),
  methods: {
    back() {
      this.$router.go(-1)
    },
    logOut () {
      axios.post('/auth/logout/', {}, { headers: { 'Authorization':`Token ${this.$store.state.auth.token}` } })
        .then(response => {
          this.$router.push({ name: 'login' })
        })
    },
    goToProjects () {
      this.$router.push({ name:'projects', params: { user:this.$store.state.auth.user.email }})
    },
    goToSettings () {
      this.$router.push({ name:'profile', params: { user:this.$store.state.auth.user.email }})
    }
  }
}

</script>
