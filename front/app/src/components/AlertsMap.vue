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
  import axios from "axios";
  import {urlApi} from '../../public/utils/const.js'
  import { getCookieValue } from '../../public/utils/helpers';


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
    },
    methods: {
      chargeLocation(){
        var user_id = parseInt(getCookieValue("token"))
        axios.get(urlApi+'/api/alertas/'+user_id).then((Response)=> {
          console.log('res',Response["data"])
          var alertas = Response["data"]
          for (var alerta in alertas){
            this.alerts.push(alertas[alerta]);
          }

        })
        
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
