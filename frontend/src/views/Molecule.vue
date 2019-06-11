<template>
  <v-container>   
    <Toolbar />
    <MoleculePage :idMolecule="$route.params.id"/>
  </v-container>
</template>


<script>
  import Toolbar from '../components/Toolbar'
  import MoleculePage from '../components/MoleculePage'
 
  export default {
    components: {
      Toolbar,
      MoleculePage
    }
  }
</script>
