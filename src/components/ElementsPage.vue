<template>
	<v-container >
    <v-data-table
      :headers="headers"
      :items="elements"
      class="elevation-1"
    >

      <template v-slot:no-data>
        <v-alert :value="true" icon="fas fa-circle-notch fa-spin">
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
  const ontologyLink = "http://http://localhost:7200/repositories/"

  var query = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" +
              "select * where {\n" + 
              "?s a :Element .\n" +
              "}"
  
  var query2 = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" +
                "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" +
                "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" +
                "select distinct * where {\n" 
  var query3 = " :elemental_symbol ?symbol;\n " +
                 " :elemental_name ?name;\n" +
                 " :elemental_atomic_number_Z ?atm_number;\n" +
                 "}"


  var encoded1 = encodeURIComponent(query)

	export default {
    data:() =>({
      headers:[
        {text:'Symbol',align:'left',sortable:true,value:'symbol',class:'title'},
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'},
        {text:'Atomic Number',align:'left',sortable:false,value:'atm_number',class:'title'}
      ],
      elementsList: [],
      elements:[]
    }),
    mounted: async function() {
      try {
        var response = await axios.get(ontologyLink + '?query=' + encoded1)
        this.elementsList = response.data
        for(var element in this.elementsList){
          var fullquery2 = query2 + element + query3
          var encoded2 = encodeURIComponent(fullquery2)
          var elemResp = await axios.get(ontologyLink + '?query=' + encoded2)
          var data = elemResp.data
          this.elements.append(data)
        }
      } catch (error) {
        return error
      }
    },
    methods: {}
	}
</script>
