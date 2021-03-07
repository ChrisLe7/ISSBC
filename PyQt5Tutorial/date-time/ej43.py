# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:44:45 2021

@author: ChrisLe
"""

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print('Fecha del Calendario Gregoriana de hoy:', now.toString(Qt.ISODate))
print('Fecha del Calendario Juliano de hoy:', now.toJulianDay()) 