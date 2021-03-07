# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 08:48:41 2021

@author: ChrisLe
"""

from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication)

from PyQt5.QtGui import QColor

import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        
        self.col = QColor (0,0,0)
        
        
        botonRojo = QPushButton ('Rojo',self)
        botonRojo.setCheckable (True)
        botonRojo.move(10,10)
        
        botonRojo.clicked[bool].connect(self.setColor)
        
        botonVerde = QPushButton('Verde', self)
        botonVerde.setCheckable (True)
        botonVerde.move(10,60)
        
        botonVerde.clicked[bool].connect(self.setColor)
        
        botonAzul = QPushButton ('Azul', self)
        botonAzul.setCheckable (True)
        botonAzul.move (10,110)
        
        botonAzul.clicked[bool].connect(self.setColor)
        
        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        
     
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Toggle button')
        self.show()
    
    
    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Rojo":
            self.col.setRed(val)
        elif source.text() == "Verde":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()