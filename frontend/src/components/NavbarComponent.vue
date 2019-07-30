<template>
    <div class="page-container md-layout-row">
    <md-app>
      <md-app-toolbar class="md-dark">
        <md-button class="md-icon-button" @click="back">
          <octicon :icon="Octicons.chevronLeft" :scale="1.7"/>
        </md-button>
        <span class="md-title">{{ $route.meta.title }}</span>
      </md-app-toolbar>

      <md-app-drawer :md-active.sync="menuVisible" md-persistent="mini">
        <md-list class="md-toolbar-section-end">
          <md-list-item @click="goToProjects">
            <octicon :icon="Octicons.repo" :scale="1.5"/>
          </md-list-item>
          <md-list-item @click="goToSettings">
            <octicon :icon="Octicons.settings" :scale="1.5"/>
          </md-list-item>
          <md-list-item href="https://blackswan.readthedocs.io/en/latest/">
            <octicon :icon="Octicons.fileCode" :scale="1.5"/>
          </md-list-item>
          <md-list-item @click="logout">
            <octicon :icon="Octicons.signOut" :scale="1.5"/>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <router-view v-if="this.$store.getters.userLoaded"></router-view>
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
import { Octicons } from 'octicons-vue'
import axios from 'axios'
import {vueAuth} from '../main'

export default {
  name: 'PermanentMini',
  data: () => ({
    Octicons,
    menuVisible: false
  }),
  methods: {
    back() {
      this.$router.go(-1)
    },
    logout () {
      console.log('wtf')
      vueAuth.setToken({key: null})
      return this.$router.push({ name: 'login' })
    },
    goToProjects () {
      this.$router.push({ name:'projects', params: { user:this.$store.state.users.user.username }})
    },
    goToSettings () {
      this.$router.push({ name:'repositories' })
    },
    goToDocs () {
      this.$router.push({ name:'docs' })
    }
  }
}

</script>
