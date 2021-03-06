# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:45:44 2021

@author: ChrisLe
"""

from PyQt5.QtCore import QDate, Qt

borodino_battle = QDate(1812, 9, 7)
slavkov_battle = QDate(1805, 12, 2)

now = QDate.currentDate()

j_today = now.toJulianDay()
j_borodino = borodino_battle.toJulianDay()
j_slavkov = slavkov_battle.toJulianDay()

d1 = j_today - j_slavkov
d2 = j_today - j_borodino

print(f'Días desde la Batalla de Slavkov: {d1}')
print(f'Días desde la Batalla de Borodino : {d2}')
