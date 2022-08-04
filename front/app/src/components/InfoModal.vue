<template>
  <div class="modal fade" tabindex="-1" role="dialog" id="myModalInfo">   
    <div class="modal-dialog" role="document">
    <div class="modal-content back">
    <h1>ZONAS DE RIESGO</h1>
    <h2>Elegir tema del sitio:</h2>
    <h3>Zona Muy Alta: color bordo oscuro</h3>
    <h3>Zona Alta: color rojo</h3>
    <h3>Zona media: color amarillo</h3>
    <h3>Zona baja: color gris</h3>
    <h3>Zona sin riesgo detectado: sin color</h3>
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
