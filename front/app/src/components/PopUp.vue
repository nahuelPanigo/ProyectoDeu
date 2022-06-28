<template>
  <div>
    <img @click="openModal" src="/logo.png" >
  </div>
</template>
<script>
import HelloApp from './HelloApp'

export default {
// ...
  methods: {
    openModal() {
      this.$FModal.show(
        { component: HelloApp },
        { msg: "En la pagina de inicio se mostrara un tablero con los datos actualizados de lluvias y proximas precipitaciones" ,
        title: "pagina de inicio",
        srcImg: "/backend.png"
        }
      )
    }
  }
}
</script>