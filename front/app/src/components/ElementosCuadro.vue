<template>
        <div class="col-sm-6">
          <i class="pepito"></i>
          <h4>{{titulo}}</h4>
          <h5>{{valor}}</h5>
        </div>
</template>

<script>

export default {
    name : "ElementoCuadro",
        props:{
            titulo: String,
            valor: String,
            clase: String
        },mounted(){
            var element =document.getElementsByClassName("pepito")[0];
            element.className=this.clase;
      }
}
</script>
<style>

</style>