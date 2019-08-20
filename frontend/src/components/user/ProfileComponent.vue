<template>
  <div>
    <h1>{{ this.$store.state.users.user.username }}</h1>
    <md-tabs class="md-transparent" md-sync-route>
      <md-tab id="tab-repos" md-label="Repositories" :to="{name:'repositories'}" exact>
      </md-tab>
      <md-tab id="tab-settings" md-label="Settings" :to="{name:'settings'}">
      </md-tab>
    </md-tabs>
    <router-view></router-view>
  </div>
</template>

<script>
export default {}
</script>

<style>

</style>
