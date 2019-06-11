<template>
  <v-container>   
    <Toolbar />
    <ElementPage />
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
