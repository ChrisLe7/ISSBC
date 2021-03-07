# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:37:58 2021


Ejercicios de la Sección de PyQt5 date and time

@author: ChrisLe
"""

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print('Fecha Local: ', now.toString(Qt.ISODate))
print('Fecha Universal: ', now.toUTC().toString(Qt.ISODate))

#Con la opción de de antes de las comillas permitimos añadir variables a nuestra cadena de texto.
 
print(f'La diferencia de fechas es: {now.offsetFromUtc()} segundos')

