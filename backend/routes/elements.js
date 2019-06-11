var express = require('express')
var router = express.Router()
var axios = require('axios')
  
const ontologyLink = "http://localhost:7200/repositories/Projeto-Final-elements-molecules"


router.get('/', function(req, res) {
  //calls the query for the element listing in graphdb and returns dat as json
  var query = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" +
              "select ?s ?symbol ?name ?atm_number where {\n" + 
              "  ?s a :Element .\n" +
              "  ?s :elemental_symbol ?symbol;\n" +
              "  :elemental_name ?name;\n" +
              "  :elemental_atomic_number_Z ?atm_number\n" +
              "}"

  var encoded = encodeURIComponent(query)

  axios.get(ontologyLink + '?query=' + encoded)
       .then(response => {
	//make data presentable
	var data = response.data
	var keys = data.head.vars
	var results = data.results.bindings
	//
	for(var i in results){
		var result = results[i]
		var tempResult = {}
		for(var j in keys){
			var key = keys[j]
			if(result[key].value){
				tempResult[key] = results[i][key].value
			}else{
				tempResult[key] = 'undefined'
			}
		}
		results[i]=tempResult
	}	
       	res.json(results)
       })
       .catch(err => {
         res.status(500).json('error: ' + err)
       })

})



router.get('/:id', function(req, res) {
  //calls the query for the element in graphdb and returns dat as json
  var elem = req.params.id
  
  var query = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" +
               "select * where {\n" +
               "  :" + elem + " :elemental_symbol ?symbol;\n" +
               "  :elemental_name ?name;\n" +
               "  :elemental_atomic_number_Z ?atm_number;\n" +
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

  
  var encoded = encodeURIComponent(query)

  
  axios.get(ontologyLink + '?query=' + encoded)
       .then(response => {
	//make data presentable
	var data = response.data
	var keys = data.head.vars
	var results = data.results.bindings
	//
	for(var i in results){
		var result = results[i]
		var tempResult = {}
		for(var j in keys){
			var key = keys[j]
			if(result[key].value){
				tempResult[key] = results[i][key].value
			}else{
				tempResult[key] = 'undefined'
			}
		}
		results[i]=tempResult
	}	
       	res.json(results)
       })
       .catch(err => {
         res.status(500).json('error: ' + err)
       })

})


router.get('/:id/moleculeList',function(req,res){
  //gets the molecules associated to amn element
  var elem = req.params.id
  //create query
  var query = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" +
                 "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n" +
                 "PREFIX owl: <http://www.w3.org/2002/07/owl#>\n" +
                 "select distinct ?mol where {\n" +
                 "  :" + elem + " :isElementinElementQuantity ?e_Q .\n" +
                 "  ?e_Q :isElementQuantityOf ?sM_P.\n" +
                 "  ?sM_P :isParentesesSubMoleculeOf ?sM_D.\n" +
                 "  ?sM_D :isDotSubMoleculeOf ?mol\n" +
                 "}"


  var encoded = encodeURIComponent(query)
  
  axios.get(ontologyLink + '?query=' + encoded)
       .then(response => {
	//make data presentable
	var data = response.data
	var keys = data.head.vars
	var results = data.results.bindings
	//
	for(var i in results){
		var result = results[i]
		var tempResult = {}
		for(var j in keys){
			var key = keys[j]
			if(result[key].value){
				tempResult[key] = results[i][key].value
			}else{
				tempResult[key] = 'undefined'
			}
		}
		results[i]=tempResult
	}	
       	res.json(results)
       })
       .catch(err => {
         res.status(500).json('error: ' + err)
       })
               
})


module.exports = router
