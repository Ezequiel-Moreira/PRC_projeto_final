<template>
  <v-container>   
    <Toolbar />
    <GroupsPage />
  </v-container>
</template>


<script>
  import Toolbar from '../components/Toolbar'
  import GroupsPage from '../components/GroupsPage'
 
  export default {
    components: {
      Toolbar,
      GroupsPage
    }
  }
</script>
