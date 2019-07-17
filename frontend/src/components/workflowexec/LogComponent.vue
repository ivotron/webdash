<template>
  <md-content class="md-primary log-content" v-if="execution">
    {{ execution.log }}
  </md-content>
</template>

<script>
import axios from 'axios'
export default {
  props:['execution']
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
