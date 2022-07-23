<template>
  <nav class="navbar navbar-inverse">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="/home">Inundaciones La Plata</a>
        </div>
        <ul class="nav navbar-nav">
          <li><a id="mapaEvacuacion" class="v-step-1" href="/mapaEvacuacion">Centros de evacuacion</a></li>
          <li><a id="mapaZonaRiesgo" class="v-step-2" href="/mapaZonasRiesgo">Zonas de riesgo</a></li>
          <li><a v-if="sesion === true" href="/listaAlertas" id="misAlertas"  class="v-step-4" onclick="misAlertas">Mis alertas</a></li>
          <li><a href="#" id="masInformacion" class="v-step-3" onclick="masInformacion">Mas informacion</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li><a id="iniciarSesion" v-if="sesion === false" href="/iniciarSesion" ><span class="glyphicon glyphicon-user"></span> Iniciar Sesion</a></li>
          <li><a id="registrarse" v-if="sesion === false" href="/registrarse" ><span class="glyphicon glyphicon-user"></span> Registrarse </a></li>
          <li><a id="cerrarSesion" v-if="sesion === true" href="#" v-on:click="delete_cookie('token')"><span class="glyphicon glyphicon-log-in"></span> Cerrar sesion</a></li>
        </ul>
      </div>
    </nav>
</template>

<script>

export default {
  name: 'app',
  data(){
    return {
      sesion:true,
      fontSize: "chico"
    }
  },created(){
    if(this.getCookie("token")){
      this.sesion=true
    }else{
      this.sesion=false
    }
  },methods: {
      getCookie(name){
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return true;
        return false;
      },
      delete_cookie(name) {
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
        window.location='/home'
      }
  }
}
</script>