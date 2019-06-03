<template>
    <div class="page-container md-layout-row">
    <md-app>
      <md-app-toolbar class="md-primary">
        <md-button class="md-icon-button">
          <md-icon>keyboard_arrow_left</md-icon>
        </md-button>
        <span class="md-title">{{ $route.meta.title }}</span>
      </md-app-toolbar>

      <md-app-drawer md-permanent="full">
        <md-toolbar class="md-transparent" md-elevation="0">
          Blackswan
        </md-toolbar>

        <md-list>
          <md-list-item to="/projects">
            <md-icon>move_to_inbox</md-icon>
            <span class="md-list-item-text">Projects</span>
          </md-list-item>
        </md-list>
      </md-app-drawer>

      <md-app-content>
        <router-view></router-view>
      </md-app-content>

    </md-app>
  </div>
</template>

<style lang="scss" scoped>
  .md-toolbar + .md-toolbar {
    margin-top: 16px;
  }
  .md-app {
    min-height: 100vh;
    border: 1px solid rgba(#000, .12);
  }
  .md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
  }

</style>

<script>
  export default {
    name: 'PermanentFull'
  }

</script>
