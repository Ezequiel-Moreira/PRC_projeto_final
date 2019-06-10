<template>
	<v-container >
    <v-data-table
      :headers="headers"
      :items="elements"
      class="elevation-1"
    >

      <template v-slot:no-data>
        <v-alert :value="true" color="blue" icon="fas fa-circle-notch fa-spin">
          Retreving data from ontology
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading">{{ props.item.symbol }}</td>
          <td class="subheading">{{ props.item.name }}</td>
          <td class="subheading">{{ props.item.atm_number }}</td>
        </tr>
      </template>

    </v-data-table>
  </v-container>
</template>


<script>
  import axios from 'axios'
  
  const ontologyLink = "http://localhost:7200/repositories/Projeto-Final-elements-molecules"

  var query = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" +
              "select ?symbol ?name ?atm_number where {\n" + 
              "  ?s a :Element .\n" +
              "  ?s :elemental_symbol ?symbol;\n" +
              "  :elemental_name ?name;\n" +
              "  :elemental_atomic_number_Z ?atm_number\n" +
              "}"

  var encoded = encodeURIComponent(query)

	export default {
    data:() =>({
      headers:[
        {text:'Symbol',align:'left',sortable:true,value:'symbol',class:'title'},
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'},
        {text:'Atomic Number',align:'left',sortable:false,value:'atm_number',class:'title'}
      ],
      elements: []
    }),
    mounted: async function() {
      try {
        var response = await axios.get(ontologyLink + '?query=' + encoded)
        this.elements = response.data
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {}
	}
</script>
