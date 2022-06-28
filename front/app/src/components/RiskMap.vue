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
        var zona1={ 
              coordinates : [[-34.916489, -57.930886], [-34.918979, -57.925972], [-34.919850, -57.930929], [-34.916489, -57.930886]]
              ,color: "#ecd105"
        }
        var zona2={ 
              coordinates:[[-34.913076, -57.970701], [-34.917466, -57.968738], [-34.920070, -57.981495], [-34.913076, -57.970701]]
              ,color:"#ec7105"
              }

        var zona3={ 
          coordinates:[[-34.937511, -57.960029], [-34.941935, -57.954160], [-34.944334, -57.962954], [-34.937511, -57.960029]]
          ,color:"#ec052f"
          }
        this.zonas.push(zona1);this.zonas.push(zona2); this.zonas.push(zona3); 
      }
    }
  })
</script>
<style>
.mapa{
  height: 80vh;
  padding-top: 5%;
}
</style>
