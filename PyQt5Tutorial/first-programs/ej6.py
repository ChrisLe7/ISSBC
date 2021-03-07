# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:44:25 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication

class Example (QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.resize(450,250)
        #Nosotros creamos nuestro propio método para centrar el Widget
        self.center()
        self.setWindowTitle('Ventana Centrada')
        self.show()
        
    def center(self):
        #frameGeometry nos da los tamaños de la ventana  
        qr = self.frameGeometry()
        #Posteriormente con QDesktopWidget(), conseguimos  la geometria disponible de nuestra pantalla.
        cp = QDesktopWidget().availableGeometry().center()
        #Y despues de haber obtenido el punto central recolocamos la ventana con moveCenter. 
        #la cual centrara el Widget respecto a ese punto.
        qr.moveCenter(cp)
        self.move(qr.topLeft())
     
    
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    