<template>
        <div class="col-sm-4">
          <h3>{{titulo}}</h3>
          <h4>{{valor}}</h4>
        </div>
</template>

<script>
import ElementosCuadro from '../components/ElementosCuadro.vue'

export default {
    name : "Cuadro",
    components: { ElementosCuadro,
            },
        props:{
            titulo: String,
            valor: String
        }
}
</script>