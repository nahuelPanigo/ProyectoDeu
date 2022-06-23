import Vue from 'vue'
import Router from 'vue-router'
import Login from './views/Login.vue'

Vue.use(Router)
const routes = [
  { path: '/', name: 'login', component: Login }, 
  { path: '/', name: 'login', component: Login }, 
  { path: '/', name: 'login', component: Login } 
]

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router