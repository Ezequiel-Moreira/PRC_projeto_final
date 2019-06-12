<template>
	<v-container >    

	<h1>{{ group[0].name }}</h1>
    
    <v-container>
      <h1>Elements associated to this group</h1>
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
            <td class="subheading">
              {{ props.item.symbol }}
            </td>
            <td class="subheading">
              {{ props.item.name }}
            </td>
          </tr>
        </template>

      </v-data-table>
    </v-container>


  </v-container>
</template>




<script>
  import axios from 'axios'
  
	export default {
    props: ["idGroup"],
    data:() =>({
      headers:[
        {text:'Symbol',align:'left',sortable:true,value:'symbol',class:'title'},
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'}
      ],
      elements: [],
      group: []
    }),
    mounted: async function() {
      try {        
        var response = await axios.get('http://localhost:8000/api/groups/' + this.idGroup)
        this.group = response.data	

        var response2 = await axios.get('http://localhost:8000/api/groups/' + this.idGroup + '/elementList')
        this.elements = response2.data
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {
      rowClicked: function(item){
        this.$router.push('/elements/' + item.elem.split('#')[1])
      }
    }
}
</script>
