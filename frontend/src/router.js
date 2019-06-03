import Vue from 'vue'
import VueRouter from 'vue-router'

import NavbarComponent from '@/components/NavbarComponent.vue'
import ProjectListComponent from '@/components/project/ProjectListComponent.vue'
import ExecutionListComponent from '@/components/workflowexec/ExecutionListComponent.vue'

import { MdToolbar,
         MdApp,
         MdButton,
         MdDrawer,
         MdList,
         MdIcon,
         MdContent,
         MdTable,
         MdField,
         MdCard,
         MdRipple} from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'

import 'vue-material/dist/theme/default-dark.css'


const routes = [
  {
    path: '/',
    component: NavbarComponent,
    children: [
      {
        path: 'projects',
        meta: { title: 'Projects' },
        component: ProjectListComponent
      },
      {
        path: 'projects/executions',
        meta: { title: 'executions' },
        component: ExecutionListComponent
      }
    ]
  }
]
Vue.use(VueRouter)
Vue.use(MdToolbar)
Vue.use(MdDrawer)
Vue.use(MdApp)
Vue.use(MdList)
Vue.use(MdContent)
Vue.use(MdTable)
Vue.use(MdField)
Vue.use(MdCard)
Vue.use(MdRipple)
Vue.use(MdButton)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

export default router
