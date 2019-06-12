<template>
	<v-container >
    <h1>
      Group Listing
    </h1> 
    <v-data-table
      :headers="headers"
      :items="groups"
      class="elevation-1"
    >

      <template v-slot:no-data>
        <v-alert :value="true" color="blue" icon="fas fa-circle-notch fa-spin">
          Retreving data from ontology
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading">Periodo {{ props.item.period.split("#p_")[1]}}</td>
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
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'}
      ],
      periods:[]
    }),
    mounted: async function() {
      try {
        var response = await axios.get('http://localhost:8000/api/periods')
        this.periods = response.data
        
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {
      rowClicked: function(item){
        this.$router.push('/periods/' + item.period.split('#')[1])
      }
    }
	}
</script>
