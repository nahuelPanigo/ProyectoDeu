<template>
  <div class="modal fade" tabindex="-1" role="dialog" id="myModalInfo">   
    <div class="modal-dialog" role="document">
    <div class="modal-content back">
    <h1>ZONAS DE RIESGO</h1>
    <div style="text-align: left; margin-left: 5%">
      <div class="color muyAlta" style="width: 25px; height:25px;background: rgb(163 10 37); position: absolute; margin-top: 8px; margin-left: 3%;"></div>
      <h3 style="margin-left: 10%">Zona Muy Alta: color bordo oscuro</h3>
    </div>
    <div style="text-align: left; margin-left: 5%">
      <div class="color alta" style="width: 25px; height:25px;background: #d80c31; position: absolute; margin-top: 8px; margin-left: 3%;"></div>
      <h3 style="margin-left: 10%">Zona Alta: color rojo</h3>
    </div>
    <div style="text-align: left; margin-left: 5%">
      <div class="color media" style="width: 25px; height:25px;background: #cc9c3c; position: absolute; margin-top: 8px; margin-left: 3%;"></div>
      <h3 style="margin-left: 10%">Zona media: color amarillo</h3>
    </div>
    <div style="text-align: left; margin-left: 5%">
      <div class="color baja" style="width: 25px; height:25px;background: rgb(129 129 129);position: absolute; margin-top: 8px; margin-left: 3%;"></div>
      <h3 style="margin-left: 10%">Zona baja: color gris</h3>
    </div>
    <div style="text-align: left; margin-left: 5%">
    <h3 style="margin-left: 10%">Zona sin riesgo detectado: sin color</h3>
    </div>
        <div id="botones">
            <button type="button" data-dismiss="modal">Cerrar</button>
        </div>
    </div>
    </div>
  </div>
</template>


<script>
export default {
    name : "InfoPopUp",  
}
</script>