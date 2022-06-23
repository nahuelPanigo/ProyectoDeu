<template>
  <nav class="navbar navbar-inverse">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="#">Inundaciones La Plata</a>
        </div>
        <ul class="nav navbar-nav">
          <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">Mapas <span class="caret"></span></a>
          <ul class="dropdown-menu">
          <li class="active"><a href="#">Centros de evacuacion</a></li>
          <li class="active"><a href="#">Zonas de riesgo</a></li>
          </ul>
          <!-- <% if current.user  -->
          <li><a href="#">Mis alertas</a></li>
          <li><a href="#">Mas informacion</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <!-- <% if no inicio sesion -->
          <li><a href="#"><span class="glyphicon glyphicon-user"></span> Login</a></li>
          <li><a href="#"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
          <!-- else -->
          <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> Log out</a></li>
        </ul>
      </div>
    </nav>
</template>