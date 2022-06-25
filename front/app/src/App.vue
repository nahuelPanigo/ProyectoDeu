<template>
  <div id="app">
    <NavBar/>
    <router-view></router-view>
    <FooterLayout/>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import FooterLayout from './components/FooterLayout.vue'

export default {
  name: 'App',
  components: {
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
