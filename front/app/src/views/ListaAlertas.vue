<template>
 <div class="alertas">
   <h1> Mis Alertas programadas </h1>
   <h2> En este mapa se visualizan todas las alertas configuradas por el usuario. </h2>
   <a href="/nuevaAlerta"  id="v-step-5"><button> Crear nueva Alerta </button> </a>
    <AlertsMap></AlertsMap>
    <v-tour name="alertas" :steps="steps" :options="myOptions"></v-tour>
  </div>
</template>

<script>
import AlertsMap from '../components/AlertsMap.vue'

export default {
  name: 'ListarAlertas',
  components: {
    AlertsMap
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
            target: '#v-step-5',  
            header: {
              title: 'Guia Rapida para el uso de la pagina',
            },
            content: 'Pulse aqui para configurar una alerta nueva'
          }
          ]
    }
  }
}
</script>