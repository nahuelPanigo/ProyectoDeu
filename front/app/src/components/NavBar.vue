<template>
  <nav class="navbar navbar-inverse">
      <div class="container-fluid">
        <ul class="nav navbar-nav navbar-header">
          <li><a href="/home">Inundaciones La Plata</a></li>
          <li class="dropdown">
            <a class="dropdown-toggle v-step-1" data-toggle="dropdown"> Mapas <span class="caret"></span></a>
            <ul class="dropdown-menu">
            <li><a id="mapaEvacuacion" href="/mapaEvacuacion">Centros de evacuacion</a></li>
            <li><a id="mapaZonaRiesgo" href="/mapaZonasRiesgo">Zonas de riesgo</a></li>
            </ul>
            </li>
          <li><a v-if="sesion === true" href="/listaAlertas" id="misAlertas"  class="v-step-4" onclick="misAlertas">Mis alertas</a></li>
          <li><a href="/masInformacion" id="masInformacion" class="v-step-3" onclick="masInformacion">Mas informacion</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a id="iniciarSesion" v-if="sesion === false" href="/iniciarSesion"><span class="glyphicon glyphicon-user"></span> Iniciar Sesion</a></li>
          <li><a id="registrarse" v-if="sesion === false" href="/registrarse" ><span class="glyphicon glyphicon-user"></span> Registrarse </a></li>
          <li><a id="cerrarSesion" v-if="sesion === true" href="/home" v-on:click="delete_cookie('token')"><span class="glyphicon glyphicon-log-in"></span> Cerrar sesion</a></li>
        </ul>
      </div>
    </nav>
</template>

<script>
import {getCookie,deleteCookie} from '../../public/utils/helpers.js'



export default {
  name: 'app',
  data(){
    return {
      sesion:true,
      fontSize: "chico"
    }
  },mounted(){
    if(getCookie("token")){
      this.sesion=true
    }else{
      this.sesion=false
    }
  },methods: {
      delete_cookie(name) {
        deleteCookie(name);
      },
      theFunction: function(id){
        var element=document.getElementById(id);
        element.classList.add('ace');
      }
  }
}
</script>
<style>
  
</style>