<template>
  <div>
    <div v-if="projects">
      <md-card>
        <md-table md-height="600" v-model="searched" md-sort="name" md-sort-order="asc" md-fixed-header>
          <md-table-toolbar>

            <md-field md-clearable class="md-toolbar-section-end">
              <md-input placeholder="Search by name..." v-model="search" @input="searchOnTable" />
            </md-field>
          </md-table-toolbar>

          <md-table-empty-state
            md-label="No Projects found"
            :md-description="`No project found with this '${search}'.`">
          </md-table-empty-state>

          <md-table-row slot="md-table-row" slot-scope="{ item }" @click.native="openExecutions(item.repo)">
            <md-table-cell md-label="Name" md-sort-by="name">{{ item.repo }}</md-table-cell>
            <template v-if='item.last_execution'>
              <md-table-cell md-label="#" md-sort-by="title">{{ item.last_execution.exec_number }}</md-table-cell>
              <md-table-cell md-label="Last commit" md-sort-by="title">{{ item.last_execution.revision }}</md-table-cell>
              <md-table-cell md-label="Commit date" md-sort-by="title">{{ item.last_execution.exec_date }}</md-table-cell>
              <md-table-cell md-label="State" md-sort-by="state">
                <template v-if="item.last_execution.state === 'running'">
                  <md-icon>check</md-icon>
                </template>
                <template v-else>
                  <md-icon>cancel</md-icon>
                </template>
              </md-table-cell>
            </template>
            <template v-else>
              <md-table-cell md-label="#" md-sort-by="title">N/A</md-table-cell>
              <md-table-cell md-label="Last commit" md-sort-by="title">N/A</md-table-cell>
              <md-table-cell md-label="Commit date" md-sort-by="title">N/A</md-table-cell>
              <md-table-cell md-label="State" md-sort-by="state"><md-icon>cancel</md-icon></md-table-cell>
            </template>
          </md-table-row>
        </md-table>
      </md-card>
    </div>
      <div v-else>
        <md-empty-state
          md-rounded
          md-icon="access_time"
          md-label="Loading projects">
        </md-empty-state>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

  const toLower = text => {
    return text.toString().toLowerCase()
  }

  const searchByName = (items, term) => {
    if (term) {
      return items.filter(item => toLower(item.name).includes(toLower(term)))
    }

    return items
  }

  export default {
    name: 'TableSearch',
    data: () => ({
      search: null,
      searched: [],
      projects: []
    }),
    methods: {
      searchOnTable () {
        this.searched = searchByName(this.projects, this.search)
      },
      openExecutions (name) {
        this.$router.push({ name: 'executions', params: { user:this.$store.state.users.user.username, project: name }})
      }
    },
    created () {
      axios.get(`/api/users?username=${this.$route.params.user}`)
        .then(response => {
          if(response.data.length){
            axios.get(`/api/projects?username=${this.$route.params.user}`)
              .then(response => {
                this.projects = response.data
                this.searched = this.projects
              })
          }else{
            this.$router.push({ name:'404' })
          }
        })
    }
  }
</script>

<style lang="scss" scoped>
  .md-field {
    max-width: 300px;
  }
  .md-icon {
    height: 30px;
  }

</style>
