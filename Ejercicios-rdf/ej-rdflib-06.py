# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:08:17 2021
Este ejercicio lo unico que hace es ofrecer otra forma de mostrar el grafo
@author: ChrisLe
"""

import rdflib
import pprint

#from rdflib import Graph

g = rdflib.Graph()
g.parse("demo.nt", format="nt") 

print (len(g)) # prints 2

for stmt in g:
    pprint.pprint(stmt)

# prints :
(rdflib.term.URIRef('http://bigasterisk.com/foaf.rdf#drewp'),
 rdflib.term.URIRef('http://example.com/says'),
 rdflib.term.Literal(u'Hello world'))
(rdflib.term.URIRef('http://bigasterisk.com/foaf.rdf#drewp'),
 rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'),
 rdflib.term.URIRef('http://xmlns.com/foaf/0.1/Person'))
