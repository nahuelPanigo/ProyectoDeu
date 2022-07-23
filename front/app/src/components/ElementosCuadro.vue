<template>
        <div class="col-sm-6 borde-cuadro">
          <i class="pepito"></i>
          <h3>{{titulo}}</h3>
          <h4>{{valor}}</h4>
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
    i{
       font-size: 40px;
    }
    .borde-cuadro{
        border-style: groove;
        height: 150px;
        background-color: var(--cuadros-color);
    }
</style>