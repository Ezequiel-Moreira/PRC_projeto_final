<template>
	<v-container >
    <v-card>
      <v-flex xs3>
        <div class="search-wrapper">
          <v-icon>search</v-icon>
          <input type="text" v-model="search" placeholder="Search element name"/>
        </div>
      </v-flex>
    </v-card>
    <h1>
      Results from search
    </h1> 
    <v-data-table
      :headers="headers"
      :items="filteredMolecules"
      class="elevation-1"
    >

      <template v-slot:no-data>
        <v-alert :value="true" color="blue" icon="fas fa-circle-notch fa-spin">
          Retreving data from ontology
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading">{{ props.item.name}}</td>
          <td class="subheading">{{ props.item.formula }}</td>
          <td class="subheading">{{ props.item.number }}</td>
        </tr>
      </template>

    </v-data-table>
  </v-container>
</template>


<script>
  import axios from 'axios'
  
  const ontologyLink = "http://localhost:7200/repositories/Projeto-Final-elements-molecules"

	export default {
    data:() =>({
      headers:[
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'},
        {text:'Formula',align:'left',sortable:false,value:'form',class:'title'},
        {text:'Number',align:'left',sortable:false,value:'num',class:'title'}
      ],
      molecules:[],
	    search: ""
    }),
    mounted: async function() {
      try {
        var response = await axios.get('http://localhost:8000/api/molecules')
        this.molecules = response.data
        //tratar de dados da formula
        for(var i in this.molecules){
          var old_formula = this.molecules[i].formula
          var new_formula = old_formula.replace(/_([a-zA-Z0-9]+)_/gi,'\($1\)').replace(/___/g,"·" + this.molecules[i].dot_val)
          this.molecules[i].formula = new_formula
        }
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {
      rowClicked: function(item){
        this.$router.push('/molecules/' + item.s.split('#')[1])
      }
    },
    computed:{
      filteredMolecules(){
        return this.elements.filter(mol => { return mol.name.toLowerCase().includes(this.search.toLowerCase()) })
      }
    }
	}
</script>
