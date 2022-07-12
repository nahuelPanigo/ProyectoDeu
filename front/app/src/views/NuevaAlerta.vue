<template>
<div id="nuevaAlerta">
  <div>
    <h1>Nueva Alerta</h1>
  </div>
<b-form @submit.prevent="onSubmit" id="form">
    <div class="nombre">
      <label class="form-label" for="name">Nombre de la alerta:</label>
      <input class="form-input" id="name" required placeholder="Nombre">
    </div>
    <b-form-input type="text" placeholder="Dirección"> </b-form-input>
						<MapaNuevaAlerta @changeLat="form.latitude = $event"
							@changeLong="form.length = $event"> 
						</MapaNuevaAlerta>
    <button type="submit" name="Crear">Crear</button>
  </b-form>
</div>
</template>

<script>
import MapaNuevaAlerta from '../components/MapaNuevaAlerta.vue'

  export default {
	name: 'nuevaAlerta',
  props: {
    center: Object
  },
  components:{
    MapaNuevaAlerta
  },
  data(){
		return{
			form:{
        name: '',
        latitude: 0,
        length: 0
      }
    }
  }
}

</script>

<style>
  .nombre{
    text-align: center;
    margin-top:2%;
  }

  .nombre label{
    margin:1%;
  }

</style>