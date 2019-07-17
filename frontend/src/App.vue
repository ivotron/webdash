<template lang="html">
  <div>
    <router-view/>
  </div>
</template>

<script>
import {vueAuth} from './main'
export default {
  name: 'App',
  created() {
    this.$store.dispatch('getUser')
  }
}
</script>
