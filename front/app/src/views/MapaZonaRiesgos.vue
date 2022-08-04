<template>
  <div class="Centros De Evacuacion">
    <h1>Mapa Zonas de riesgo</h1>
    <h2> En este mapa se visualizan las distintas zonas de la ciudad, distinguiendose los niveles de riesgo.</h2>
    <button  class="btn" data-toggle="modal" data-target="#myModalInfo"> 
     <i class="bi bi-gear-fill" id ="config-icon">Info Zonas</i>   
    </button>
    <InfoPopUp/>
    <RiskMap></RiskMap>
  </div>
</template>

<script>
import RiskMap from '../components/RiskMap.vue'
import InfoPopUp  from '../components/InfoModal.vue'

export default {
  name: 'RiskMapView',
  components: {
    RiskMap,
    InfoPopUp
  }
}
</script>