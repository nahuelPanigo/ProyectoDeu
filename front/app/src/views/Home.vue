    <template>
    <div class="homeView">
    <div id="v-step-0" class="jumbotron text-center cuadro">
      <h1>Alertas inundaciones</h1>
      <h2>El sitio web trata de alertar a los ciudadanos, ante posibles inundaciones mediante alertas configurables de acuerdo a los puntos de interes. Ademas muestra informacion de precipitaciones actuales proximas, pasadas y mapas de informacion.
      </h2> 
      </div>  
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
  }
  .cuadro{
    background-color: rgb(118 150 150 / 55%);
    height: 50%;
 }

</style>