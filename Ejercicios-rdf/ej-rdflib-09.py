# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:25:35 2021

@author: ChrisLe
"""

from rdflib.namespace import OWL, RDF, RDFS
from rdflib import Graph, Literal, Namespace, URIRef

# Construct the linked data tools namespace
LDT   = Namespace("http://www.linkeddatatools.com/plants#")

# Create the graph
graph = Graph()

# Create the node to add to the Graph
Plant = URIRef(LDT["Planttype"])

# Add the OWL data to the graph
graph.add((Plant, RDF.type, OWL.Class))
graph.add((Plant, RDFS.subClassOf, OWL.Thing))
graph.add((Plant, RDFS.label, Literal("The plant type")))
graph.add((Plant, RDFS.comment, Literal("The class of all plant types")))

# Bind the OWL and LDT name spaces
graph.bind("owl", OWL)
graph.bind("ldt", LDT)

print ('Formato XML')
print (' ')
print (graph.serialize(format='xml'))
print (' ')
print (' ')
print (' ')
print (' ')
print ('Formato N3')

print (graph.serialize(format='n3'))

print (' ')
print (' ')
print (' ')


print

print ('otra forma de presentar')
print (graph.serialize(format='pretty-xml'))

graph.serialize('sal.owl',format='pretty-xml')