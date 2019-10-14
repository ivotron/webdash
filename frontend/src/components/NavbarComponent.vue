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
          <md-list class="md-toolbar-section-end">
            <md-list-item title="Read the Docs" href="https://blackswan.readthedocs.io/en/latest/" target="_blank">
              <md-icon>description</md-icon>
            </md-list-item>
            <template v-if="getKey()">
              <md-list-item title="Projects" @click="goToProjects">
                <md-icon>view_list</md-icon>
              </md-list-item>
              <md-list-item title="Settings" @click="goToSettings">
                <md-icon>settings</md-icon>
              </md-list-item>
              <md-list-item title="Logout" @click="logout">
                <md-icon>exit_to_app</md-icon>
              </md-list-item>
            </template>
            <template v-else>
              <md-list-item @click="goLogin">
                <md-icon>person</md-icon>
              </md-list-item>
            </template>
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
import {vueAuth} from '../main'

export default {
  name: 'PermanentMini',
  data: () => ({
    menuVisible: false
  }),
  methods: {
    back(){
      this.$router.go(-1)
    },
    logout(){
      vueAuth.storage.removeItem(vueAuth.tokenName)
      return this.$router.push({ name: 'login' })
    },
    goToProjects(){
      this.$router.push({ name:'projects', params: { user:this.$store.state.users.user.username }})
    },
    goToSettings(){
      this.$router.push({ name:'repositories' })
    },
    goLogin(){
      this.$router.push({ name:'login' })
    },
    getKey(){
      return vueAuth.getToken()
    }
  }
}

</script>
