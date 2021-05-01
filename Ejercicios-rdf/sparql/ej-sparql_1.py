# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 09:46:06 2021

@author: ChrisLe
"""

import rdflib
if __name__=='__main__':
    g = rdflib.Graph()
    g.load("foaf.rdf") #Con esto cargaremos el contenido del fichero foad.rdf en el grafo.
    # the QueryProcessor knows the FOAF prefix from the graph
    # which in turn knows it from reading the RDF/XML file
    for row in g.query('select ?s where { [] foaf:knows ?s .}'):
        print (row.s)
# or row["s"]
# or row[rdflib.Variable("s")]