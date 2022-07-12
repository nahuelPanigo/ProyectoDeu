<template>
    <div id="app">
    <NavBar/>
    <v-tour name="App" :steps="steps" :options="myOptions"></v-tour>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar
  }, 
  data(){
    return{
       myOptions: {
          useKeyboardNavigation: true,
          labels: {
            buttonSkip: 'Saltear recorrido',
            buttonPrevious: 'Anterior',
            buttonNext: 'Siguiente',
            buttonStop: 'Terminar recorrido'
          }
        },
      steps: [
          {
            target: '#v-step-0',  
            header: {
              title: 'Guia Rapida para el uso de la pagina',
            },
            content: 'En esta seccion apareceran los datos de las lluvias proximas y milimetros acumulados'
          },
          {
            target: '.v-step-1',
            content: 'Aqui podras ver los centros de evacuacion existentes'
          },
          {
            target: '.v-step-2',
            content: 'En esta seccion se podra visualizar las zonas de riesgo en un mapa de la ciudad de la plata',
          },
          {
            target: '.v-step-3',
            content: 'Aqui se mostrara mas informacion del sitio web',
          }
          ]
    }
  },created(){
    if(this.getCookie("token")){
      var dict = {
            target: '.v-step-4',
            content: 'En esta seccion se podran administrar alertas en distintos puntos de interes para advertirte ante posibles inundaciones ',
          }
      this.steps.push(dict)
      console.log("token")
    }
  },mounted: function () {
      this.$tours['App'].start()
    },
    methods:{
        getCookie(name){
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return true;
        return false;
      },
    }
}



</script>

<style>
.app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url('../public/backend.png');
}
</style>
