# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:44:22 2021

@author: ChrisLe
"""

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

unix_time = now.toSecsSinceEpoch() 
print(unix_time)

d = QDateTime.fromSecsSinceEpoch(unix_time)
print(d.toString(Qt.ISODate))