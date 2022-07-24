<template>
   <div class="registrarse-view">
    <h1 class="title">Registrarse</h1>
    <form class="form" action="/iniciarSesion">
      <label class="form-label" for="email">Ingrese un email:</label>
      <input class="form-input" type="email" id="email" placeholder="Email">
      <label class="form-label" for="password">Ingrese una contraseña</label>
      <input class="form-input" type="password" id="password" placeholder="contraseña">
      <input class="form-submit" type="submit" value="Registrarse" v-on:click='setAction'>
    </form>
  </div>
</template>

<script>

export default {
  name: 'RegistrarseView'
}
</script>

