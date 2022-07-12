    <template>
    <div class="homeView">
    <div id="v-step-0" class=" text-center cuadro">
      <h1>Alertas inundaciones</h1>
      <h2>El sitio web trata de alertar a los ciudadanos, ante posibles inundaciones mediante alertas configurables de acuerdo a los puntos de interes. Ademas muestra informacion de precipitaciones actuales proximas, pasadas y mapas de informacion.
      </h2> 
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