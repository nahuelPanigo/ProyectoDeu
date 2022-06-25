    <template>
    <div class="home">
    <div class="jumbotron text-center">
      <h1>Alertas inundaciones</h1>
      <p>Esta es una aplicacion informativa donde se puede visualizar centros de evacuaciones, zonas de riesgo de la ciudad y se podra configurar alertas para ser advertido en caso de posibles Inundaciones
        Poner mas info
      </p> 
      <Cuadro></Cuadro>
    </div>   

    </div>
</template>
<script>
import Cuadro from '../components/Cuadro'

export default {
  name: 'Home',
  components: {
      Cuadro
  }
}
</script>