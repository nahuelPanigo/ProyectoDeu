<template>
    <div class="container">
      <div class="row">
       <ElementosCuadro titulo="un textoasd" valor="text"></ElementosCuadro>  
       <ElementosCuadro titulo="text" valor="text"></ElementosCuadro>  
    `</div>
     <div class="row">
       <ElementosCuadro titulo="text" valor="text"> </ElementosCuadro>  
       <ElementosCuadro titulo="text" valor="text"> </ElementosCuadro>  
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
    color: black;
}

</style>
