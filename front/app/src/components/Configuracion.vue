<template>
  <div class="modal fade" tabindex="-1" role="dialog" id="myModal">   
    <div class="modal-dialog" role="document">
    <div class="modal-content back">
    <h1>Configuraciones del sitio</h1>
    <h2>Elegir tema del sitio:</h2>
    <fieldset>
    <legend>temas:</legend>
    <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineClaro" value="modo claro">
        <label class="form-check-label" for="inlineClaro">modo claro</label>
    </div>
    <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineOscuro" value="modo oscuro">
        <label class="form-check-label" for="inlineOscuro">modo oscuro</label>
    </div>
    </fieldset>
    <h2>Elegir tamaño de la letra del sitio:</h2>
      <div class="col-auto my-1">
      <label class="mr-sm-2 sr-only" for="inlineFormCustomSelect">tamaño de la letra</label>
      <select class="custom-select mr-sm-2" id="inlineFormCustomSelect">
        <option selected>Elegir tamaño...</option>
        <option value="chico">chico</option>
        <option value="medio">medio</option>
        <option value="grande">grande</option>
      </select>
      </div>
        <div id="botones">
            <button type="button" data-dismiss="modal">Cerrar</button>
            <button id="guardar" v-on:click='changeConfig' data-dismiss="modal" >Guardar Cambios </button>
        </div>
    </div>
    </div>
  </div>
</template>


<script>
export default {
    name : "ConfiguracionPopUp",
    mounted(){
      this.setTema(this.getCookie("tema"));
    },
    methods :{
      changeConfig: function(){
          const radioOscuro=document.getElementById('inlineClaro');
          if(radioOscuro.checked){
            this.createCookie("tema","oscuro")
            this.changeDark()
          }else{
            this.createCookie("tema","claro")
            this.changeLigth()
          }
      },
      getCookie(name){
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return true;
        return false;
      },createCookie(name,value) {
          var date = new Date();
          date.setTime(date.getTime()+(10*24*60*60*1000));
          var expires = "; expires="+date.toGMTString();
          document.cookie = name+"="+value+expires+"; path=/"; 
      },changeDark(){
        var declaration = document.styleSheets[16].cssRules[0].style;
        declaration.setProperty('--back-color', 'rgb(0, 0, 24)');
        declaration.setProperty('--primary-color', '#95b3d1');
      },changeLigth(){
        var declaration = document.styleSheets[16].cssRules[0].style;
        declaration.setProperty('--back-color', '#eee');
        declaration.setProperty('--primary-color', '#000000');
      },
      setTema(tema){
        var radio="";
        switch (tema){
          case "oscuro":
            radio=document.getElementById('inlineOscuro');
            break;
          default: 
            radio=document.getElementById('inlineClaro');
            break;
        }
        radio.checked=true;
      }
    }
}
</script>

<style >

#botones{
    width: 98%;
    margin-top: 1%;
    margin-block-end: 2%;
    margin-left: 1%;
    margin-right: 1%;
}
#botones button{
    width: 50%;
    background: #044d39;
}
#inlineFormCustomSelect{
    padding: 1%;
    margin: 1%;
    background: #044d39;
}

label{
    margin: 1%;
}
legend{
    color: aliceblue;
}
.back{
  background: var(--back-color)
}
</style>
