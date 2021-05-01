# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 08:28:28 2021

@author: ChrisLe
"""

from rdflib import Graph # Importamos la clase Graph de rdflib
from rdflib import Namespace # Namespace nos servira para almacernar nuestros espacios de nombre
from rdflib import Literal # Nos permitira almacenar una variable como un literal (Valor Constante)

FOAF = Namespace("http://xmlns.com/foaf/0.1/") # De esta forma almacenamos el nombre de dominio para hacermos más facil su uso
EX = Namespace("http://example.org/foovocab#")


def main ():
    # Creamos el grafo
    
    s = Graph()
    
    #Ahora asignaremos un prefijo a cada uno de los espacios de nombre en el grafo
    
    s.bind('dc',EX) #Mediante bind podemos hacerlo
    #bind (prefijo, espacioNombre)
    
    s.bind('foaf',FOAF)
    
    #Ahora leeremos del archivo rdf, para ello usaremos parse
    
    s.parse ('exe2.rdf')
    
    #Ahora podemos mostrar la información que contiene el grafo
    
    print('El Contendido del grafo en formato XML seria: ')
    print ("------------------------------")
    print (s.serialize(format = "xml")) #Con serializable transformamos el contenido del grafo al formato deseado

    #Quién es la secretaria de Bob?
    
    print ("------------------------------")

    # Encuentra un tipo llamado Bob...
    print ('Encuentra un indiciduo llamado Bob...')
    for who in s.subjects(FOAF["name"], Literal("Bob")):#sujetos con este predicado y este objeto
        bob = who
        print  ('El individuo es:',who)
        print ()
        
        
    print ('===============================')
    # who is secretlyStalking bob?
    print ( '  Quien es la secretaria de  bob?')
    
    for who in s.subjects(EX["secretlyStalking"], bob):
        for n in s.objects(who, FOAF["name"]):
            print ( n, "is secretlyStalking Bob!")

if __name__ == '__main__':
    main()
    
    