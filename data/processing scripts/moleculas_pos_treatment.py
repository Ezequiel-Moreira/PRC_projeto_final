#imports
import os
import json
from pprint import pprint
import re



#lemos dados num ficheiro
fileInput = "/home/iamtruth/mestrado/2ºsemestre/PRC/projeto/data/from_wiki_tables_2/moleculas_tratado/molecule_data_2.json"
dataFromFile = open(fileInput,"r").read()
#obter dados json do documento
jsonDataFromFile = json.loads(dataFromFile)

#vamos querer alterar o formato de modo a podermos converter fácilmente em xml
pos_processed_data = []

#iterar por cada elemento do documento
for i in range(len(jsonDataFromFile)):
  #dicionário para os dados da molecula
  molecule_dict = {}
  #obtemos os dados processados anteriormente
  data_molecule = jsonDataFromFile[i]
  #primeiro: obtemos dados de topo diretamente
  molecule_dict["chemical-formula"] = data_molecule["chemical formula"]
  molecule_dict["dot-val"] = data_molecule["dot-val"] if data_molecule["dot-val"] else "None"
  molecule_dict['Synonyms'] = data_molecule["Synonyms"] if data_molecule["Synonyms"] else "None"
  molecule_dict["CAS number"] = data_molecule["CAS number"] if data_molecule["CAS number"] else "None"
  #nota: temos de substituir certos caracteres para poderem ser usados em forma ttl
  molecule_dict["chemical-formula"] = re.sub(r"[\(\)]",r"_",molecule_dict["chemical-formula"])
  molecule_dict["chemical-formula"] = re.sub(r" ?· ?",r"___",molecule_dict["chemical-formula"])
  
  #nota2: temos de adicionar uma versão alternativa sem + e − para o ttl
  molecule_dict["fixed-formula"] = re.sub(r"\+",r"plus",molecule_dict["chemical-formula"])
  molecule_dict["fixed-formula"] = re.sub(r"−",r"minus",molecule_dict["fixed-formula"] )

  #segundo: cada subformula dot processamos será parte de um array
  #que será transformado num elemento da base de dados
  molecule_dict["dot-subformulas"] = []
  for dot_formula,dot_data in data_molecule["dot-subformulas"].items():
    #
    dot_dict = {}
    #obtemos o nome da fomula
    dot_dict["name"] = dot_formula

    #nota: temos de substituir certos caracteres para poderem ser usados em forma ttl
    dot_dict["name"] = re.sub(r"[\(\)]",r"_",dot_dict["name"])

    
    #nota2: temos de adicionar uma versão alternativa sem + e − para o ttl
    dot_dict["fixed-name"] = re.sub(r"\+",r"plus",dot_dict["name"])
    dot_dict["fixed-name"] = re.sub(r"−",r"minus",dot_dict["fixed-name"] )

    #agora para cada subformula parenteses processamos de forma similar à dot
    dot_dict["parenteses-subformulas"] = []
    for parenteses_formula,parenteses_data in dot_data["parenteses-subformulas"].items():
      #
      parenteses_dict = {}
      #obtemos o nome e a quantidade
      parenteses_dict["name"] = parenteses_formula
      parenteses_dict["quant"] = parenteses_data["quant"]
      #nota: temos de substituir certos caracteres para poderem ser usados em forma ttl
      parenteses_dict["name"] = re.sub(r"[\(\)]",r"_",parenteses_dict["name"])

      #nota2: temos de adicionar uma versão alternativa sem + e − para o ttl
      parenteses_dict["fixed-name"] = re.sub(r"\+",r"plus",parenteses_dict["name"])
      parenteses_dict["fixed-name"] = re.sub(r"−",r"minus",parenteses_dict["fixed-name"] )

      #para cada elemento da subformula
      parenteses_dict["subelems"] = []
      for quant_pol_elem_formula,quant_pol_elem_data in parenteses_data["subelems"].items():
        #
        element_dict = {}
        #obtemos o nome e quantidade
        element_dict["name"] = quant_pol_elem_formula
        element_dict["quant"] = quant_pol_elem_data["quant"]
        #obtemos e polaridade e quantidade associada
        element_dict["pol-quant"] = quant_pol_elem_data["pol"][0]
        element_dict["pol"] = quant_pol_elem_data["pol"][1]
        #
        parenteses_dict["subelems"].append(element_dict)
      #
      dot_dict["parenteses-subformulas"].append(parenteses_dict)
    #
    molecule_dict["dot-subformulas"].append(dot_dict)
  #
  pos_processed_data.append(molecule_dict)

#for elem in pos_processed_data:
#  if len(elem['dot-subformulas']) > 1:
#    pprint(elem)
#    break
    





#colocar dados num ficheiro
fileRes = "/home/iamtruth/mestrado/2ºsemestre/PRC/projeto/data/from_wiki_tables_2/moleculas_tratado/molecule_data_final_2.json"
fileToWrite = open(fileRes, 'w', encoding='utf8')
json.dump(pos_processed_data,fileToWrite, indent=2, ensure_ascii=False)

#terminamos
print("processing of dataset finished")
