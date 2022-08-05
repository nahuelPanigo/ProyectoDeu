<template>
<div id="DesplegableAlerta" class="card" style="width: 18rem">
  <div class="card-body">
    <h3>{{alert.name}}</h3>
    <h4>ZONA DE RIESGO:<br> {{alert.zone}}</h4>
    <a href="/mapaZonasRiesgo" class="masInfo"> <i class="bi bi-info-circle info"> Ver zona en el mapa de riesgos</i></a>
  </div>
  <ul class="list-group list-group-flush">
    <button class="second-icon eliminar" v-on:click='deleteAlerta'><i class="bi bi-trash3 second-icon"></i> Eliminar</button>
  </ul>
</div>
</template>

<script>
import axios from "axios";
import {urlApi} from '../../public/utils/const.js';

  export default {
	name: 'DesplegableAlerta',
  props: {
    alert: Object
  },
  methods:{
    deleteAlerta:function(){
      var idAlerta = this.alert.id
      axios.delete(urlApi+'/api/alertas/delete/'+idAlerta).then(()=> {
      })
      window.location.replace(document.URL)
    }
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
  .eliminar{
    width: 100%;
  }
  .info{
    font-size: 20px;
  }
  
</style>