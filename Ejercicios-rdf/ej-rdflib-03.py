# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:36:58 2021

@author: ChrisLe
"""

from rdflib import Namespace, Literal, URIRef
from rdflib.graph import Graph, ConjunctiveGraph
from rdflib.plugins.memory import IOMemory

if __name__=='__main__':
    ns = Namespace("http://love.com#") #Cogemos el espacio de nombres con el que trabajaremos
    mary = URIRef("http://love.com/lovers/mary#") #Obtenemos la referencia del sujeto con el que vamos a trabajar
    john = URIRef("http://love.com/lovers/john#")
    cmary=URIRef("http://love.com/lovers/mary#")
    cjohn=URIRef("http://love.com/lovers/john#")
    store = IOMemory() #Reservamos memoria para nuestro grafo
    g = ConjunctiveGraph(store=store) #Creamos un nuevo grafo de conjuntos donde iremos almacenando los grafos de cada sujeto
    g.bind("love",ns) #Liga a la etiqueta love el espacio de nombre ns
    gmary = Graph(store=store, identifier=cmary) #Creamos un grafo para Mary para así almanenar sus propiedades
    gmary.add((mary, ns['hasName'], Literal("Mary")))
    gmary.add((mary, ns['loves'], john))
    gjohn = Graph(store=store, identifier=cjohn)
    gjohn.add((john, ns['hasName'], Literal("John")))
    
    #Una vez creados los grafos tanto para Mary como para John Mostraremos el contenido

    print ('#Contenido del grafo de Conjuntos')
    print
    print 
    for c in g.contexts():
        print("-- %s " % c)
    print 
    print ('#Contenido del Grafo de John en notación N3')
    print(gjohn.serialize(format='n3'))
    print("===================")
    print ('#Contenido del Grafo de John en notación N3')

    print(gmary.serialize(format='n3'))
    print("===================")
    #full graph
    print(g.serialize(format='n3'))
    # query the conjunction of all graphs
    print ('Mary loves:')
    for x in g[mary : ns.loves/ns.hasName]: #La forma que realizamos la query es indicando que deseamos de los valores del predicado ns.loves queremos unicamente su propiedad ns.hasName
        print (x)