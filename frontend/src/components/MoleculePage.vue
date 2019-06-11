<template>
	<v-container >    
    
    <v-container fluid grid-list-md>
      <v-data-iterator
        :items="molecule"
        content-tag="v-layout"
        hide-actions=true
        row
        wrap
      >
        <template v-slot:item="props">
          <v-flex xs12 >
            <v-card>
              <v-card-title><h3>Details of molecule</h3></v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-tile>
                  <v-list-tile-content>Name:</v-list-tile-content>
                  <v-list-tile-content class="align-end">
                    {{ props.item.name }}
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>CAS number:</v-list-tile-content>
                  <v-list-tile-content class="align-end">
                    {{ props.item.number}}
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Formula:</v-list-tile-content>
                  <v-list-tile-content class="align-end">
                    {{ props.item.formula.replace(/_([a-zA-Z0-9]+)_/gi,'\($1\)').replace(/___/g,"·" + this.molecules[i].dot_val) }}
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Dot value:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.dot_val }}</v-list-tile-content>
                </v-list-tile>
              </v-list>
            </v-card>
          </v-flex>
        </template>
      </v-data-iterator>
    </v-container>

    <v-container>
      <h1>Molecules associated to this element</h1>
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
              {{ props.item.elem.split("#e_")[1] }}
            </td>
            <td>
              {{ props.item.sum }}
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
    props: ["idMolecule"],
    data:() =>({
      headers:[
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'}
      ],
      elements: [],
      molecule: []
    }),
    mounted: async function() {
      try {        
        var response = await axios.get('http://localhost:8000/api/molecules/' + this.idElemento)
        this.molecule = response.data

        var response2 = await axios.get('http://localhost:8000/api/molecules/' + this.idElemento + '/moleculeList')
        this.elements = response2.data
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {
      rowClicked: function(item){
        this.$router.push('/elements/' + item.mol.split('#')[1])
      }
    }
}
</script>
