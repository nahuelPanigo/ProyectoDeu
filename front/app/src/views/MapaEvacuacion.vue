<template>
  <div class="Centros De Evacuacion">
    <h1>Mapa de Centros de evacuacion</h1>
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