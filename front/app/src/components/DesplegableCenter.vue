<template>
<div id="DesplegableCenter" class="card" style="width: 18rem">
  <div class="card-body">
    <h5 center>{{center.name}}</h5>
  </div>
  <ul class="list-group list-group-flush">
    <li class="list-group-item"> <strong> Dirección: </strong> {{center.direction}} </li>
    <li class="list-group-item"> <strong> Horario: </strong> {{ center.startHour }} - {{center.closeHour}} </li>
    <li class="list-group-item"> <strong> Teléfono: </strong>  {{center.phone}} </li>
  </ul>
</div>
</template>

<script>
  export default {
	name: 'DesplegableCenter',
  props: {
    center: Object
  }
}
</script>

<style scoped>
  .leaflet-popup-content{
    margin:1px;
  }
</style>