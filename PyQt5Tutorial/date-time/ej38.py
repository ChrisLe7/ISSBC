# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:39:00 2021

Ejercicios de la Sección de PyQt5 date and time
@author: ChrisLe
"""

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

d = QDate(1945, 5, 7)

print(f'Número de días en este mes: {d.daysInMonth()}')
print(f'Número de días en este año: {d.daysInYear()}')