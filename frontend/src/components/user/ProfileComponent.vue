<template>
  <div>
    <h1>{{ this.$store.state.users.user.username }}</h1>
    <md-tabs md-sync-route>
      <md-tab id="tab-repos" md-label="Repositories" :to="{name:'repositories'}" exact>
        repositories
      </md-tab>
      <md-tab id="tab-settings" md-label="Settings" :to="{name:'settings'}">
      </md-tab>
    </md-tabs>
    <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    projects: []
  }),
  created () {
    axios.get(`/api/projects?username=${this.$route.params.user}`)
      .then(response => {
        this.projects = response.data
        this.searched = this.projects
      })
  }
}
</script>

<style>

</style>
