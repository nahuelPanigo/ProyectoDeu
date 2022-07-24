<template>
  <div class="login-view">
    <h1 class="title">Iniciar Sesion</h1>
    <form class="form" action="/home">
      <label class="form-label" for="email">Email:</label>
      <input class="form-input" type="email" id="email" placeholder="Email">
      <label class="form-label" for="password">Contraseña:</label>
      <input class="form-input" type="password" id="password" placeholder="contraseña">
      <input class="form-submit" type="submit" value="Ingresar" v-on:click='setAction'>
    </form>
  </div>
</template>

<script>

export default {
  name: 'LoginView',
  methods: {
    setAction: function(){
      document.cookie = "token=asdasfsafg3RDFMi12m3eoimlk";
    }
  }

}
</script>

<style >
.login-view{
  padding: 2rem;
  size: 100vh;
}
.title {
  text-align: center;
}
.form { 
  margin: 3rem auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  width: 35%;
  min-width: 350px;
  max-width: 100%;
  background-color: var(--cuadros-color);
  border-radius: 5px;
  padding: 40px;
  box-shadow: 0 4px 10px 4px rgba(0, 0, 0, 0.3);
}
.form-label {
  margin-top: 2rem;
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}
.form-input {
  padding: 10px 15px;
  background: none;
  background-image: none;
  border: 1px solid white;
  color: var(--primary-color);
}
.form-submit {
  background: var(--button-color);
  border: none;
  color: var(--primary-color);
  margin-top: 3rem;
  padding: 1rem 0;
  cursor: pointer;
}
</style>