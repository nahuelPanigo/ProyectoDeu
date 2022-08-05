<template>
    <div class="homeView">
    <div class=" text-center cuadro">
      <h1>Alertas inundaciones</h1>
      <h2>El sitio web trata de alertar a los ciudadanos, ante posibles inundaciones mediante alertas configurables de acuerdo a los puntos de interes. </h2> 
      <h3>Ademas brinda informacion de precipitaciones actuales, proximas y pasadas, como asi tambien mapas de informacion relevante.</h3>
      </div>  
      <h3 class="text-center"> Precipitaciones Acumuladas y Estimaciones </h3>
      <CuadroHome></CuadroHome> 
      </div>
</template>
<script>
import CuadroHome from '../components/CuadroHome'

export default {
  name: 'HomeView',
  components: {
      CuadroHome,
  }
}
</script>
<style>

  h2{
    padding-left: 1%;
    padding-right: 1%;
    padding-top: 1%;
  }
  h3{
    padding-left: 1%;
    padding-right: 1%;
    padding-top: 1%;
  }


</style>