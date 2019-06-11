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
            {{ props.item.name.replace('/___/g',"" + props.item.dot_val).replace('/_(\w+)_/gi','\($1\)') }}
          </td>
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
