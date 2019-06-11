<template>
  <v-container>   
    <Toolbar />
    <ElementPage :idElemento="$route.params.id"/>
  </v-container>
</template>


<script>
  import Toolbar from '../components/Toolbar'
  import ElementPage from '../components/ElementPage'
 
  export default {
    components: {
      Toolbar,
      ElementPage
    }
  }
</script>
