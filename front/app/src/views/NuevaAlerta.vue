<template>
<div id="nuevaAlerta">
  <a href="/listaAlertas">Mis Alertas</a> > <a class="paginaActual"> Nueva Alerta</a> 
  <div>
    <h1>Nueva Alerta</h1>
    <h3> Aqui puede configurar una nueva alerta. </h3>
    <h4> Se le enviara un mail en el caso de que se acumule mucha agua en la zona, advirtiendo ante posibles inundaciones </h4>
  </div>
<b-form >
    <div class="nombre">
      <label class="form-label" for="name">Ingrese el nombre de la alerta:</label>
      <input class="form-input" id="name" required placeholder="Nombre">
    </div>
    <div style="text-align: left;">
    <label for="mapa"> Seleccione la ubicacion de la alerta en el mapa:</label>
    </div>
		<MapaNuevaAlerta 
    @changeLat="form.latitude = $event" 
    @changeLong="form.length = $event">
    </MapaNuevaAlerta>
    <!-- <button type="submit" name="Crear" class="guardar">Crear</button> -->
    <button style="margin: 0.5%;" class="volver" v-on:click='setAction'>Crear Alerta</button>
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