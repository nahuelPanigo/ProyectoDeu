<template>
<div id="DesplegableAlerta" class="card" style="width: 18rem">
  <div class="card-body">
    <h4>{{alert.name}}</h4>
  </div>
  <ul class="list-group list-group-flush">
    <button class="second-icon"><i class="bi bi-trash3 second-icon"></i> Eliminar</button>
  </ul>
</div>
</template>

<script>
  export default {
	name: 'DesplegableAlerta',
  props: {
    alert: Object
  }
}

</script>

<style scoped>
  .leaflet-popup-content{
    margin:1px;
  }
  .card-body{
    text-align: center;
  }
  .second-icon{
    font-size: var(--font-size)
  }
</style>