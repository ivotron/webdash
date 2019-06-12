import Vue from 'vue'
import VueRouter from 'vue-router'

import NavbarComponent from '@/components/NavbarComponent.vue'
import ProjectListComponent from '@/components/project/ProjectListComponent.vue'
import ExecutionListComponent from '@/components/workflowexec/ExecutionListComponent.vue'
import LoginComponent from '@/components/auth/LoginComponent.vue'

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
         MdRipple,
         MdProgress,
         MdEmptyState
       } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'


const routes = [
  {
    path: '/',
    component: NavbarComponent,
    children: [
      {
        path: ':user/projects',
        name: 'projects',
        meta: { title: 'Projects' },
        component: ProjectListComponent
      },
      {
        path: ':user/:project/executions',
        name: 'executions',
        meta: { title: 'Executions' },
        component: ExecutionListComponent
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: LoginComponent
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
Vue.use(MdProgress)
Vue.use(MdEmptyState)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

export default router
