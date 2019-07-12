<template>
  <div class="md-layout">
    <md-field class="md-layout-item md-size-50 md-small-size-100">
      <label>Secret key</label>
      <md-input v-model="$store.state.users.token" type="password" disabled></md-input>
    </md-field>
  </div>
</template>
<script>
  export default {
  }
</script>

<style>
</style>
