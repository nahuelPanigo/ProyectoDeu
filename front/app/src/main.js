import Vue from 'vue'
import App from './App.vue'
import router from './router'
import 'leaflet/dist/leaflet.css'
import VueTour from 'vue-tour'

require('vue-tour/dist/vue-tour.css')

Vue.config.productionTip = false
Vue.use(VueTour)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
