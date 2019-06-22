<template>
  <md-content class="md-primary log-content">
    {{ execution.wf_str }}
  </md-content>
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
