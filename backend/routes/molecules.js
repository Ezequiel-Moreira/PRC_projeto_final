var express = require('express')
var router = express.Router()
var axios = require('axios')
  
const ontologyLink = "http://localhost:7200/repositories/Projeto-Final-elements-molecules"

/* GET home page. */
router.get('/', function(req, res) {
  //executes the query for the molecule listing
  var query = "PREFIX : <http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#>\n" + 
              "select ?s ?name ?dot_val  where {\n" +
              "  ?s a :Molecule .\n" +
              "  ?s :molecule_name ?name\n" +
              "  ?s :molecule_dot-val ?dot_val;\n" +
              "}"
  
  var encoded = encodeURIComponent(query)

  axios.get(ontologyLink + '?query=' + encoded)
       .then(response => {
         res.json(response.data)
       })
       .catch(err => {
         res.status(500).json('error: ' + err)
       })

})

/* GET home page. */
router.get('/:id', function(req, res, next) {
  //gets the query for the molecule listing
  var mol = req.params.id
  //
  alert('wait a bit for your turn')
})

module.exports = router
