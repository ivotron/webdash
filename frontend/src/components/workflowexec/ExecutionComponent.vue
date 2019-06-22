<template>
  <div>
    <md-card>
      <md-ripple>
        <md-card-header>
          <div class="md-title">{{ this.$route.params.project }}</div>
          <div class="md-subhead"># {{ execution.exec_number }}</div>
        </md-card-header>
        <md-card-content>
          <p>User: {{ this.$route.params.user }}</p>
          <p>Branch: {{ execution.branch }}</p>
          <p>Revision: {{ execution.revision }}</p>
          <p>Pull request: {{ execution.pr }}</p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
        </md-card-content>
      </md-ripple>
    </md-card>

    <md-tabs md-sync-route>
      <md-tab id="tab-log" md-label="Logs" :to="{name:'log',params:{user:this.$store.state.auth.user.email,project: this.$route.params.project,execution: this.$route.params.execution}}" exact></md-tab>
      <md-tab id="tab-graph" md-label="Workflow" :to="{name:'workflow',params:{user:this.$store.state.auth.user.email,project: this.$route.params.project,execution: this.$route.params.execution}}"></md-tab>
    </md-tabs>
    <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    execution: null
  }),
  created () {
    axios.get(
      `/api/executions/${this.$route.params.execution}`, {
        headers: { 'Authorization':`Token ${this.$store.state.auth.token}` }})
          .then(response => {
            this.execution = response.data
          })
  }
}
</script>

<style>
</style>
