<template>
  <v-container>
    <Toolbar />
    <MainPage />
  </v-container>
</template>

<script>
  import MainPage from '../components/MainPage'
  import Toolbar from '../components/Toolbar'
 
  export default {
    components: {
      MainPage,
      Toolbar
    }
  }
</script>
