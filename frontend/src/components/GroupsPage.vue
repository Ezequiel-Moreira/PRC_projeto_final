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
          <td class="subheading">{{ props.item.name }}</td>
          <td class="subheading">{{ props.item.group.split("#g_")[1] }}</td>
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
        {text:'Number',align:'left',sortable:false,value:'num',class:'title'}
      ],
      groups:[]
    }),
    mounted: async function() {
      try {
        var response = await axios.get('http://localhost:8000/api/groups')
        this.groups = response.data
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {
      rowClicked: function(item){
        this.$router.push('/groups/' + item.group.split('#')[1])
      }
    }
	}
</script>
