# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:37:06 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication

class Example(QWidget):
    
    #Definimos el Constructo
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        #Creamos un boton para la acción OK y otro para Cancelar
        
        okButton = QPushButton("OK")
        cancelarButton = QPushButton("Cancelar")
        okButton.clicked.connect(self.Ok)
        cancelarButton.clicked.connect(self.Cancelar)
        #Ahora crearemos las cajas de posicionamiento
        
        hBox = QHBoxLayout()
        #Con addStretch lo que hacemos es colocar un pequeño espacio entre los Widgets
        hBox.addStretch(2)
        #Añadimos los Widgets al layout
        hBox.addWidget(okButton)
        hBox.addWidget(cancelarButton)
        
        vBox = QVBoxLayout()
        vBox.addStretch(2)
        vBox.addLayout(hBox)
        
        self.setLayout(vBox)
        
        #Una vez hecho esto ajustaremos el tamaño de nuestra ventana principal
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Ventana Posicionamiento Mediante BoxLayout')
        self.show()
        
    def Ok(self):
        print ("Hola, ha pulsado OK")
    
    def Cancelar (self):
        print ("Hola ha Pulsado Cancelar")
        

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()