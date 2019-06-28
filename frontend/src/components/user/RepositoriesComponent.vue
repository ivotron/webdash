<template>
  <div>
    <template v-for="project in projects">
      <div class="md-layout md-gutter md-alignment-top-center">
        <md-icon class="md-layout-item md-size-5">book</md-icon>
        <p class="md-layout-item md-size-95">{{ project.title }}</p>
      </div>
    </template>
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
      })
  }
}
</script>

<style>
</style>
