<template>
  <div>
    <md-field class="md-layout md-gutter md-alignment-top-space-between">
      <label>Secret key</label>
      <md-input class="md-layout-item md-size-5" v-model="password" type="password"></md-input>
    </md-field>
  </div>
</template>
<script>
  export default {
    data: () => ({
      initial: 'Initial Value',
      password: 'mysecurepassword'
    })
  }
</script>

<style>
</style>
