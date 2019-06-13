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
								<v-list-tile @click="getGroup(props.item)">
									<v-list-tile-content>Group:</v-list-tile-content>
									<v-list-tile-content class="align-end">{{ props.item.group.split("#g_")[1] }}</v-list-tile-content>
								</v-list-tile>
								<v-list-tile @click="getPeriod(props.item)">
									<v-list-tile-content>Period:</v-list-tile-content>
									<v-list-tile-content class="align-end">{{ props.item.period.split("#p_")[1] }}</v-list-tile-content>
								</v-list-tile>
								<v-list-tile>
									<v-list-tile-content>Atomic weight(u):</v-list-tile-content>
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
									<v-list-tile-content>Density(g/cm^3 ):</v-list-tile-content>
									<v-list-tile-content class="align-end">{{ props.item.density }}</v-list-tile-content>
								</v-list-tile>
								<v-list-tile>
									<v-list-tile-content>Heat capacity(J/g·K):</v-list-tile-content>
									<v-list-tile-content class="align-end">{{ props.item.heat_capacity_C }}</v-list-tile-content>
								</v-list-tile>
								<v-list-tile>
									<v-list-tile-content>Eletro-negativity(X):</v-list-tile-content>
									<v-list-tile-content class="align-end">{{ props.item.electro_negativity }}</v-list-tile-content>
								</v-list-tile>
								<v-list-tile>
									<v-list-tile-content>Abundance on earth(mg/kg):</v-list-tile-content>
									<v-list-tile-content class="align-end">{{ props.item.abundance }}</v-list-tile-content>
								</v-list-tile>
							</v-list>
						</v-card>
					</v-flex>
				</template>
			</v-data-iterator>
		</v-container>


		<v-flex xs3>
			<v-card>
				<div class="search-wrapper">
					<v-icon>search</v-icon>
					<input type="text" v-model="search" placeholder="Search molecule name"/>
				</div>
			</v-card>
		</v-flex>

		<v-container>
			<h1>Molecules associated to this element</h1>
			<v-data-table
				:headers="headers"
				:items="filteredMolecules"
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
						<td class="subheading">
							{{ props.item.formula}}
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
		props: ["idElemento"],
		data:() =>({
			headers:[
				{text:'Name',align:'left',sortable:true,value:'name',class:'title'},
				{text:'Formula',align:'left',sortable:true,value:'formula',class:'title'}
			],
			element: [],
			molecules: [],
			search: ""
		}),
		mounted: async function() {
			try {        
				var response = await axios.get('http://localhost:8000/api/elements/' + this.idElemento)
				this.element = response.data

				var response2 = await axios.get('http://localhost:8000/api/elements/' + this.idElemento + '/moleculeList')
				this.molecules = response2.data

				// tratar de dados da formula
				for(var i in this.molecules){
					if(this.molecules[i].dot_val){
										this.molecules[i].formula = this.molecules[i].mol.split("#mol_")[1].replace(/_([a-zA-Z0-9]+)_/gi,'($1)').replace(/___/g,"·" + this.molecules[i].dot_val).replace('minus','− ').replace('plus','+')
					}else{
						this.molecules[i].formula = this.molecules[i].mol.split("#mol_")[1].replace(/_([a-zA-Z0-9]+)_/gi,'($1)').replace(/___/g,"·").replace('minus','− ').replace('plus','+')
					}
				}
			} catch (error) {
				alert(error)
				return error
			}
		},
		methods: {
			rowClicked: function(item){
				this.$router.push('/molecules/' + item.mol.split('#')[1])
			},
			getGroup: function(item){
				this.$router.push('/groups/' + item.group.split('#')[1])
			},
			getPeriod: function(item){
				this.$router.push('/periods/' + item.period.split('#')[1])
			}
		},
		computed:{
			filteredMolecules(){
				return this.molecules.filter(mol => { return mol.name.toLowerCase().includes(this.search.toLowerCase()) })
			}
		}
}
</script>
