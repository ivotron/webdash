<template>
  <div class="md-layout md-gutter md-alignment-center-left">
    <md-field class="md-layout-item md-size-50" style="margin-left:10px;">
      <md-content class="md-layout-item">
        <label>Secret key</label>
        <md-input class="md-layout-item md-size-80" v-model="$store.state.users.token" type="password" readonly></md-input>
      </md-content>
    </md-field>
    <md-button class="md-dense md-raised md-primary md-layout-item md-size-10" @click="resetKey">Reset</md-button>
  </div>
</template>
<script>
  export default {
    methods: {
      resetKey () {
        return this.$store.dispatch('resetToken')
          .then(response => {
            this.$router.push({ name: 'login' })
          })
      }
    }
  }
</script>

<style>
</style>
