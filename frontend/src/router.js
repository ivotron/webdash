import Vue from 'vue'
import VueRouter from 'vue-router'

import NavbarComponent from '@/components/NavbarComponent.vue'
import ProjectListComponent from '@/components/project/ProjectListComponent.vue'
import ExecutionListComponent from '@/components/workflowexec/ExecutionListComponent.vue'
import ExecutionComponent from '@/components/workflowexec/ExecutionComponent.vue'
import WorkflowComponent from '@/components/workflowexec/WorkflowComponent.vue'
import LogComponent from '@/components/workflowexec/LogComponent.vue'
import LoginComponent from '@/components/auth/LoginComponent.vue'
import GraphComponent from '@/components/tests/GraphComponent.vue'

import {
        MdToolbar,
        MdApp,
        MdButton,
        MdDrawer,
        MdList,
        MdIcon,
        MdContent,
        MdField,
        MdCard,
        MdRipple,
        MdProgress,
        MdEmptyState,
        MdTable
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
      },
      {
        path: ':user/:project/:execution',
        name: 'results',
        meta: { title: 'Results' },
        component: ExecutionComponent,
        children: [
          {
            path: ':user/:project/:execution',
            name: 'workflow',
            meta: { title: 'Workflow' },
            component: WorkflowComponent
          },
          {
            path: ':user/:project/:execution/log',
            name: 'log',
            meta: { title: 'Log' },
            component: LogComponent
          }
        ]
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: LoginComponent
  },
  {
    path: '/tests',
    name: 'tests',
    component: GraphComponent
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
