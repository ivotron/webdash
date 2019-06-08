<template>
  <div>
    <md-card md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">{{ this.$route.params.project }}</div>
          <div class="md-subhead">By: CROSS</div>
        </md-card-header>

        <md-card-content md-med>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio itaque ea, nostrum odio. Dolores, sed accusantium quasi non.
        </md-card-content>
      </md-ripple>
    </md-card>
    <md-table md-height="600" v-model="searched" md-sort="name" md-sort-order="asc" md-card md-fixed-header>
      <md-table-toolbar>
        <div class="md-toolbar-section-start">
          <h1 class="md-title">Executions</h1>
        </div>
      </md-table-toolbar>

      <md-table-row slot="md-table-row" slot-scope="{ item }">
        <md-table-cell md-label="ID" md-sort-by="id" md-numeric>{{ item.id }}</md-table-cell>
        <md-table-cell md-label="Revision" md-sort-by="title">{{ item.revision }}</md-table-cell>
        <md-table-cell md-label="Branch" md-sort-by="date">{{ item.branch }}</md-table-cell>
      </md-table-row>
    </md-table>
  </div>
</template>

<style lang="scss" scoped>
  .md-card {
    width: 850px;
    margin: 4px;
    display: inline-block;
    vertical-align: top;
  }
</style>

<script>
import axios from 'axios'
const toLower = text => {
  return text.toString().toLowerCase()
}

export default {
  name: 'TableSearch',
  data: () => ({
    search: null,
    searched: [],
    executions: []
  }),
  created () {
    axios.get(`/api/executions?project=${this.$route.params.project}`, { headers: { 'Authorization':`Token ${this.$store.state.auth.token}` } })
      .then(response => {
        this.executions = response.data
        this.searched = this.executions
      })
  }
}
</script>
