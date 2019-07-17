<template>
  <div>
    <template v-for="project in projects">
      <div class="md-layout md-gutter md-alignment-top-center">
        <md-icon class="md-layout-item md-size-5">book</md-icon>
        <p class="md-layout-item md-size-15">{{ project.repo }}</p>
        <md-switch v-model="boolean" class="md-layout-item md-primary">Enable</md-switch>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    projects: [],
    boolean: true
  }),
  created () {
    axios.get('/api/projects', {}, { headers: { 'Authorization':`Token ${this.$store.state.users.token}` } })
      .then(response => {
        this.projects = response.data
      })
  }
}
</script>

<style>
</style>
