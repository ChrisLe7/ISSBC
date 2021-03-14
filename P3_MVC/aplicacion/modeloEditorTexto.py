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
        return data
        
def guardarArchivo(direccion, datos):
       
    if direccion != '':
       
       fichero =  open(direccion, 'w')
       fichero.write(datos)
       fichero.close()


def listarDirectorio (direccion):
    contenido = os.listdir(direccion)
    return contenido