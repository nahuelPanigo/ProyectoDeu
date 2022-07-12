<template>
    <div class="container">
      <div class="row">
          
       <ElementosCuadro titulo="milimetros diarios acumulados" valor="5 mm" clase="bi bi-moisture"></ElementosCuadro>  
       <ElementosCuadro titulo="milimetros semanales acumulados" valor="14 mm" clase="bi bi-moisture"></ElementosCuadro>  
    </div>
     <div class="row">
       <ElementosCuadro titulo="probabilidad de lluvias" valor="40 %" clase="bi bi-cloud-rain"> </ElementosCuadro>  
       <ElementosCuadro titulo="estimacion de precipitaciones" valor="2 mm" clase="bi bi-droplet-half"> </ElementosCuadro>  
    `</div>
    </div>
    
</template>

<script>
import ElementosCuadro from './ElementosCuadro.vue'

export default {
    name : "CuadroHome",
    components: { ElementosCuadro,
            }
}
</script>
<style>
.container{
    width: 90%;
    height: 50%;
    color: rgb(255, 255, 255);
}

</style>
