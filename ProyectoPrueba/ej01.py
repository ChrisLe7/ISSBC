# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:38:25 2021

@author: ChrisLe
"""

# La variable __name__ nos permite identificar si el script es el programa principal o no
def suma(a,b):
    s = a+b 
    return s

def producto (a,b):
    '''

    Parameters
    ----------
    a : Numbers
        DESCRIPTION.
    b : Numbers
        DESCRIPTION.

    Returns
    -------
    Producto de a y b.

    '''
    s = a * b
    return s

#Función para recorrer una lista
def ejLista01(li):
    '''
    Parameters
    ----------
    li : Lista
        Mostrará la Lista li.

    Returns
    -------
    None.
    '''
    for i in li :
        print (i)
    
#Función para recorrer una lista
def ejLista02(li):
    for i in list(range(len(li))):        
        print (i,li[i])

#Función para recorrer un string
def cadena1 (cad):
    for i in cad:
        print (i)
        

if __name__ == '__main__':
    ej=4
    if ej==1:
        #print (__name__)
        print(suma(2,3))
        #print ('Hola')
    elif ej==2:
        ejLista01([1,4,5,'hola'])
    elif ej==3:
        ejLista02([1,4,5,'hola'])
    elif ej==4:
        cadena1('Hola')
        
