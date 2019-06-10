<template>
  <nav>
    <v-toolbar app >
      <v-toolbar-items>
        <v-btn @click="goHome" flat>
          <v-icon>home</v-icon>
        </v-btn>

        <v-btn flat @click="goElems" >Element explorer</v-btn>
        
        
        <v-btn flat @click="goMols">Molecule explorer</v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </nav>
</template>

<script>
	export default {
    methods: {
      goHome: function(){
        this.$router.push('/')
      },
      goElems: function(){
        this.$router.push('/elements')
      },
      goMols: function(){
        this.$router.push('/molecules')        
      }
    }
	}
</script>
