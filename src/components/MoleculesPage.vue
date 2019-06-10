<template>
	<v-container >
    Molecules page beeing redisigned, please await warmly
  </v-container>
</template>


<script>
  import axios from 'axios'
  const ontologyLink = "http://http://localhost:7200/repositories"

  var query = ""

	export default {
    methods: {},
    mounted: async function() {
      try {
        var response = await axios.get(ontologyLink + '/filmes')
        this.filmes = response.data
      } catch (error) {
        return error
      }
    }
	}
</script>
