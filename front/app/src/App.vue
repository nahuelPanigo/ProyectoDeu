<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <NavBar/>
    <router-view></router-view>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <FooterLayout/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'
import FooterLayout from './components/FooterLayout.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    NavBar,
    FooterLayout
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
