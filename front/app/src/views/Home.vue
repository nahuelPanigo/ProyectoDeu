    <template>
    <div class="homeView">
    <div class="jumbotron text-center">
      <h1>Alertas inundaciones</h1>
      <h3>Esta es una aplicacion informativa donde se puede visualizar centros de evacuaciones, zonas de riesgo de la ciudad y se podra configurar alertas para ser advertido en caso de posibles Inundaciones
        Poner mas info
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