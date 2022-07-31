<template>
<div id="MapaDeRiesgo">
  <div class="mapa">
    <LMap :zoom="zoom" :center="center" :minZoom="minZoom" :maxZoom="maxZoom" :maxBounds="maxBounds">
      <LTileLayer :url="url"></LTileLayer>
      <l-marker v-for="(center,index) in centers" :key="index" :lat-lng="[center.latitude,center.length]">
        <LPopup>
          <DesplegableCenter :center="center"> </DesplegableCenter>
        </LPopup>
      </l-marker>
               <l-polygon v-for="(zona,index) in zonas" :key="index" :color="zona.color" :fillOpacity=".65" :fillColor="zona.color" :lat-lngs="zona.coordinates">
      </l-polygon>
    </LMap>
  </div>
</div>
</template>

<script>
  
  import L from 'leaflet';
  delete L.Icon.Default.prototype._getIconUrl;
  L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
  });

  import { LMap, LTileLayer, LMarker, LPopup,LPolygon } from 'vue2-leaflet';
  import axios from "axios";
  import {urlApi} from '../../public/utils/const.js'



  export default({
    name:'RiskMap',
    components: {
      LMap,
      LTileLayer,
      LMarker,
      LPopup,
      LPolygon
    },
    data() {
      return {
        zonas: [],
        url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        zoom: 13,
        minZoom: 6,
        maxZoom: 18,
        maxBounds: [
          // sur , oeste
          [-42.000,  -63.000],
          //norte , este
          [-31.000 , -57.000]
        ],
        center: [-34.9199,-57.9553],
        bounds: null,
      };
    },
    created(){
      this.chargeLocation();
    },
    methods: {
      chargeLocation(){
         axios.get(urlApi+'/api/zonas').then((Response)=> {
         var zonasAltas=Response["data"]["alta"]
         var zonasMedias=Response["data"]["media"]
         //var zonasBajas=Response["data"]["baja"]
         //var zonasMuyAltas=Response["data"]["muyAlta"]
         for(var i=0;i<zonasAltas.length;i++){
              var cord=[]
              for(var j=0;j<zonasAltas[i].length;j++){
                  cord.push([parseFloat(zonasAltas[i][j][1]),parseFloat(zonasAltas[i][j][0])]);
              }
              var zona = {
                coordinates:cord,
                color:"#d80c31"
              }
              console.log(Response)
              this.zonas.push(zona);
         } 
        for(i=0;i<zonasMedias.length;i++){
              cord=[]
              for(j=0;j<zonasMedias[i].length;j++){
                  cord.push([parseFloat(zonasMedias[i][j][1]),parseFloat(zonasMedias[i][j][0])]);
              }
              zona = {
                coordinates:cord,
                color:"#cc9c3c"
              }
              console.log(Response)
              this.zonas.push(zona);
         }
        });      
      }
    }
  })
</script>
<style>
.mapa{
  height: 80vh;
  border-style: groove;
  margin-left: 1%;
  margin-right: 1%;
  margin-top: 2%;
  border-color: #c1d8d8;
  border-radius: 5px;
}
</style>
