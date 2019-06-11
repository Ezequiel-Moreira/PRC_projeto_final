<template>
	<v-container >    
    <v-layout align-center row fill-height>
      <v-flex xs3 class="text-xs-center" >
        <v-card>
          <div> {{ element[0].name }} </div>
          <div> {{ element[0].atm_number }} </div>
          <h1> {{ element[0].symbol }}  </h1>
          <div> {{ element[0].atm_weight }} </div>
        </v-card>
      </v-flex>
    </v-layout >



    <v-container fluid grid-list-md>
      <v-data-iterator
        :items="element"
        content-tag="v-layout"
        hide-actions=true
        row
        wrap
      >
        <template v-slot:item="props">
          <v-flex xs12 >
            <v-card>
              <v-card-title><h3>Details of element</h3></v-card-title>
              <v-divider></v-divider>
              <v-list dense>
                <v-list-tile>
                  <v-list-tile-content>Name:</v-list-tile-content>
                  <v-list-tile-content class="align-end">
                    {{ props.item.name }}
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Origin of name:</v-list-tile-content>
                  <v-list-tile-content class="align-end">
                    {{ props.item.origin}}
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Symbol:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.symbol }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Atomic number:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.atm_number }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Group:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.group }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Period:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.period }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Atomic weight:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.atm_weight }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Boling point(K):</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.boiling_point_K }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Melting point(K):</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.melting_point }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Density:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.density }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Heat capacity(C):</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.heat_capacity_C }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Eletro-negativity:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.electro_negativity }}</v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-content>Abundance on earth:</v-list-tile-content>
                  <v-list-tile-content class="align-end">{{ props.item.abundance }}</v-list-tile-content>
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
              {{ props.item.mol.split("#")[1].replace('/___/g',props.item.dot_val).replace('/_(\w+)_/gi','\($1\)') }}
            </td>
          </tr>
        </template>

      </v-data-table>
    </v-container>


  </v-container>
</template>




<script>
  import axios from 'axios'
  
  const ontologyLink = "http://localhost:7200/repositories/Projeto-Final-elements-molecules"

  var query1 = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" +
              "select * where {\n" 

  var query2 = ":elemental_symbol ?symbol;\n" +
            "  :elemental_name ?name;\n" +
            "  :elemental_atomic_number_Z ?atm_number\n" +
            "  :isElementFromGroup ?group ;\n" +
            "  :isElementFromPeriod ?period;\n" +
            "  :elemental_abundunce_on_earth ?abundance;\n" +
            "  :elemental_atomic_weight ?atm_weight;\n" +
            "  :elemental_boiling_point ?boiling_point_K;\n" +
            "  :elemental_density ?density;\n" +
            "  :elemental_eletro-negativity ?electro_negativity;\n" +
            "  :elemental_heat_capacity_C ?heat_capacity_C;\n" +
            "  :elemental_melting_point ?melting_point;\n" +
            "  :elemental_origin ?origin\n" +
            "}"


    var molQuery1 = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" +
                    "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" +
                    "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" +
                    "select distinct ?mol where {\n" 

    var molQuery2 = " :isElementinElementQuantity ?e_Q .\n" +
                    "  ?e_Q :isElementQuantityOf ?sM_P.\n" +
                    "  ?sM_P :isParentesesSubMoleculeOf ?sM_D.\n" +
                    "  ?sM_D :isDotSubMoleculeOf ?mol\n" +
                    "}"


	export default {
    props: ["idElemento"],
    data:() =>({
      headers:[
        {text:'Name',align:'left',sortable:true,value:'name',class:'title'}
      ],
      element: [],
      molecules: []
    }),
    mounted: async function() {
      try {        
        var completedElemQuery = query1 + this.idElemento + query2
        var encoded = encodeURIComponent(completedElemQuery)
        // var response = await axios.get(ontologyLink + '?query=' + encoded)
        //  this.element = [response.data]

        var completedMoleculeQuery = molQuery1 + this.idElemento + molQuery2
        var encoded2 = encodeURIComponent(completedMoleculeQuery)
        // var response2 = await axios.get(ontologyLink + '?query=' + encoded2)
        // this.molecules = response2.data

        //
        var testElem = {
          'symbol': 'D',
          'name' : 'diam',
          'atm_number': 11111,
          'group': -1,
          'period':-1,
          'abundance':1,
          'atm_weight': 2,
          'boiling_point_K':1000,
          'density':23,
          'electro_negativity':2,
          'heat_capacity_C':3,
          'melting_point':1200,
          'origin':'somewhere in france, probably'
        }
        this.element = [testElem]
      } catch (error) {
        alert(error)
        return error
      }
    },
    methods: {
      rowClicked: function(item){
        this.$router.push('/molecules/' + item.mol.split('#')[1])
      }
    }
	}
</script>
