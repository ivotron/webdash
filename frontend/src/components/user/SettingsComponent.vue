<template>
  <div class="md-layout">
    <md-field class="md-layout-item md-size-50 md-small-size-100">
      <label >Secret key</label>
      <md-input v-model="password" type="password"></md-input>
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
