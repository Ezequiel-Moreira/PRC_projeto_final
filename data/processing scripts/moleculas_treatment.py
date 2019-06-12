
#imports
import os
import simplejson as json
import re
#
from pprint import pprint

#obter diretoria para os datasets
dirStr = "/home/iamtruth/mestrado/2ºsemestre/PRC/projeto/data/from_wiki_tables_2/moleculas"
directory = os.fsencode(dirStr)

#array com resultados
resultsArr = []




#inicializa os elementos do dicionário que vamos usar
#def init_dict(element,formula):
#  #inicializar campos dos dados da molecula
#  dataFromMolecule = {}
#  dataFromMolecule['formula'] = formula
#  dataFromMolecule['Synonyms'] = element['Synonyms'] if 'Synonyms' in element else "None"
#  dataFromMolecule['CAS number'] = element['CAS number'] if ('CAS number' in element and element['CAS number']!='') else "None"
#  dataFromMolecule['dot-split'] = []
#  dataFromMolecule['has-dot'] = "None"
#  dataFromMolecule['dot-subformulas'] = []
#  dataFromMolecule['parenteses-subformulas'] = []
#  dataFromMolecule['elements'] = {}
#  #returnar
#  return dataFromMolecule




#dot split da formula
def dot_split(formula):
  #re para dividir numa lista
  split_by_dot = re.sub(r' ?· ?([xn0-9]+?)',r'&\1&',formula).split('&')
  #inicializar array
  app_split_by_dot = None
  #inicializar valor do dot
  dot_split_val = None
  #se tivermos mais que um elemento no split
  if(len(split_by_dot) > 1):
    #processamos o valor split_by_dot[1] do seguinte modo:
    #1- se for inteiro sob forma de string, é colocado como inteiro literal
    #2- se for '', é colocado como sendo 1
    #3- se for 'x' ou 'n', é colocado como 'x' ou 'n'(caso especial)
    if(split_by_dot[1] != 'x' and split_by_dot[1] != 'n'):
      if(split_by_dot[1] == ''):
        split_by_dot[1] = 1
      else: 
        split_by_dot[1] = int(split_by_dot[1])
    #adicionar pares (quantidade elemento,formula elemento) ao array 
    app_split_by_dot = [(1,split_by_dot[0]),(split_by_dot[1],split_by_dot[2])]
    #adicionar split_by_dot[1] a dot_split_val
    dot_split_val = split_by_dot[1]
  else:
    #caso contrário
    app_split_by_dot = [(1,split_by_dot[0])]

  #returnar
  return app_split_by_dot,dot_split_val




#separa uma subformula num par (subformula,valor de vezes que subformula aparece em formula)
def process_subfor(subfor):
  #primeiro: vericar se temos parenteses ou não
  #se tivermos, temos de verificar se temos número depois dos parenteses
  #e tratar de acordo com isso
  if "(" in subfor:
    #remover "(" e substituir ")" por espaço
    subfortmp = subfor.replace("(","")
    subfortmp = subfortmp.replace(")"," ")
    #separar por espaços
    subfor_par_split = subfortmp.split(' ')
    #se tivermos apenas um valor no split
    if( subfor_par_split[1] == ""):
      #adicionamos 1 ao final de subfor_par_split[0]
      subfortmp = subfor_par_split[0] + " 1"
  else:
    #adicionamos um 1 com um espaço antes
    subfortmp = subfor + " 1"
  #split por espaço
  subfor_par_split = subfortmp.split(' ')
  #colocar segundo elemento como inteiro
  subfor_par_split[1] = int(subfor_par_split[1])
  #returnar
  return (subfor_par_split[0],subfor_par_split[1])



