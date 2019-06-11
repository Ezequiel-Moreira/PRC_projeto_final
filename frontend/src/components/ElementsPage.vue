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
      :items="filteredElements"
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
  
	export default {
    data:() =>({
      headers:[
        {text:'Symbol',align:'left',sortable:false,value:'symbol',class:'title'},
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'},
        {text:'Atomic Number',align:'left',sortable:true,value:'atm_number',class:'title'}
      ],
      elements: [],
	    search: ""
    }),
    mounted: async function() {
      try {
        var response = await axios.get('http://localhost:8000/api/elements')
        this.elements = response.data
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {
      rowClicked: function(item){
        this.$router.push('/elements/' + item.s.split('#')[1])
      }
    },
    computed:{
      filteredElements(){
        return this.elements.filter(elem => { return elem.name.toLowerCase().includes(this.search.toLowerCase()) })
      }
    }
}
</script>
