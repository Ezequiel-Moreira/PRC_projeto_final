<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    
    
    <xsl:output method="text" encoding="UTF-8"/>
    
    <xsl:template match="/">
        <xsl:apply-templates/>
    </xsl:template>
    
    
    <xsl:template match="root">        
        <xsl:apply-templates/>
    </xsl:template>
    
    <xsl:template match="row">
        <xsl:variable name="formulaMolecula" select="chemical-formula"/> 
        <xsl:variable name="valueDotMolecula" select="dot-val"/>
        <xsl:variable name="formulaMoleculaFixed" select="fixed-formula"/>
        <xsl:variable name="nameMolecula" select="Synonyms"/>
        <xsl:variable name="numberMolecula" select="CAS_number"/>
        <xsl:variable name="apos">"</xsl:variable>        
        <xsl:variable name="formulaMoleculaString" select="concat($apos,$formulaMolecula,$apos)"/>
        <xsl:variable name="valueDotMoleculaString" select="concat($apos,$valueDotMolecula,$apos)"/>
        <xsl:variable name="nameMoleculaString" select="concat($apos,$nameMolecula,$apos)"/>
        <xsl:variable name="numberMoleculaString" select="concat($apos,$numberMolecula,$apos)"/>
        
        ###  http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#mol_<xsl:value-of select="$formulaMoleculaFixed"/>
        :mol_<xsl:value-of select="$formulaMoleculaFixed"/> rdf:type owl:NamedIndividual ,
        :Molecule ;          
        :molecule_dot-val <xsl:value-of select="$valueDotMoleculaString"/>;
        :molecule_name <xsl:value-of select="$nameMoleculaString"/>;
        :molecule_number <xsl:value-of select="$numberMoleculaString"/>;
        :molecule_formula <xsl:value-of select="$formulaMoleculaString"/> .
        
        
        <xsl:apply-templates select="dot-subformulas">
            <xsl:with-param name="formulaMolecula" select="$formulaMoleculaFixed"/>
        </xsl:apply-templates>        
    </xsl:template>
    
    
    
    
    <xsl:template match="dot-subformulas">            
        <xsl:param name="formulaMolecula" />
        <xsl:variable name="formulaDotMolecula" select="name"/> 
        <xsl:variable name="formulaDotFixed" select="fixed-name"/>
        <xsl:variable name="dot-id" select="generate-id()"/>
        <xsl:variable name="apos">"</xsl:variable>        
        <xsl:variable name="formulaDotString" select="concat($apos,$formulaDotMolecula,$apos)"/>
           
            
        ###  http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#dSMol_<xsl:value-of select="$formulaDotFixed"/>_<xsl:value-of select="$dot-id"/>
        :dSMol_<xsl:value-of select="$formulaDotFixed"/>_<xsl:value-of select="$dot-id"/> rdf:type owl:NamedIndividual ,
        :DotSubMolecule ;
        :dotSubMolecule_name <xsl:value-of select="$formulaDotString"/> .
            
            
        :mol_<xsl:value-of select="$formulaMolecula"/>  :hasDotSubMolecule :dSMol_<xsl:value-of select="$formulaDotFixed"/>_<xsl:value-of select="$dot-id"/> .
          
        :dSMol_<xsl:value-of select="$formulaDotFixed"/>_<xsl:value-of select="$dot-id"/> :isDotSubMoleculeOf  :mol_<xsl:value-of select="$formulaMolecula"/> .
            
        <xsl:apply-templates select="parenteses-subformulas">
            <xsl:with-param name="formulaDotMolecula" select="$formulaDotFixed"/>    
            <xsl:with-param name="dot-id" select="$dot-id"/>
        </xsl:apply-templates>            
        
    </xsl:template>
    
    
    
    
    
    
    <xsl:template match="parenteses-subformulas">             
        <xsl:param name="formulaDotMolecula" />
        <xsl:param name="dot-id"/>
        <xsl:variable name="formulaParentesesMolecula" select="name"/> 
        <xsl:variable name="quantidadeParentesesMolecula" select="quant"/>
        <xsl:variable name="formulaParentesesFixed" select="fixed-name"/>
        <xsl:variable name="parenteses-id" select="generate-id()"/>
        <xsl:variable name="apos">"</xsl:variable>      
        <xsl:variable name="formulaParentesesString" select="concat($apos,$formulaParentesesMolecula,$apos)"/>           
            
            
        ###  http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#pSMol_<xsl:value-of select="$formulaParentesesFixed"/>_<xsl:value-of select="$parenteses-id"/>
        :pSMol_<xsl:value-of select="$formulaParentesesFixed"/>_<xsl:value-of select="$parenteses-id"/> rdf:type owl:NamedIndividual ,
        :ParentesesSubMolecule ;
        :parentesesSubMolecule_name <xsl:value-of select="$formulaParentesesString"/> ;
        :parentesesSubMolecule_quant <xsl:value-of select="$quantidadeParentesesMolecula"/> .
            
            
        :dSMol_<xsl:value-of select="$formulaDotMolecula"/>_<xsl:value-of select="$dot-id"/> :hasParentesesSubMolecule :pSMol_<xsl:value-of select="$formulaParentesesFixed"/>_<xsl:value-of select="$parenteses-id"/> .
            
        :pSMol_<xsl:value-of select="$formulaParentesesFixed"/>_<xsl:value-of select="$parenteses-id"/> :isParentesesSubMoleculeOf :dSMol_<xsl:value-of select="$formulaDotMolecula"/>_<xsl:value-of select="$dot-id"/>  .
            
        <xsl:apply-templates select="subelems">            
            <xsl:with-param name="formulaParentesesMolecula" select="$formulaParentesesFixed"/>
            <xsl:with-param name="parenteses-id" select="$parenteses-id"/>
        </xsl:apply-templates>            
        
    </xsl:template>
    
    
    
    
    
    
    <xsl:template match="subelems">             
        <xsl:param name="parenteses-id"/>
        <xsl:param name="formulaParentesesMolecula" />
        <xsl:variable name="formulaElemento" select="name"/> 
        <xsl:variable name="quantidadeElemento" select="quant"/>
        <xsl:variable name="polaridadeElemento" select="pol"/> 
        <xsl:variable name="quantidadePolaridadeElemento" select="pol-quant"/>
        <xsl:variable name="apos">"</xsl:variable>      
        <xsl:variable name="formulaElementoString" select="concat($apos,$formulaElemento,$apos)"/> 
        <xsl:variable name="polaridadeElementoString" select="concat($apos,$polaridadeElemento,$apos)"/> 
            
            
        ###  http://www.semanticweb.org/iamtruth/ontologies/2019/4/final_project#eQ_<xsl:value-of select="$formulaElemento"/>_<xsl:value-of select="$quantidadeElemento"/>_<xsl:value-of select="$quantidadePolaridadeElemento"/>_<xsl:value-of select="$polaridadeElemento"/>
        :eQ_<xsl:value-of select="$formulaElemento"/>_<xsl:value-of select="$quantidadeElemento"/>_<xsl:value-of select="$quantidadePolaridadeElemento"/>_<xsl:value-of select="$polaridadeElemento"/> rdf:type owl:NamedIndividual ,
        :ElementQuantity ;              
        :hasElementinElementQuantity :e_<xsl:value-of select="$formulaElemento"/> ;              
        :elementQuantity_name <xsl:value-of select="$formulaElementoString"/> ;
        :elementQuantity_pol <xsl:value-of select="$polaridadeElementoString"/>;
        :elementQuantity_pol-quant <xsl:value-of select="$quantidadePolaridadeElemento"/> ;
        :elementQuantity_quant <xsl:value-of select="$quantidadeElemento"/> .
            
            
        :pSMol_<xsl:value-of select="$formulaParentesesMolecula"/>_<xsl:value-of select="$parenteses-id"/> :hasElementQuantity :eQ_<xsl:value-of select="$formulaElemento"/>_<xsl:value-of select="$quantidadeElemento"/>_<xsl:value-of select="$quantidadePolaridadeElemento"/>_<xsl:value-of select="$polaridadeElemento"/> .
            
        :eQ_<xsl:value-of select="$formulaElemento"/>_<xsl:value-of select="$quantidadeElemento"/>_<xsl:value-of select="$quantidadePolaridadeElemento"/>_<xsl:value-of select="$polaridadeElemento"/> :isElementQuantityOf  :pSMol_<xsl:value-of select="$formulaParentesesMolecula"/>_<xsl:value-of select="$parenteses-id"/> .
            
        :e_<xsl:value-of select="$formulaElemento"/> :isElementinElementQuantity :eQ_<xsl:value-of select="$formulaElemento"/>_<xsl:value-of select="$quantidadeElemento"/>_<xsl:value-of select="$quantidadePolaridadeElemento"/>_<xsl:value-of select="$polaridadeElemento"/> .
            
        
    </xsl:template>
    
    
</xsl:stylesheet>