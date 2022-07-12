<template>
  <div class="Centros De Evacuacion">
    <h1>Mapa Zonas de riesgo</h1>
    <p> En este mapa se visualizan las distintas zonas de la ciudad, distinguiendose los niveles de riesgo.</p>
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