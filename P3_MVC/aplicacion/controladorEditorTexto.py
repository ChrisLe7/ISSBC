# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:07:01 2021

@author: ChrisLe
"""

from aplicacion import modeloEditorTexto as modelo

def abrirArchivo(direccion):
    return modelo.abrirArchivo(direccion)

def guardarArchivo(direccion, datos):
    modelo.guardarArchivo(direccion, datos)
    
def listarDirectorio (direccion):
    return modelo.listarDirectorio(direccion)