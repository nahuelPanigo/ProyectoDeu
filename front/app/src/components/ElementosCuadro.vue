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
       font-size: var(--size-icon);
    }
    .borde-cuadro{
        border-style: groove;
        height: auto;
        background-color: var(--cuadros-color);
    }
</style>