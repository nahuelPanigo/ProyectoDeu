<template>
  <nav class="navbar navbar-inverse">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="/home">Inundaciones La Plata</a>
        </div>
        <ul class="nav navbar-nav">
          <li><a id="mapaEvacuacion" href="/mapaEvacuacion" onclick="theFunction(mapaEvacuacion)">Centros de evacuacion</a></li>
          <li><a id="mapaZonaRiesgo" href="/mapaZonasRiesgo" onclick="theFunction(mapaZonaRiesgo)">Zonas de riesgo</a></li>
          <!-- <% if current.user  -->
          <li><a href="#" id="misAlertas"  onclick="misAlertas">Mis alertas</a></li>
          <li><a href="#" id="masInformacion" onclick="masInformacion">Mas informacion</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <!-- <% if no inicio sesion -->
          <li><a id="iniciarSesion" v-if="sesion === false" href="/iniciarSesion" onclick="theFunction(iniciarSesion)"><span class="glyphicon glyphicon-user"></span> Login</a></li>
          <li><a id="registrarse" v-if="sesion === false" href="#" onclick="theFunction(registrarse)"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
          <!-- else -->
          <li><a id="cerrarSesion" v-if="sesion === true" href="#" onclick="theFunction(cerrarSesion)"><span class="glyphicon glyphicon-log-in"></span> Log out</a></li>
        </ul>
      </div>
    </nav>
</template>

<script>

export default {
  name: 'app',
  data(){
    return {
      sesion:true
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
      theFunction: function(id){
        var element=document.getElementById(id);
        element.classList.add('ace');
      }
  }
}
</script>