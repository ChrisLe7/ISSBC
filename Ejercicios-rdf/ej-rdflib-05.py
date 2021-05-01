# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:01:45 2021

@author: ChrisLe
"""

from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF

g = Graph() #De esta forma creamos un Nodo Blanco, el cual no posee refencia ninguna

# Creamos un nodo, el que usaremos como referencia de donna 
donna = BNode()

# Añadimos las tripletas al grafo.
g.add( (donna, RDF.type, FOAF.Person) )
g.add( (donna, FOAF.nick, Literal("donna", lang="foo")) )
g.add( (donna, FOAF.name, Literal("Donna Fales")) )
g.add( (donna, FOAF.mbox, URIRef("mailto:donna@example.org")) )

print ('# Recorremos el grafo tripleta por tripleta, indicando sujeto, predicado, objeto.')
print("--- printing raw triples ---")
for s, p, o in g:
    print(("Sujeto " + s ,"Predicado " + p,"Objeto " + o))

print ()

print ('# For each foaf:Person in the store print out its mbox property.')

print("--- printing mboxes ---")
for person in g.subjects(RDF.type, FOAF.Person):
    for mbox in g.objects(person, FOAF.mbox):
        print ('mbox: ',)
        print(mbox)

 
print ('# Asignamos los preficos a los espacios de nombres para facilitar la lectura')
g.bind("dc", DC)
g.bind("foaf", FOAF)
print ("==========================")
print( g.serialize(format='n3') )