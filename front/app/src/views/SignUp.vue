<template>
   <div class="registrarse-view">
    <h1 class="title">Registrarse</h1>
    <form class="form" action="/iniciarSesion">
      <label class="form-label" for="email">Ingrese un email:</label>
      <input class="form-input" type="email" id="email" placeholder="Email">
      <label class="form-label" for="password">Ingrese una contraseña</label>
      <input class="form-input" type="password" id="password" placeholder="contraseña">
      <label class="form-label" for="repeatPassword">Repita la contraseña</label>
      <input class="form-input" type="password" id="repeatPassword" placeholder="contraseña">
      <a href="#" class="form-submit" v-on:click='setAction'>Registrarse</a>
      <!-- <input class="form-submit" type="submit" value="Registrarse" v-on:click='setAction'> -->
    </form>
  </div>
</template>

<script>

import axios from "axios";
import {urlApi} from '../../public/utils/const.js'

export default {
  name: 'RegistrarseView',
  methods: {
    setAction: function(){
      axios.post(urlApi+'/api/user/registrarse',this.getjson()).then((Response)=> {
        console.log(Response)
      if(Response["data"]["user"] != null){
        this.$router.push({ name: 'login' })
      }else{
        console.log(Response)
        alert(Response["data"]["errores"]["errores"])
      }
      });
    },getjson(){
      return {
        "password" : document.getElementById("password").value,
        "email" : document.getElementById("email").value,
        "repeatPassword" : document.getElementById("repeatPassword").value
      }
    }
  }
}
</script>

