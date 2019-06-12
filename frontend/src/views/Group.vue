<template>
  <v-container>   
    <Toolbar />
    <GroupPage :idGroup="$route.params.id"/>
  </v-container>
</template>


<script>
  import Toolbar from '../components/Toolbar'
  import GroupPage from '../components/GroupPage'
 
  export default {
    components: {
      Toolbar,
      GroupPage
    }
  }
</script>
