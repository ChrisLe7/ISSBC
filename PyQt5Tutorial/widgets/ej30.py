# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:33:47 2021

@author: ChrisLe
"""

from PyQt5.QtWidgets import (QWidget, QProgressBar, QPushButton, QApplication)

from PyQt5.QtCore import QBasicTimer

import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        
        
    def initUI(self):

        self.barraProgreso = QProgressBar(self)
        self.barraProgreso.setGeometry (30,40,200,25)
        
        self.boton = QPushButton ('Iniciar', self)
        
        self.boton.move (40,80)
        
        self.boton.clicked.connect(self.doAction)

        #Con este objeto realizaremos el conteo del tiempo para
        # la barra de progreso.        
        self.timer = QBasicTimer()
        
        self.step = 0 
        
        self.setGeometry (300,300, 280, 170)
        
        self.setWindowTitle ('QProgessBar')
        self.show()
        
    def timerEvent (self, e):
        
        if self.step >= 100:
            self.timer.stop()
            self.boton.setText('Acabado')
            return
        
        self.step = self.step + 1 
        self.barraProgreso.setValue(self.step)
    
    def doAction(self):
        
        if self.timer.isActive():
            self.timer.stop()
            self.boton.setText('Iniciar')
            
        else:
            self.timer.start(100, self)
            self.boton.setText('Parar')
            
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
    