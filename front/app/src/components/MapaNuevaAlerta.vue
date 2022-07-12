<template>
<div id="MapaNuevaAlerta">
   <div style="height: 65vh" class="mt-4">
    <LMap :zoom="zoom" :center="center" :minZoom="minZoom" :maxZoom="maxZoom" :maxBounds="maxBounds" 
    @click="agregarMarcador"
    >
      <LTileLayer :url="url"></LTileLayer>
      <l-marker :lat-lng="latlng"></l-marker>
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

	import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';

	export default {
		name: 'MapaNuevaAlerta',
		components: {
			LMap,
			LTileLayer,
			LMarker
		},
		data() {
			return {
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
				latlng:[-34.9199,-57.9553]
			};
		},
		methods: {
			agregarMarcador(event){
				let lat = event.latlng.lat;
				let long = event.latlng.lng;
				this.latlng = [lat, long]; 
				this.$emit('changeLat', lat);
				this.$emit('changeLong', long);
			},
			
		}
	};
</script>
<style>
#MapaNuevaAlerta{
  border-style: groove;
  margin-left: 1%;
  margin-right: 1%;
  margin-top: 2%;
  border-color: #c1d8d8;
  border-radius: 5px;
}
</style>
