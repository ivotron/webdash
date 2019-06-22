<template>
  <md-content class="md-primary log-content">
    {{ execution.log }}
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
  .log-content {
    margin-top: 20px;
    margin-left: 15px;
    background: #000;
    background-color: #000;
  }

</style>
