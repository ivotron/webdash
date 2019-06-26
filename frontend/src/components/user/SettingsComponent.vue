<template>
  <div>
    <md-field>
      <label></label>
      <md-input v-model="password" type="password"></md-input>
    </md-field>

<script>
  export default {
    data: () => ({
      initial: 'Initial Value',
      password: 'mysecurepassword'
    })
  }
</script>

<style lang="scss" scoped>
  .md-field:last-child {
    margin-bottom: 40px;
  }
</style>
