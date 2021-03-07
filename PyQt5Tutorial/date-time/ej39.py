# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:39:40 2021

@author: ChrisLe
"""

from PyQt5.QtCore import QDate

xmas1 = QDate(2019, 12, 24)
xmas2 = QDate(2020, 12, 24)

now = QDate.currentDate()

dayspassed = xmas1.daysTo(now)
print(f'{dayspassed} días desde la última Navidad')

nofdays = now.daysTo(xmas2)
print(f'Faltan {nofdays} días antes de la próxima Navidad')

