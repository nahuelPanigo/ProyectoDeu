    <template>
    <div class="homeView">
    <div class="jumbotron text-center">
      <h1>Alertas inundaciones</h1>
      <h3>El sitio web trata de alertar a los ciudadanos, ante posibles inundaciones mediante alertas configurables de acuerdo a los puntos de interes. Ademas muestra informacion de precipitaciones actuales proximas, pasadas y mapas de informacion.
      </h3> 
      </div>  
      <CuadroHome></CuadroHome> 
    </div>
</template>
<script>
import CuadroHome from '../components/CuadroHome'

export default {
  name: 'HomeView',
  components: {
      CuadroHome
  }
}
</script>
<style>
  h3{
    padding: 2%;
  }

</style>