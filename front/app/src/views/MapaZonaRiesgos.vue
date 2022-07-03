<template>
  <div class="Centros De Evacuacion">
    <h1>Mapa de Centros de evacuacion</h1>
    <RiskMap></RiskMap>
  </div>
</template>

<script>
import RiskMap from '../components/RiskMap.vue'

export default {
  name: 'RiskMapView',
  components: {
    RiskMap
  }
}
</script>