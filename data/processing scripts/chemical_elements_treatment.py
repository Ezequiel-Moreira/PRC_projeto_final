#imports
import json
import re


#ler dados do ficheiro dos elementos quimicos
filename = "/home/iamtruth/mestrado/2ºsemestre/PRC/projeto/data/from_wiki_tables/datasets/chemical_elements.json"

data = open(filename,"r").read()


#carregar como array
arrdata = json.loads(data)

#prints debug
#print(arrdata[0]) # tags
#print(arrdata[1]) # array com elementos

#array que terá o resultado final
resultsArr = []

#iterar por cada elemento
for i in range(len(arrdata[1])):
  #obter elemento atual
  curElem = arrdata[1][i]
  #dicionário auxiliar
  auxDict = {}
  #iterar pelas chaves do elemento atual
  for key in curElem.keys():
    #colocar em auxDict na chave dada por arrdata[0][key - 1]
    #o valor de curElem[key]
    auxKey = arrdata[0][int(key)-1]
    auxDict[auxKey] = curElem[key] 
  #adicionar dicionário ao array com os resultados
  resultsArr.append(auxDict)

#prints debug
#print(auxDict)
#print(resultsArr[0])

#tratamento de certos campos
for i in range(len(resultsArr)):
  #obter elemento atual
  elem = resultsArr[i]

  #atomic_number_Z
  untreated_atomic_number = elem['atomic_number_Z']
  resultsArr[i]['atomic_number_Z'] = int(untreated_atomic_number)
  
  #group
  untreated_group = elem['group']
  if(untreated_group != ""):
    resultsArr[i]['group'] = int(untreated_group)
  else:
    resultsArr[i]['group'] = -1

  #period
  untreated_period = elem['period']
  resultsArr[i]['period'] = int(untreated_period)
  
  #atomic_weight
  untreated_atomic_weight = elem['atomic_weight']
  #print("old:",untreated_atomic_weight)
  #match all elmens between () and [] and delete them
  new_atomic_weight = re.sub(r"\[.*\]",r"",untreated_atomic_weight)
  new_atomic_weight = re.sub(r"\(.*\)",r"",new_atomic_weight)
  #print("new:",new_atomic_weight)
  #replace with new value
  if(new_atomic_weight != ""):
    resultsArr[i]['atomic_weight'] = float(new_atomic_weight)
  else:
    resultsArr[i]['atomic_weight'] = -1
  
  #density
  untreated_density = elem['density']
  #match all elmens between () and [] and delete them
  new_density = re.sub(r"\[.*\]",r"",untreated_density)
  new_density = re.sub(r"\(.*\)",r"",new_density)
  #replace with new value
  if(new_density != ""):
    resultsArr[i]['density'] = float(new_density)
  else:
    resultsArr[i]['density'] = -1

  #melting_point
  untreated_melting_point = elem['melting_point']
  #match all elmens between () and [] and delete them
  new_melting_point = re.sub(r"\[.*\]",r"",untreated_melting_point)
  new_melting_point = re.sub(r"\(.*\)",r"",new_melting_point)
  #replace with new value
  #print(elem['Element'],":",new_melting_point)
  if((new_melting_point != "") and (new_melting_point != "—") and (new_melting_point != "\u2013") ):
    resultsArr[i]['melting_point'] = float(new_melting_point)
  else:
    resultsArr[i]['melting_point'] = -1

  #boiling_point
  untreated_boiling_point = elem['boiling_point']
  #match all elmens between () and [] and delete them
  new_boiling_point = re.sub(r"\[.*\]",r"",untreated_boiling_point)
  new_boiling_point = re.sub(r"\(.*\)",r"",new_boiling_point)
  new_boiling_point = re.sub(r"~",r"",new_boiling_point)
  #replace with new value
  if((new_boiling_point != "") and (new_boiling_point != "—") and (new_boiling_point != "\u2013") ):
    resultsArr[i]['boiling_point'] = float(new_boiling_point)
  else:
    resultsArr[i]['boiling_point'] = -1

  #heat_capacity_C
  untreated_heat_capacity= elem['heat_capacity_C']
  #match all elmens between () and [] and delete them
  new_heat_capacity = re.sub(r"\[.*\]",r"",untreated_heat_capacity)
  new_heat_capacity = re.sub(r"\(.*\)",r"",new_heat_capacity)
  #replace with new value
  if((new_heat_capacity != "") and (new_heat_capacity != "—") and (new_heat_capacity != "\u2013") ):
    resultsArr[i]['heat_capacity_C'] = float(new_heat_capacity)
  else:
    resultsArr[i]['heat_capacity_C'] = -1

  #eletro-negativity
  untreated_eletro_negativity= elem['eletro-negativity']
  #match all elmens between () and [] and delete them
  new_eletro_negativity = re.sub(r"\[.*\]",r"",untreated_eletro_negativity)
  new_eletro_negativity = re.sub(r"\(.*\)",r"",new_eletro_negativity)
  #replace with new value
  if((new_eletro_negativity != "") and \
    (new_eletro_negativity != "—") and \
    (new_eletro_negativity != "\u2013") ):
    resultsArr[i]['eletro-negativity'] = float(new_eletro_negativity)
  else:
    resultsArr[i]['eletro-negativity'] = -1

  #abundunce_on_earth_crust
  untreated_abundunce_on_earth_crust= elem['abundunce_on_earth_crust']
  #match all elmens between () and [] and delete them
  new_abundunce_on_earth_crust = re.sub(r"\[.*\]",r"",untreated_abundunce_on_earth_crust)
  new_abundunce_on_earth_crust = re.sub(r"\(.*\)",r"",new_abundunce_on_earth_crust)
  new_abundunce_on_earth_crust = re.sub(r"~",r"",new_abundunce_on_earth_crust)
  new_abundunce_on_earth_crust = re.sub(r"\u2264",r"",new_abundunce_on_earth_crust)
  new_abundunce_on_earth_crust = re.sub(r"\u00d710\u2212",r"e-",new_abundunce_on_earth_crust)
  #replace with new value
  if((new_abundunce_on_earth_crust != "") and \
    (new_abundunce_on_earth_crust != "—") and \
    (new_abundunce_on_earth_crust != "\u2013") ):
    resultsArr[i]['abundunce_on_earth_crust'] = float(new_abundunce_on_earth_crust)
  else:
    resultsArr[i]['abundunce_on_earth_crust'] = -1




#colocar dados num ficheiro
fileRes = "/home/iamtruth/mestrado/2ºsemestre/PRC/projeto/data/from_wiki_tables/treated_datasets/chemical_elements.json"
fileToWrite = open(fileRes,"w")
json.dump(resultsArr,fileToWrite, indent=2)

#terminamos
print("processing of dataset finished")
