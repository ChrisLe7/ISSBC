# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:23:15 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example (QWidget):
    
    #Definimos el constructor
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Primero crearemos unas etiquetas de texto para 
        #   su posterior posicionamiento
        
        label1 = QLabel('Texto 1',self)
        label2 = QLabel('Texto 2',self)
        label3 = QLabel('Texto 3',self)
        
        #Posicionaremos las etiquetas mediante la funcion move
        #move (coordenada_x,coordenada_y)
        label1.move(10,15)
        label2.move(40,45)
        label3.move(20,75)
        
        #Una vez hecho esto ajustaremos el tamaño de nuestra ventana principal
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Ventana Posicionamiento Absoluto')
        self.show()
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()