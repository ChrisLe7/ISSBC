# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:23:25 2021
Este ejercicio es igual al de ej-rdflib-t-06.py
@author: ChrisLe
"""

from rdflib import Graph
from rdflib import URIRef, BNode, Literal, Namespace
from rdflib.namespace import RDF, FOAF

n = Namespace("http://example.org/people/")

n.bob # = rdflib.term.URIRef(u'http://example.org/people/bob')
n.eve # = rdflib.term.URIRef(u'http://example.org/people/eve')

bob = URIRef("http://example.org/people/Bob")
linda = BNode() # a GUID is generated NODO BLANCO

name = Literal('Bob') # passing a string
age = Literal(24) # passing a python int
height = Literal(76.5) # passing a python float

#Ver las variables creadas : ej-rdflib-t-04
print (name)
print (age)
print (height)



g = Graph()

g.add( (bob, RDF.type, FOAF.Person) )
g.add( (bob, FOAF.name, name) )
g.add( (bob, FOAF.knows, linda) )
g.add( (linda, RDF.type, FOAF.Person) )
g.add( (linda, FOAF.name, Literal('Linda') ) )

print 
print (g.serialize(format='turtle'))
print 
print (g.serialize(format='xml'))

print 
print (g.serialize(format='n3'))

print

print (n.bob, n.eve)

#print RDF.type

#print FOAF.knows


#Parte del ejemplo ej-rdflib-t-07.py
g.add( ( bob, FOAF.age, Literal(42) ) )
print ("Bob is ", g.value( bob, FOAF.age ))
# prints: Bob is 42

g.set( ( bob, FOAF.age, Literal(43) ) ) # replaces 42 set above
print ("Bob is now ", g.value( bob, FOAF.age ))
# prints: Bob is now 43




#Parte del ejemplo ej-rdflib-t-08.py

'''
Removing Triples

Similarly, triples can be removed by a call to remove():

Graph.remove()[source]

    Remove a triple from the graph

    If the triple does not provide a context attribute, removes the triple from all contexts.

When removing, it is possible to leave parts of the triple unspecified (i.e. passing None), this will remove all matching triples:
'''
g.remove( (bob, None, None) ) # remove all triples about bob

print (g.serialize(format='turtle'))

'''

La salida es: 

@prefix ns1: <http://xmlns.com/foaf/0.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ns1:Person ;
    ns1:name "Linda" .

'''