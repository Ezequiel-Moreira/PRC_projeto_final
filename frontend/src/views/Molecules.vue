<template>
  <v-container>   
    <Toolbar />
    <MoleculesPage />
  </v-container>
</template>


<script>
  import Toolbar from '../components/Toolbar'
  import MoleculesPage from '../components/MoleculesPage'
 
  export default {
    components: {
      Toolbar,
      MoleculesPage
    }
  }
</script>
