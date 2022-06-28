<template>
  <div class="Centros De Evacuacion">
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