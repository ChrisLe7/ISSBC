# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:55:17 2021

@author: ChrisLe
"""

import rdflib

g = rdflib.Graph()
result = g.parse("http://www.w3.org/People/Berners-Lee/card")  #De esta forma agregamos el contenido al grafo


print("graph has %s statements." % len(g)) #Mostramos el número de elementos de los que se compone el grafo
# prints graph has 79 statements.


#Posteriormente mostraremos cada uno de los sujetos 

for subj, pred, obj in g:
    print ('--->', subj)
    
    if (subj, pred, obj) not in g:
       raise Exception("It better be!")

print ("------------------------------")


print("Contenido del grafo en notación N3")

s = g.serialize(format='n3')

print (s)
