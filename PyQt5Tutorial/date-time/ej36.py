# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:35:18 2021

Ejercicios de la Sección de PyQt5 date and time
@author: ChrisLe
"""

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print('Formato ISO: ' + now.toString(Qt.ISODate))
print('Formato Fecha Extendida: ' + now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()

print('Formato Fecha Objeto QDateTime: ' + datetime.toString())

time = QTime.currentTime()

print('Formato Hora Objeto QTime' + time.toString(Qt.DefaultLocaleLongDate))