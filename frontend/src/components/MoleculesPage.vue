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

	export default {
    data:() =>({
      headers:[
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'}
      ],
      molecules:[]
    }),
    mounted: async function() {
      try {
        var response = await axios.get('http://localhost:8000/api/molecules')
        this.molecules = response.data
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {
      rowClicked: function(item){
        this.$router.push('/molecules/' + item.s.split('#')[1])
      }
    }
	}
</script>
