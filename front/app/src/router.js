import Vue from 'vue'
import Router from 'vue-router'
import LoginView from './views/Login.vue'
import HomeView from './views/Home.vue'
import MapaEvacuacion from './views/MapaEvacuacion.vue'
import RiskMapView from './views/MapaZonaRiesgos.vue'


Vue.use(Router)
const routes = [
  { path: '/iniciarSesion', name: 'login', component: LoginView }, 
  { path: '/home', name: 'home', component: HomeView }, 
  { path: '/mapaEvacuacion', name: 'mapaEvacuacion', component: MapaEvacuacion },
  { path: '/mapaZonasRiesgo', name: 'riskMapView', component: RiskMapView }  
]

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router