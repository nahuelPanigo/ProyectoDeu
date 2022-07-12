<template>
  <div class="Centros De Evacuacion">
    <h1>Mapa de Centros de evacuacion</h1>
    <h2> En este mapa se visualizan los centros a los que podras acudir en busca de ayuda o para realizar donaciones, ubicados en los distintos puntos de la ciudad. </h2>
    <AllCenterMap></AllCenterMap>
  </div>
</template>

<script>
import AllCenterMap from '../components/AllCenterMap.vue'
export default {
  name: 'MapaEvacuacion',
  components: {
    AllCenterMap
  }
}
</script>