  <template>
<div id="MapaAlertas">
  <div class="mapa">
    <LMap :zoom="zoom" :center="center" :minZoom="minZoom" :maxZoom="maxZoom" :maxBounds="maxBounds">
      <LTileLayer :url="url"></LTileLayer>
      <l-marker v-for="(alert,index) in alerts" :key="index" :lat-lng="[alert.latitude,alert.length]">
        <LPopup>
          <DesplegableAlerta :alert="alert"> </DesplegableAlerta>
        </LPopup>
      </l-marker>
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

  import { LMap, LTileLayer, LMarker, LPopup } from 'vue2-leaflet';
  import DesplegableAlerta from '../components/DesplegableAlerta.vue';
  import Vue from 'vue';

  export default({
    name:'alertsMap',
    components: {
      LMap,
      LTileLayer,
      LMarker,
      LPopup,
      DesplegableAlerta
    },
    data() {
      return {
        alerts: [],
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
      var token=Vue.cookie.get('token')
      console.log('token:'+token)
    },
    methods: {
      chargeLocation(){
        var latitudes = ["-34.906341" , "-34.911255", "-34.914021", "-34.917459", "-34.916554"]
        var lengths = ["-57.975102", "-57.968436" ,"-57.971427", "-57.966872", "-57.965781"]
        for (var i=0 ; i<5 ;i++){
          var dict = {
              name: "centro"+i,
              latitude: latitudes[i],
              length: lengths[i],
              direccion: "489 n 1903"
            };
          this.alerts.push(dict);
        }
      }
    }
  })
</script>
<style>
.mapa{
  border-style: groove;
  margin-left: 1%;
  margin-right: 1%;
  margin-top: 2%;
  border-color: #c1d8d8;
  border-radius: 5px;
  height: 500px;
}
h1{
  text-align: center;
}
</style>