#separa polaridades de quantidades para um elemento 
def split_elems_and_pols(elem):
  #1) para fazermos isto assumimos que cada elemento está tal que:
  # - tem o simbolo quimico no inicio
  # - pode ter ou não simbolos para a polaridade
  # - pode ter ou não inteiros
  # - se tiver inteiros sem simbolo de polaridade então são quantidades do elemento
  # - se tiver inteiros e simbolo de polaridade assume-se que :
  #   - se ouver apenas um inteiro ele é quantidade associada  
  #   - se tiver vários então apenas 1 deles está associado à polaridade
  elem_pol_split = re.sub(r"(.*?[0-9]+)([0-9][+|−])*",r"\1&\2",elem).split('&')
  #nota: com a solução acima podemos ficar com moleculas pegadas a um dos sinais
  #,pelo que temos de tratar dela
  if "+" in elem_pol_split[0]: elem_pol_split = [elem_pol_split[0].replace("+",""),"+"]
  if "−" in elem_pol_split[0]: elem_pol_split = [elem_pol_split[0].replace("−",""),"−"]
  #nota2: a solução acima leva a que elemento seguido de vários números com polaridade
  #fiquem todos juntos, temos de tratar disso
  match = re.match(r"(.*?[0-9]+)([0-9])",elem_pol_split[0])
  if(match
     and 
     (elem_pol_split[1] == '+' or elem_pol_split[1] == '−')
    ):
    elem_pol_split = [match.group(1),match.group(2) + elem_pol_split[1]]
  #returnar
  return elem_pol_split



#processa a polaridade de um par separado de elemntos e polaridades
#sem ter polaridades separadas
def treat_polatiry(elem):
  pol_elem_treated = None
  #primeiro tratamos das que não têm simbolos de polaridade
  #, correspondendo a terem apenas um valor no split ou 
  #o seu segundo elemento ser ''
  if( (len(elem_pol_split) == 1) or (elem_pol_split[1] == '')):
    pol_elem_treated = [elem_pol_split[0],(0,'neutral')]
  #caso tenha + ou − no segundo elemento temos de separar a quantidade se existir
  elif("+" in elem_pol_split[1]):
    if(elem_pol_split[1] == '+'):
      pol_elem_treated = [elem_pol_split[0],(1,'positive')]
    else:
      #removemos o +
      pol_elem_treated = [ elem_pol_split[0],(int(elem_pol_split[1].replace("+","")),'positive')]
  elif("−" in elem_pol_split[1]): 
    if(elem_pol_split[1] == '−'):
      pol_elem_treated = [elem_pol_split[0],(1,'negative')]
    else:
      #removemos o −
      pol_elem_treated = [ elem_pol_split[0],(int(elem_pol_split[1].replace("−","")),'negative')]
  #returnar 
  return pol_elem_treated[0],pol_elem_treated[1]

  





#iniciar array de dados
element_data = {}

