<template>
  <div>
    <template>
    <h3>Blackswan</h3>
    <md-button class="md-dense md-raised md-primary md-accent" @click.native="updateRepositories()"><md-icon>cached</md-icon> Sync</md-button>
    <p>In addition to enabling your repository below, you need to properly configure the CI builds. <a class="md-accent"href="">Read here for more.</a></p>
    <div v-for="project in projects">
      <div class="md-layout md-gutter md-alignment-center-left">
        <md-icon class="md-layout-item md-size-5">book</md-icon>
        <p class="md-layout-item md-size-25">{{ project.repo }}</p>
        <md-switch v-model="project.enabled" class="md-layout-item md-accent" v-on:change="updateProject(project)"></md-switch>
      </div>
    </div>
    <md-divider></md-divider>
    <h3>GitHub available</h3>
    <div v-for="repo in repositories">
      <div class="md-layout md-gutter md-alignment-center-left">
        <md-icon class="md-layout-item md-size-5">book</md-icon>
        <p class="md-layout-item md-size-25">{{ repo.name }}</p>
        <md-switch v-model="repo.enabled" class="md-layout-item md-accent" v-on:change="createProject(repo)"></md-switch>
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
    array: []
  }),
  created () {
    axios.get('/auth/github/repo/')
      .then(response => {
        this.repositories = response.data
        for(repo in this.repositories){
          repo.enabled = false
        }
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
        }).then(response => {
          this.projects.push(response.data)
          var i = this.repositories.indexOf(repo);
          if (i > -1) {
            this.repositories.splice(i, 1);
          }
        })
    },
    updateProject(repo){
      axios.patch(`/api/projects/${repo.id}`, {enabled:repo.enabled})
    },
    updateRepositories(repo){
      axios.get('/auth/github/repo/sync/')
        .then(response => {
          this.projects = this.projects.concat(response.data)
        })
    }
  }
}
</script>

<style>
</style>
