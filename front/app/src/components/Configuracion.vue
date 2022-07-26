<template>
  <div class="modal fade" tabindex="-1" role="dialog" id="myModal">   
    <div class="modal-dialog" role="document">
    <div class="modal-content back">
    <h1>Configuraciones del sitio</h1>
    <h2>Elegir tema del sitio:</h2>
    <fieldset>
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
import {getCookie,createCookie,setProperty, changeSize} from '../../public/utils/helpers.js'
export default {
    name : "ConfiguracionPopUp",
    mounted(){
      this.setTema(getCookie("tema"));
    },
    methods :{
      changeConfig: function(){
          const radioOscuro=document.getElementById('inlineClaro');
          if(!radioOscuro.checked){
            createCookie("tema","oscuro")
            setProperty('rgb(0, 0, 24)','#95b3d1','#044d39','rgba(19, 35, 47, 0.9)')
          }else{
            createCookie("tema","claro")
            
            setProperty('#c3c3d6','#000000','#8a91b7','rgb(145 170 189 / 51%)')
          }
          const fontSize=document.getElementById('inlineFormCustomSelect')
          const sizeSelected=fontSize.options[fontSize.selectedIndex].value
          if(sizeSelected === 'medio'){
            createCookie("size", "mediano")
            changeSize('15px','30px','25px','20px', '18px', '1.5rem', '45px')
          } else {
            if (sizeSelected === 'chico'){
              createCookie("size", "chico")
              changeSize('12px', '25px', '20px', '15px', '12px', '1rem','30px')
            } else {
              createCookie("size", "grande")
              changeSize('20px', '40px', '35px', '30px', '25px', '2rem','65px')
            }
          }
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
    width: 100%;
    height: auto;
    display: flex;
    justify-content: space-around;
}
#botones button{
    width: 50%;
    flex-grow: 1;
    background: var(--button-color);
}
#inlineFormCustomSelect{
    padding: 1%;
    margin: 1%;
    background: var(--button-color);
}
label{
    margin: 1%;
}
legend{
    color: var(--primary-color);
}
.back{
  background: var(--back-color)
}
</style>
