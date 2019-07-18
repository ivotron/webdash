<template>
  <div>
    <template>
    <div v-for="project in projects">
      <div class="md-layout md-gutter md-alignment-center-left">
        <md-icon class="md-layout-item md-size-5">book</md-icon>
        <p class="md-layout-item md-size-25">{{ project.repo }}</p>
        <md-switch v-model="boolean" class="md-layout-item md-primary md-size-40">Enable</md-switch>
      </div>
      <md-divider></md-divider>
    </div>
    <div v-for="repo in repositories">
      <div class="md-layout md-gutter md-alignment-center-left">
        <md-icon class="md-layout-item md-size-5">book</md-icon>
        <p class="md-layout-item md-size-25">{{ repo.name }}</p>
        <div class="md-layout-item">
          <md-button class="md-dense md-raised md-primary" @click.native="createProject(repo)">Add project</md-button>
        </div>
      </div>
    </div>
  </template>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    repositories: [],
    projects: [],
    boolean: true
  }),
  created () {
    axios.get('/auth/github/repo/')
      .then(response => {
        this.repositories = response.data
      })
    axios.get('/api/projects/')
      .then(response => {
        this.projects = response.data
      })
  },
  methods: {
    createProject(repo){
      axios.post(`/api/projects/`, {
        organization:repo.owner.organizations_url,
        repo:repo.name,
        repo_url:repo.html_url,
        github_id:repo.id,
        private:repo.private
        })
    }
  }
}
</script>

<style>
</style>
