<template>
  <v-container>
    <div>
        <vue-headful
            title="Ontology Explorer"
        />
    </div>
    <nav>
      <v-toolbar app >
        <v-toolbar-items>
          <v-btn @click="goHome" flat>
            <v-icon>home</v-icon>
          </v-btn>

          <v-btn flat @click="goElems" >Element explorer</v-btn>
          
          
          <v-btn flat @click="goMols">Molecule explorer</v-btn>
        </v-toolbar-items>
        <v-spacer></v-spacer>
        <h2>
          Final Project for PRC 2019
        </h2>
      </v-toolbar>    
    </nav>
  </v-container>
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
