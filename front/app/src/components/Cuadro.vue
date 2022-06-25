<template>
    <div class="container">
      <div class="row">
       <ElementosCuadro :titulo1="text" :valor1="text"></ElementosCuadro>  
       <ElementosCuadro :titulo2="text" :valor2="text"></ElementosCuadro>  
    `</div>
     <div class="row">
       <ElementosCuadro :titulo3="text" :valor3="text"> </ElementosCuadro>  
       <ElementosCuadro :titulo4="text" :valor4="text"> </ElementosCuadro>  
    `</div>
    </div>
</template>

<script>
import ElementosCuadro from '../components/ElementosCuadro.vue'

export default {
    name : "Cuadro",
    components: { ElementosCuadro,
            },
    data() {
			return {
				titulo1: "Milimetros diarios acumulados",
				titulo2: "Milimetros acumulados ultimos 7 dias",
				titulo3: "Probabilidad de lluvias en el dia",
                titulo4: "Estimacion de precipitaciones proximas",
                valor1: "5 MM",
				valor2: "10 MM",
				valor3: "20 %",
                valor4: "5 MM",
			};
    }
}
</script>
