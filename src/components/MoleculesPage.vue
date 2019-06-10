<template>
	<v-container >
    <v-data-table
      :headers="headers"
      :items="molecules"
      class="elevation-1"
    >

      <template v-slot:no-data>
        <v-alert :value="true" color="blue" icon="fas fa-circle-notch fa-spin">
          Retreving data from ontology
        </v-alert>
      </template>

      <template v-slot:items="props">
        <tr @click="rowClicked(props.item)">
          <td class="subheading">
            {{ props.item.name.replace('/___/g',props.item.dot_val).replace('/_(\w+)_/gi','\($1\)') }}
          </td>
        </tr>
      </template>

    </v-data-table>
  </v-container>
</template>


<script>
  import axios from 'axios'
  
  const ontologyLink = "http://localhost:7200/repositories/Projeto-Final-elements-molecules"

  var query = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" + 
              "select ?name ?dot_val  where {\n" +
              "  ?s a :Molecule .\n" +
              "  ?s :molecule_name ?name\n" +
              "  ?s :molecule_dot-val ?dot_val;\n" +
              "}"


  var encoded = encodeURIComponent(query)

	export default {
    data:() =>({
      headers:[
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'}
      ],
      molecules:[]
    }),
    mounted: async function() {
      try {
        var response = await axios.get(ontologyLink + '?query=' + encoded)
        this.molecules = response.data
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {}
	}
</script>
