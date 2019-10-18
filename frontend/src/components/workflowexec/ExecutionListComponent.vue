<template>
  <div>
    <div v-if="executions">
      <md-card md-with-hover>
        <md-ripple>
          <md-card-header>
            <div class="md-title">{{ this.$route.params.project }}</div>
            <div class="md-subhead">By: {{ this.$route.params.org }}</div>
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

        <md-table-row slot="md-table-row" slot-scope="{ item }" @click.native="openResults(item.id)">
          <md-table-cell md-label="Commit" md-sort-by="id" md-numeric>{{ item.id }}</md-table-cell>
          <md-table-cell md-label="Pull request" md-sort-by="title">{{ item.revision }}</md-table-cell>
          <md-table-cell md-label="Branch" md-sort-by="branch">{{ item.branch }}</md-table-cell>
          <md-table-cell md-label="Execution #" md-sort-by="branch">{{ item.exec_number }}</md-table-cell>
          <md-table-cell md-label="Execution date" md-sort-by="branch">{{ item.exec_date }}</md-table-cell>
          <md-table-cell md-label="State" md-sort-by="state">{{ item.state }}</md-table-cell>
        </md-table-row>
      </md-table>
    </div>
    <div v-else>
      <md-empty-state
        md-rounded
        md-icon="access_time"
        md-label="Loading executions">
      </md-empty-state>
    </div>
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
  methods: {
    openResults (id) {
      this.$router.push({
        name: 'log',
        params: {
          user:this.$store.state.users.user.username,
          project: this.$route.params.project,
          execution: id
         }
       })
    }
  },
  created () {
    axios.get(`/api/users?username=${this.$route.params.org}`)
      .then(response => {
        if(response.data.length){
          axios.get(`/api/executions?project=${this.$route.params.project}`)
            .then(response => {
              this.executions = response.data
              this.searched = this.executions
          })
        }else{
          this.$router.push({ name:'404' })
        }
      })
  }
}
</script>
