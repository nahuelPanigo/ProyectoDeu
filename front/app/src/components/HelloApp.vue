<template>
  <div class="hello">
    <h1>{{ title }}</h1>
    <p>
      {{msg}}
    </p>
    <img id="imagen_tutorial" />
  <button></button>
  </div>
</template>

<script>
export default {
  name: 'HelloApp',
  props: {
    title: String,
    msg: String,
    srcImg: String,
  },Mounted(){
      var image=document.getElementById("imagen_tutorial");
      image.setAttribute('src', this.srcImg);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1{
  text-align: center;
}
p{
  padding: 1%;
}
</style>
