<template>
<div id="DesplegableAlerta" class="card" style="width: 18rem">
  <div class="card-body">
    <h5 center>{{center.name}}</h5>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item"> <strong> Dirección: </strong> {{center.direccion}} </li>
    <li class="list-group-item"><button>Eliminar</button></li>
  </ul>
</div>
</template>

<script>
  export default {
	name: 'DesplegableAlerta',
  props: {
    center: Object
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
</style>