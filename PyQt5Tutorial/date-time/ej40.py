# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:40:03 2021

@author: ChrisLe
"""

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print(f'Hoy:', now.toString(Qt.ISODate))
print(f'Añadiendo 12 dias: {now.addDays(12).toString(Qt.ISODate)}')
print(f'Quitando 22 dias: {now.addDays(-22).toString(Qt.ISODate)}')

print(f'Añadiendo 50 segundos: {now.addSecs(50).toString(Qt.ISODate)}')
print(f'Añadiendo 3 meses: {now.addMonths(3).toString(Qt.ISODate)}')
print(f'Añadiendo 12 años: {now.addYears(12).toString(Qt.ISODate)}')

