<template>
  <div>
    <h1>{{ this.$store.state.auth.user.username }}</h1>
    <md-tabs md-sync-route>
      <md-tab id="tab-repos" md-label="Repositories" :to="{name:'repositories',params:{user:this.$store.state.auth.user.email}}" exact>
        repositories
      </md-tab>
      <md-tab id="tab-settings" md-label="Settings" :to="{name:'settings',params:{user:this.$store.state.auth.user.email}}">
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
    axios.get('/api/projects', {}, { headers: { 'Authorization':`Token ${this.$store.state.auth.token}` } })
      .then(response => {
        this.projects = response.data
        this.searched = this.projects
      })
  }
}
</script>

<style>

</style>
