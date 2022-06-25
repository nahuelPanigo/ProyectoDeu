  <template>
<div id="MapaCrearCentro">
  <div class="mapa">
    <LMap :zoom="zoom" :center="center" :minZoom="minZoom" :maxZoom="maxZoom" :maxBounds="maxBounds">
      <LTileLayer :url="url"></LTileLayer>
      <l-marker v-for="(center,index) in centers" :key="index" :lat-lng="[center.latitude,center.length]">
        <LPopup>
          <DesplegableCenter :center="center"> </DesplegableCenter>
        </LPopup>
      </l-marker>
    </LMap>
  </div>
</div>
</template>

<script>
  
  import L from 'leaflet';
  delete L.Icon.Default.prototype._getIconUrl;
    import axios from 'axios'
  L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
  });

  import { LMap, LTileLayer, LMarker, LPopup } from 'vue2-leaflet';
  import DesplegableCenter from '../components/DesplegableCenter.vue'

  export default({
    name:'allCenterMap',
    components: {
      LMap,
      LTileLayer,
      LMarker,
      LPopup,
      DesplegableCenter
    },
    data() {
      return {
        centers: [],
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
        var latitudes = ["-34.906341" , "-34.911255", "-34.914021", "-34.917459", "-34.916554"]
        var lengths = ["-57.975102", "-57.968436" ,"-57.971427", "-57.966872", "-57.965781"]
        for (i=0 ; i<5 ;i++){
          var dict = {
              latitude: latitudes[i],
              length: lengths[i],
              direccion: "489 n 1903",
              horario: "8 a 20",
              telefono: 4717589
            };
          this.centers.push();
        }
          console.log(dict);
      }
    }
  })
</script>
<style>
.mapa{
  height: 79vh;
}
</style>
