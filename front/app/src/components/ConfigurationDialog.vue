<template>
<div>
<button 
  @click="change"> Dark mode </button>
</div>
</template>

<script>
export default{
  methods: {
    change() {
      return{
      styleObject: {
        fontSize: '10px',
        background: 'white'
      }
      }
    }
  }
};


</script>
