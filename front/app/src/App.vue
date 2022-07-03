<template>
  <!-- <div id="app" :style="styleObject"> -->
    <div id="app" :class="mode">
    <NavBar :mode="mode"/>
    <ConfigurationDialog/>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import ConfigurationDialog from './components/ConfigurationDialog.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    ConfigurationDialog
  }, 
  data(){
    return{
      styleObject: {
        fontSize: '40px',
        background: 'black'
      },
      mode: 'light'
    }
  }
}
</script>

<style>
.app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100vw;
  min-height: 100vw;
  background: white;
}
.dark{
  background: #192734;
  color: white;
}
</style>
