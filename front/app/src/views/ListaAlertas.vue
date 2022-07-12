<template>
 <div class="alertas">
   <h1> Mis Alertas programadas </h1>
   <a href="/nuevaAlerta"><button> Crear nueva Alerta </button> </a>
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
            target: '#v-step-0',  
            header: {
              title: 'Guia Rapida para el uso de la pagina',
            },
            content: 'En este mapa se visualizan sus alertas programadas'
          },
          {
            target: '#v-step-4',
            content: 'Seleccionando una ubicacion en el mapa, podra configurar una nueva alerta',
          }
          ]
    }
  }
}
</script>