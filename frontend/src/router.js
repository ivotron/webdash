import Vue from 'vue'
import VueRouter from 'vue-router'

import NavbarComponent from '@/components/NavbarComponent.vue'
import DocsComponent from '@/components/DocsComponent.vue'
import ProjectListComponent from '@/components/project/ProjectListComponent.vue'
import ExecutionListComponent from '@/components/workflowexec/ExecutionListComponent.vue'
import ExecutionComponent from '@/components/workflowexec/ExecutionComponent.vue'
import WorkflowComponent from '@/components/workflowexec/WorkflowComponent.vue'
import LogComponent from '@/components/workflowexec/LogComponent.vue'
import LoginComponent from '@/components/user/LoginComponent.vue'
import ProfileComponent from '@/components/user/ProfileComponent.vue'
import SettingsComponent from '@/components/user/SettingsComponent.vue'
import RepositoriesComponent from '@/components/user/RepositoriesComponent.vue'
import TestLoginComponent from '@/components/user/TestLoginComponent.vue'

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
        MdTable,
        MdTabs,
        MdSwitch,
        MdDivider
       } from 'vue-material/dist/components'
import 'vue-material/dist/vue-material.min.css'
import './default-theme.scss'


const routes = [
  {
    path: '/',
    component: NavbarComponent,
    children: [
      {
        path: '/profile',
        name: 'profile',
        meta: { title: 'Profile' },
        component: ProfileComponent,
        children: [
          {
            path: 'repositories',
            name: 'repositories',
            meta: { title: 'Profile' },
            component: RepositoriesComponent
          },
          {
            path: '/profile/settings',
            name: 'settings',
            meta: { title: 'Profile' },
            component: SettingsComponent
          }
        ]
      },
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
        path: '',
        name: 'results',
        meta: { title: 'Results' },
        component: ExecutionComponent,
        children: [
          {
            path: ':user/:project/:execution/log',
            name: 'log',
            meta: { title: 'Log' },
            component: LogComponent
          },
          {
            path: 'workflow',
            name: 'workflow',
            meta: { title: 'Workflow' },
            component: WorkflowComponent
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
    path: '/test',
    name: 'test',
    component: TestLoginComponent
  },
  {
    path: '/Documentation',
    name: 'docs',
    component: DocsComponent
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
Vue.use(MdTabs)
Vue.use(MdSwitch)
Vue.use(MdDivider)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return { x: 0, y: 0 } },
  mode: 'history',
  routes
})

export default router
