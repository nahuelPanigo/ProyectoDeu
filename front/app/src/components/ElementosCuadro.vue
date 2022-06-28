<template>
        <div class="col-sm-4">
          <h3>{{titulo}}</h3>
          <h4>{{valor}}</h4>
        </div>
</template>

<script>

export default {
    name : "ElementoCuadro",
        props:{
            titulo: String,
            valor: String
        }
}
</script>