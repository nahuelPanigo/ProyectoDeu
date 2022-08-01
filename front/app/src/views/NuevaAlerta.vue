<template>
<div id="nuevaAlerta">
  <a href="/listaAlertas">Mis Alertas</a> > <a class="paginaActual"> Nueva Alerta</a> 
  <div>
    <h1>Nueva Alerta</h1>
    <h2> Aqui puede configurar una nueva alerta </h2>
  </div>
<b-form >
    <div class="nombre">
      <label class="form-label" for="name">Nombre de la alerta:</label>
      <input class="form-input" id="name" required placeholder="Nombre">
    </div>
		<MapaNuevaAlerta 
    @changeLat="form.latitude = $event" 
    @changeLong="form.length = $event">
    </MapaNuevaAlerta>
    <!-- <button type="submit" name="Crear" class="guardar">Crear</button> -->
    <a href="#" class="form-submit" v-on:click='setAction'>Crear Alerta</a>
  </b-form>
  <a href="/listaAlertas" ><button class="volver"> Volver </button></a>
</div>
</template>

<script>
import MapaNuevaAlerta from '../components/MapaNuevaAlerta.vue'
import axios from "axios";
import {urlApi} from '../../public/utils/const.js'
import { getCookieValue } from '../../public/utils/helpers';

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
        latitude: '0',
        length: '0',
        zona: ""
      }
    }
  },
  methods:{
    setAction: function(){
      var latLong=this.form.latitude.toString()+","+this.form.length.toString()
      axios.get(urlApi+'/api/zonas/'+latLong).then((Response)=> {
          var zona=Response["data"]
          axios.post(urlApi+'/api/alertas/new',this.getjson(zona)).then((Response)=> {
          console.log(this.getjson())
          if(Response){
            this.$router.push({ name: 'listaAlertas' })
          }else{
            alert(Response["data"]["errores"]["errores"])
          }
          });
      })
    },getjson(zona){
      return {
        "name" : document.getElementById("name").value,
        "latitude" : this.form.latitude,
        "longitud" : this.form.length,
        "zona": zona,
        "user" :  getCookieValue("token")
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

  .guardar{
    background-color: var(--button-color);
    color: var(--primary-color)
  }
  
  .volver{
    background-color: var(--button-color);
    color: var(--primary-color)
  }
 
  .paginaActual {
    color: var(--primary-color);
    text-decoration:none;
    pointer-events: none;
  }

</style>