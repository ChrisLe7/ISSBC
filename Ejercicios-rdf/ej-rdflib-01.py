# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:22:29 2021

Realización del Ejercicio 01 de los ejemplos de RDFlib

@author: ChrisLe
"""
import rdflib # De esta forma importamos la librería rdflib

g = rdflib.Graph() # Creamos una instancia de grafo

g.load('http://dbpedia.org/resource/Semantic_Web')


print ("------------------------------")
print("Mostraremos el contenido del grafo de forma serializable")

print (g.serialize(format="xml")) #Muestra un grafo en formato xml

print ("------------------------------")
print("Mostraremos el contenido del grafo mostrando el Sujeto + Predicado + Valor")

for s,p,o in g:
    print(s,p,o)
    pass