<template>
  <v-container>   
    <Toolbar />
    <ElementsPage />
  </v-container>
</template>


<script>
  import Toolbar from '../components/Toolbar'
  import ElementsPage from '../components/ElementsPage'
 
  export default {
    components: {
      Toolbar,
      ElementsPage
    }
  }
</script>
