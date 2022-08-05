<template>
    <div class="homeView">
      <h1>Mas Informacion Del Sitio</h1>
      <h2>Esta seccion ofrece bibliografia de la informacion utilizada en el sitio</h2> 
      <div id="documentos" style="text-align:left">
        <h3> Bibliografia utilizada para realizar los mapas de riesgos y alertas </h3>
        <ul style="list-style:none">
            <li><a href="https://www.memoria.fahce.unlp.edu.ar/trab_eventos/ev.11310/ev.11310.pdf" >análisis en perspectiva histórica de las inundaciones- Documento UNLP</a></li>       
            <li><a href="http://omlp.sedici.unlp.edu.ar/dataset/informe-final" >inundaciones en La Plata, Berisso y Ensenada. Análisis de riesgos - Documento Conicet-UNLP</a></li>
        </ul>
      </div>
      <div id="servicios" style="text-align:left">
        <h3> Servicios utilizados para obtener el clima </h3>
        <ul style="list-style:none">
            <li><a href="https://meteo.fcaglp.unlp.edu.ar/" >Estación Meteorológica Automática La Plata Observatorio</a></li>       
            <li><a href="https://weatherstack.com/quickstart" >servicio Api Wheatherstack </a></li>
        </ul>
      </div>
      <div id="otros trabajos" style="text-align:left">
        <h3> Otros trabajos de estudiantes acerca de las inundaciones de la ciudad de La Plata</h3>
        <ul style="list-style:none">
            <li><a href="https://app-inundaciones-deu.vercel.app/map" > Simulacion de inundaciones en la ciudad de La Plata</a></li>       
        </ul>
      </div>
    </div>  
</template>
<script>

export default {
  name: 'HomeView',
  components: {
  }
}
</script>
<style>
</style>