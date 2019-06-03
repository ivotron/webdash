<template>
  <div>
    <md-card md-with-hover>
      <md-ripple>
        <md-card-header>
          <div class="md-title">Popper 2.0</div>
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
        <md-table-cell md-label="Name" md-sort-by="title">{{ item.title }}</md-table-cell>
        <md-table-cell md-label="Date of commit" md-sort-by="date">{{ item.date }}</md-table-cell>
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
const toLower = text => {
  return text.toString().toLowerCase()
}

export default {
  name: 'TableSearch',
  data: () => ({
    search: null,
    searched: [],
    projects: [
      {
        id: 1,
        title: "Add new action",
        date: "26/12/19"
      },
      {
        id: 2,
        title: "Fix previous action",
        date: "27/12/19"
      }
    ]
  }),
  created () {
    this.searched = this.projects
  }
}
</script>
