# -*- coding: utf-8 -*-
"""
Created on Sat May  1 08:38:42 2021

@author: ChrisLe
"""

import rdflib
from rdflib import Graph,Namespace
from rdflib import plugin
FOAF = Namespace("http://xmlns.com/foaf/0.1/")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")


 
my_data ='''
                @prefix foaf:  <http://xmlns.com/foaf/0.1/> .

                _:a  foaf:name   "Alice" .
                _:b  foaf:name   "Bob" .


     '''
g = Graph()
g.parse(data=my_data, format="n3")
    #print ('result',result)
    #print (len(g))
print (g.serialize(format='xml'))
    #print g.serialize(format='n3')


#2.4 Blank Node Labels in Query Results
def q1():
          
    query='''    
                 PREFIX foaf:   <http://xmlns.com/foaf/0.1/>
                 
                SELECT ?x ?name
                WHERE  { ?x foaf:name ?name }



''' 
    result=g.query(query)
    #print (result)
    for row in result:
        #print (row)
        print ("%s es %s" % tuple(row))
        

if __name__ == '__main__':

    if True:
        print ('Consulta q1')
        print ()
        q1()
 