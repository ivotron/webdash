<template>
  <div>
    <md-card>
      <md-ripple>
        <md-card-header>
          <div class="md-title">{{ this.$route.params.project }}</div>
          <div class="md-subhead"># {{ this.$route.params.execution }}</div>
        </md-card-header>
        <md-card-content md-med>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
        </md-card-content>
      </md-ripple>
    </md-card>

    <md-tabs md-sync-route>
      <md-tab id="tab-graph" md-label="Workflow" to="{name:'workflow',params:{user:this.$store.state.auth.user.email,project:this.$store.state.auth.user.email,execution:id}}" exact></md-tab>
      <md-tab id="tab-log" md-label="Logs" to="{name:'log',params:{user:this.$store.state.auth.user.email,project:this.$store.state.auth.user.email,execution: id}}"></md-tab>
      <router-view></router-view>
    </md-tabs>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    execution: []
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
