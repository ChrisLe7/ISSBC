# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 08:45:04 2021

@author: ChrisLe
"""
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example (QWidget):
        def __init__(self):
            super().__init__()
            
            self.initUI()
            
        def initUI(self):
            #qbutton será nuestro boton de nuestra Ventana
            qbutton = QPushButton('Quitar', self)
            #Asignamos al evento de Clickar la acción de Eliminar 
            #la instancia de la Ventana
            qbutton.clicked.connect(QApplication.instance().quit)
            #sizeHint nos devolvera un tamaño valido para el Widgets
            qbutton.resize(qbutton.sizeHint())
            qbutton.move (50,50)
            
            #Ahora configuraremos el tamaño de la ventana y su posición
            self.setGeometry(300, 300, 350, 250)
            self.setWindowTitle('Boton de Cerrar')
            #Con show creara el Widget en memoria y posteriormente lo mostrara 
            # por pantalla.
            self.show()
            
def main():
    app=QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  


if __name__=='__main__':
    main()








              