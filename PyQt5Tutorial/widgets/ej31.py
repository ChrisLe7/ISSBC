# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:45:09 2021

@author: ChrisLe
"""

from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QLabel, QApplication, QVBoxLayout)

from PyQt5.QtCore import QDate

import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        
    def initUI (self):
        
        vBox = QVBoxLayout (self)
        
        calendario = QCalendarWidget (self)
        calendario.setGridVisible(True)
        calendario.clicked[QDate].connect(self.showDate)
        
        vBox.addWidget (calendario)
        
        self.label = QLabel (self)
        fecha = calendario.selectedDate()
        self.label.setText(fecha.toString())
        vBox.addWidget (self.label)
        self.setLayout (vBox)
        
        self.setGeometry (300,300,350, 300)
        
        self.setWindowTitle ('Calendario')
        self.show()
        
    def showDate(self,date):
        self.label.setText(date.toString())

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()