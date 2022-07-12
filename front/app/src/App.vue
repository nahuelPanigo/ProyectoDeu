<template>
    <div id="app">
    <NavBar/>
    <button v-on:click='configurationPop' class="btn" data-toggle="modal" data-target="#myModal"> 
     <i class="bi bi-gear-fill" id ="config-icon"></i>Configuracion
    </button>
    <ConfiguracionPopUp/>
    <v-tour name="App" :steps="steps" :options="MyOptions"></v-tour>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import ConfiguracionPopUp from './components/Configuracion.vue'

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
      configurationPop:function(){
      }
    }
}



</script>

<style>
body{
  background: rgb(0, 0, 24);
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #95b3d1;
  background-size: 100vh;
}
h1{
  padding: 1%;
}
button{
  font-size:20px;
}
.btn{
  position: absolute;
  top: 10%;
  left: 20px;
  background: rgb(0, 0, 24);
  font-size: x-large;
}
.btn i{
  margin: 4%;
}
</style>