#iterar por cada ficheiro
for file in os.listdir(directory):
  filename = os.fsdecode(file)
  #ler ficheiro
  dataFromFile = open(dirStr + "/" + filename,"r").read()
  #obter dados json do documento
  jsonDataFromFile = json.loads(dataFromFile)
  #debug
  #print(jsonDataFromFile[0])

  #iterar por cada elemento do documento
  for i in range(len(jsonDataFromFile)):
    #obter elemento atual
    element = jsonDataFromFile[i]

    #obter dados da formula que queremos separar em elementos
    formula = element['Chemical formula']

    #inicializar dados do dicionário para esta molecula
    #dataFromMolecule = init_dict(element,formula)

    #separar pelo ·
    dt_split,dot_val = dot_split(formula)

    #debug
    #print(formula," -> ",(dt_split,dot_val))
    

    element_data[formula] = {}
    element_data[formula]['chemical formula'] = formula
    element_data[formula]['Synonyms'] = element["Synonyms"] if "Synonyms" in element.keys() else None
    element_data[formula]["CAS number"] = element["CAS number"] if "CAS number" in element.keys() else None
    element_data[formula]['dot-val'] = dot_val

    element_data[formula]['dot-subformulas'] = {}

    #lidar com cada elemento dentro do dot-split 
    for subdot in dt_split:
      #obter formula 
      cur_formula = subdot[1]
      #separar casos dos parenteses
      formula_split = re.sub(r'(\(.*?\)([0-9]+)?[+|−]*)',r" \1 ",cur_formula).split()
      
      element_data[formula]['dot-subformulas'][subdot[1]] = {}

      #debug
      #print(subdot," -> ",formula_split)
      
      
      element_data[formula]['dot-subformulas'][subdot[1]]['parenteses-subformulas'] = {}

      #lidar com cada elemento dentro das dot-subformulas
      for subfor in formula_split:
        #lidar com os parenteses e quantidades
        subfor_par_split = process_subfor(subfor)

        element_data[formula]['dot-subformulas'][subdot[1]]['parenteses-subformulas'][subfor] = {}
        element_data[formula]['dot-subformulas'][subdot[1]]['parenteses-subformulas'][subfor]['quant'] = subfor_par_split[1]

        #debug
        #print(subfor_par_split)

        #separamos o primeiro elemento da separação(subformula) por maiuscula
        capital_split = re.findall('[A-Z][^A-Z]*', subfor_par_split[0])

        #print(subfor_par_split[0]," -> ",capital_split)

        element_data[formula]['dot-subformulas'][subdot[1]]['parenteses-subformulas'][subfor]['subelems'] = {}


        #para cada elemento que separamos
        for elem in capital_split:


          #queremos fazer isto em 3 fazes:
          #1-separar as quantidades das polaridades 
          #2-tratar das polaridades
          #3-tratar das quantidades

          #1
          elem_pol_split = split_elems_and_pols(elem)

          #print(elem," -> ",elem_pol_split)

          #2)

          quant_ele,treated_pol = treat_polatiry(elem_pol_split)

          #print(elem," -> ",quant_ele,treated_pol)

          #3)
          #o processo é similar ao que foi feito antes para a polaridade,
          #mas neste caso apenas temos de separar o simbolo do número
          quant_elem_split = re.sub(r"([A-Z][^A-Z0-9]*)([0-9]+)?",r"\1#\2",quant_ele).split("#")
          #e colocamos o segundo elemento como inteiro se tiver lá número
          #ou 1 caso esteja a ""
          if(quant_elem_split[1] == ''): quant_elem_split[1] = 1
          quant_elem_split = (quant_elem_split[0],int(quant_elem_split[1]))


          elem_no_number = re.sub(r"[0-9]+",r"",quant_elem_split[0])


          element_data[formula]['dot-subformulas'][subdot[1]]['parenteses-subformulas'][subfor]['subelems'][elem_no_number] = {}          
          #print(elem," -> ",quant_elem_split,treated_pol)


          element_data[formula]['dot-subformulas'][subdot[1]]['parenteses-subformulas'][subfor]['subelems'][elem_no_number]['quant'] = quant_elem_split[1]
          element_data[formula]['dot-subformulas'][subdot[1]]['parenteses-subformulas'][subfor]['subelems'][elem_no_number]['pol'] = treated_pol



#pprint(element_data)







    #lidar com cada elemento dentro do split 
    #for sd_t in dt_split:
    #  sd = sd_t[1]
    #  #separar formula pelos parenteses
    #  formula_split = re.sub(r'(\(.*?\)[0-9]?)',r" \1 ",sd).split()
    #  #adicionar se não for []
    #  if formula_split != []:
    #    dataFromMolecule['dot-subformulas'].append(formula_split)
    #  #lidar com cada formula individualmente
    #  for sf in formula_split:
    #    if sf not in dataFromMolecule['elements']: 
    #      dataFromMolecule['elements'][sf] = []
    #    #tratar dos parenteses
    #    parenteses1 = sf.replace("(","")
    #    parenteses2 = parenteses1.split(")")
    #    dataFromMolecule['parenteses-subformulas'].append(parenteses2)
    #    #separar por maiusculas
    #    capital_split = re.findall('[A-Z][^A-Z]*', parenteses2[0])
    #    for elem in capital_split:
    #      #separa quantidade e elemento e colocar num par
    #      elementQuant_split = re.sub(r'([A-Z][a-z]*)([0-9]?)',r'\1&\2',elem).split('&')
    #      if(elementQuant_split[1]==''):
    #        elementQuant_split[1] = '1'
    #      if((len(parenteses2)>1) and (parenteses2[1]!='')):
    #        elementQuant_split[1] = str(int(elementQuant_split[1]) * int(parenteses2[1]))
    #      dataFromMolecule['elements'][sf].append((elementQuant_split[0],elementQuant_split[1]))
    #resultsArr.append(dataFromMolecule)


