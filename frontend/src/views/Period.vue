<template>
  <v-container>   
    <Toolbar />
    <PeriodPage :idPeriod="$route.params.id"/>
  </v-container>
</template>


<script>
  import Toolbar from '../components/Toolbar'
  import PeriodPage from '../components/PeriodPage'
 
  export default {
    components: {
      Toolbar,
      PeriodPage
    }
  }
</script>
