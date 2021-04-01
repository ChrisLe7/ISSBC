# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:06:29 2021

@author: ChrisLe
"""

import os


def abrirArchivo(direccion):

    fichero = open(direccion, 'r')
    with fichero:
        data = fichero.read()
        fichero.close()
        return data
        
def guardarArchivo(direccion, datos):
       
    if direccion != '':
       
       fichero =  open(direccion, 'w')
       fichero.write(datos)
       fichero.close()


def listarDirectorio (direccion):
    
    #Con listdir devolvemos el listado completo de archivos en el directorio pasado.
    # Posteriormente con endswitch limitamos las extensiones que deseamos mostrar
    return [fname for fname in os.listdir(direccion) if fname.endswith(('.txt', '.py'))]     