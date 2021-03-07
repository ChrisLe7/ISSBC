# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:40:29 2021

@author: ChrisLe
"""

from PyQt5.QtCore import QDateTime, QTimeZone, Qt

now = QDateTime.currentDateTime()

print(f'Zona Horaria: {now.timeZoneAbbreviation()}')

if now.isDaylightTime():
    print(f'La fecha actual cae en horario de verano')
else:
    print(f'La fecha actual no cae en horario de verano')
    
    