#pos-processamento dos dados
#for data in resultsArr:
#  #juntar submoleculas detetadas sob forma de objeto
#  molecules = data['parenteses-subformulas']
#  molsDict = {}
#  for mol in molecules:
#    #preprocessing
#    #remove - and + from names
#    if ("−" in mol[0]):
#      mol[0] = re.sub(r"([0-9])[0-9]",r"\1",mol[0])
#      mol[0] = re.sub(r"−",r"",mol[0])
#    if("+" in mol[0]):
#      mol[0] = re.sub(r"\+",r"",mol[0])
#    if(len(mol) == 1) or (mol[1] == ''):
#      molsDict[mol[0]] = 1
#    else:
#      molsDict[mol[0]] = int(mol[1])
#    #tratamento de caso especial: temos split por dot
#    if(len(data['dot-split'][0]) > 1) and (isinstance(data['dot-split'][0], list) ):
#      #minor processing
#      if(data['dot-split'][0][1][0] == ''):
#        data['dot-split'][0][1] = (str(1),data['dot-split'][0][1][1])
#
#  data['submolecules'] = molsDict
#
#  #juntar elementos iguais em termos de quantidades
#  elems = data['elements']
#  elemsList = {}
#  for formula in elems:
#    for elem in elems[formula]:
#      #some preprocessing
#      if (elem[1]== "−"):
#        elemp = (elem[0],"1","−")
#      elif (elem[1] == "+"):
#        elemp = (elem[0],"1","+")
#      elif "−" in elem[1]:
#        elemp = (elem[0],elem[1][0],elem[1][1:])
#      elif "+" in elem[1]:
#        elemp = (elem[0],elem[1][0],elem[1][1:])
#      else:
#        elemp = (elem[0],elem[1],"neutral")
#
#      #secound stage of preprocessing elements
#      if(elemp[2] == "−"):
#        elem2p = (elemp[0],int(elemp[1]),1,"negative")
#      elif(elemp[2] == "+"):
#        elem2p = (elemp[0],int(elemp[1]),1,"positive")    
#      elif "−" in elemp[2]:
#        elem2p = (elemp[0],int(elemp[1]),int(elemp[2][:-1]),"negative")    
#      elif "+" in elemp[2]:
#        elem2p = (elemp[0],int(elemp[1]),int(elemp[2][:-1]),"positive")    
#      else:
#        elem2p = (elemp[0],int(elemp[1]),0,"neutral")
#
#
#      #print(data,":",elem," -> ",elemp, " -> ",elem2p)
#
#      if not 'subelements' in data:
#        data['subelements'] = {}
#
#      elemsList[elem[0]] = elem2p
#
#    data['elements'][formula] = elemsList
#    
#    
#  #print(data)


resultsArr = [element_data[x] for x in element_data]


#colocar dados num ficheiro
fileRes = "/home/iamtruth/mestrado/2ºsemestre/PRC/projeto/data/from_wiki_tables_2/moleculas_tratado/molecule_data_2.json"
fileToWrite = open(fileRes,"w")
json.dump(resultsArr,fileToWrite, indent=2)

#terminamos
print("processing of dataset finished")
