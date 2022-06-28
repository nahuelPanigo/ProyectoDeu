<template>
  <div class="Centros De Evacuacion">
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