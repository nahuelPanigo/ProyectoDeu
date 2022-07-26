<template>
    <div id="app">
    <NavBar/>
    <button v-on:click='configurationPop' class="btn" data-toggle="modal" data-target="#myModal"> 
     <i class="bi bi-gear-fill" id ="config-icon">Configuracion</i>
    </button>
    <ConfiguracionPopUp/>
    <v-tour name="App" :steps="steps" :options="MyOptions"></v-tour>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import ConfiguracionPopUp from './components/Configuracion.vue'
import {getCookie,createCookie,getCookieValue,setVal,setFontSize} from '../public/utils/helpers.js'


export default {
  name: 'App',
  components: {
    NavBar,
    ConfiguracionPopUp
  },data(){
    return{
      openModal:false,
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
            content: 'Aqui podras ver los mapas con informacion de los centros de evacuacion existentes y de las zonas de riesgo'
          },
          {
            target: '.v-step-3',
            content: 'Aqui se mostrara mas informacion del sitio web',
          }
          ],
          MyOptions:{
          labels: {
              buttonSkip: 'Saltar',
              buttonPrevious: 'Atras',
              buttonNext: 'Siguiente',
              buttonStop: 'Finalizar'
          }
          }
    }
  },created(){
    if(getCookie("tema")==false){
      createCookie("tema","claro")
    }
    if(getCookie("token")){
      var dict = {
            target: '.v-step-4',
            content: 'En esta seccion se podran administrar alertas en distintos puntos de interes para advertir sobre posibles inundaciones ',
          }
      this.steps.push(dict)
    }
  },mounted: function () {
    this.$tours['App'].start()
    setVal(getCookieValue("tema"))
    setFontSize(getCookieValue("size"))
    },
    methods:{
      configurationPop:function(){
      }
    }
}



</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-size: 100vh;
}
h1{
  padding: 1%;
}
.btn{
  position: absolute;
  left: 20px;
  background: var(--back-color);
}
.btn i{
  margin: 4%;
  font-size:var(--font-size);
}
</style>
