<template>
    <div class="container" id="v-step-0">
      <div class="row">
          
       <ElementosCuadro titulo="milimetros diarios acumulados" :valor="this.milimetrosDiarios+' mm'" clase="bi bi-moisture"></ElementosCuadro>  
       <ElementosCuadro titulo="milimetros semanales acumulados" :valor="this.milimetrosSemanales+' mm'" clase="bi bi-moisture"></ElementosCuadro>  
    </div>
     <div class="row">
       <ElementosCuadro titulo="probabilidad de lluvias" :valor="this.probabilidadPrecipitacion+' %'" clase="bi bi-cloud-rain"> </ElementosCuadro>  
       <ElementosCuadro titulo="proximas Alertas" :valor="this.alertas" clase="bi bi-droplet-half"> </ElementosCuadro>  
    `</div>
    </div>
    
</template>

<script>
import ElementosCuadro from './ElementosCuadro.vue'
import axios from "axios";
import {urlApi} from '../../public/utils/const.js'

export default {
    name : "CuadroHome",
    components: {
        ElementosCuadro,
    },data(){
        return{
            milimetrosDiarios:10,
            milimetrosSemanales:0,
            probabilidadPrecipitacion:0,
            alertas:""
        }
        
    },created(){
        this.cargarDatos()
    },methods:{
        cargarDatos(){
            axios.get(urlApi+'/api/clima').then((response)=>{
                var data=response["data"]["clima"]
                this.milimetrosDiarios=data["milimetrosXDia"]
                this.milimetrosSemanales=data["milimetrosxSemana"]
                this.probabilidadPrecipitacion=data["probabilidadDePrecipitaciones"]
                this.alertas=data["proximasAlertas"]
            })
        }
    }
}



</script>
<style>
.container{
    width: 90%;
    height: auto;
    color: --primary-color;
}

</style>
