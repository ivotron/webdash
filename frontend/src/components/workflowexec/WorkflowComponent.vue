<template>
  <md-content class="md-primary log-content" v-if="execution">
    {{ execution.wf_str }}
  </md-content>
</template>

<script>
import axios from 'axios'
export default {
    props:['execution']
}
</script>

<style>
</style>
