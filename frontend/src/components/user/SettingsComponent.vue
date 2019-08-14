<template>
  <div class="md-layout md-gutter md-alignment-center-left">
    <md-field class="md-layout-item md-size-50" style="margin-left:10px;">
      <md-content class="md-layout-item">
        <label>Secret key</label>
        <md-input class="md-layout-item md-size-80" v-model="key" type="password" readonly></md-input>
      </md-content>
    </md-field>
    <md-button class="md-dense md-raised md-accent md-layout-item md-size-10" @click="resetKey">Reset</md-button>
    <div class="md-layout-item md-size-100">
      <h2>Themes</h2>
      <md-radio v-model="theme" value="dark-theme">Dark</md-radio>
      <md-radio v-model="theme" value="light-theme">Light</md-radio>
    </div>
  </div>
</template>
<script>
import {vueAuth} from '../../main'
import axios from 'axios'
  export default {
    data(){
      return {
        theme: this.$store.state.users.user.theme,
        key: this.getKey()
      }
    },
    methods: {
      resetKey() {
        return this.$store.dispatch('resetToken')
          .then(response => {
            this.$router.push({ name: 'login' })
          })
      },
      getKey() {
        return vueAuth.getToken()
      }
    },
    watch: {
      theme(newTheme, oldTheme) {
        axios.patch(`api/users/${this.$store.state.users.user.id}`, {theme:this.theme})
        this.$material.theming.theme = this.$store.state.users.user.theme
      }
    }
  }
</script>

<style>
</style>
