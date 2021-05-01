# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:10:58 2021

Este ejercicio es igual al de ej-rdflib-t-05.py
@author: ChrisLe
"""

from rdflib import URIRef, BNode, Literal, Namespace, Graph
from rdflib.namespace import RDF, FOAF


bob = URIRef("http://example.org/people/Bob") #Obtenemos la referencia del sujeto
linda = BNode() # a GUID is generated


name = Literal('Bob') # passing a string
age = Literal(24) # passing a python int
height = Literal(76.5) # passing a python float

print (bob)
print (name)

n = Namespace("http://example.org/people/")

n.bob # = rdflib.term.URIRef(u'http://example.org/people/bob')
n.eve # = rdflib.term.URIRef(u'http://example.org/people/eve')

print ('n.bob, n.eve: ', n.bob, n.eve)

print ('RDF.type: ', RDF.type)
print 

print ('FOAF.knows: ', FOAF.knows)

g=Graph()
g.add((linda,n.loves,bob))

print("Mostramos el contenido del grafo en XML")
print( g.serialize(format='xml') )

print("Mostramos el contenido del grafo en N3")
print( g.serialize(format='n3') )
