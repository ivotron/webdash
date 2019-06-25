<template>
  <div>
    <template v-for="project in projects">
      <div class="md-layout md-gutter md-align-center">
        <md-icon clas="md-layout-item md-size-100">book</md-icon>
        <p class="md-layout-item md-size-15">{{ project.title }}</p>
        <md-switch v-model="boolean" class="md-primary md-layout md-size-15">Primary</md-switch>
      </div>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    boolean: false,
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
