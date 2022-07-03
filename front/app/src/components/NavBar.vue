<template>
  <nav class="navbar navbar-inverse">
    <h1> {{ mode }} MODE</h1>
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="/home">Inundaciones La Plata</a>
        </div>
        <ul class="nav navbar-nav">
          <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">Mapas <span class="caret"></span></a>
          <ul class="dropdown-menu">
          <li class="active"><a href="/mapaEvacuacion">Centros de evacuacion</a></li>
          <li class="active"><a href="#">Zonas de riesgo</a></li>
          </ul>
          <!-- <% if current.user  -->
          <li><a href="#">Mis alertas</a></li>
          <li><a href="#">Mas informacion</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <!-- <% if no inicio sesion -->
          <li><a v-if="sesion === false" href="/iniciarSesion"><span class="glyphicon glyphicon-user"></span> Login</a></li>
          <li><a v-if="sesion === false" href="#"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
          <!-- else -->
          <li><a v-if="sesion === true" href="#"><span class="glyphicon glyphicon-log-in"></span> Log out</a></li>
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
      }
  },
  props: ['mode']
}
</script>