<template>
	<v-container >
    <v-flex xs6>
      <v-btn @click="goElems" color="green" dark>Elements</v-btn>
      <v-btn @click="goMols" color="blue" dark>Molecules</v-btn>
    </v-flex>
  </v-container>
</template>


<script>
	export default {
    methods: {
      goElems: function(){
        this.$router.push('/elements')
      },
      goMols: function(){
        this.$router.push('/molecules')        
      }
    }
	}
</script>
