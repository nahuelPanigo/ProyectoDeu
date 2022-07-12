<template>
  <div class="modal fade" tabindex="-1" role="dialog" id="myModal">   
    <div class="modal-dialog" role="document">
    <div class="modal-content back">
    <h1>Configuraciones del sitio</h1>
    <h2>Elegir tema del sitio:</h2>
    <fieldset>
    <legend>temas:</legend>
    <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio1" value="modo claro">
        <label class="form-check-label" for="inlineRadio1">modo claro</label>
    </div>
    <div class="form-check form-check-inline">
        <input class="form-check-input" type="radio" name="inlineRadioOptions" id="inlineRadio2" value="modo oscuro">
        <label class="form-check-label" for="inlineRadio2">modo oscuro</label>
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
            <button id="guardar">Guardar Cambios</button>
        </div>
    </div>
    </div>
  </div>
</template>


<script>
export default {
    name : "ConfiguracionPopUp"
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
  background: rgb(0, 0, 24);;
}
</style>
