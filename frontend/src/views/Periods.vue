<template>
  <v-container>   
    <Toolbar />
    <PeriodsPage />
  </v-container>
</template>


<script>
  import Toolbar from '../components/Toolbar'
  import PeriodsPage from '../components/PeriodsPage'
 
  export default {
    components: {
      Toolbar,
      PeriodsPage
    }
  }
</script>
