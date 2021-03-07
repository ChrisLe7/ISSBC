# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 09:14:16 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        #Con QPushButton Creamos un Boton en la Ventana de Aplicación
        qbtn = QPushButton('Salir', self)
        #Con el evento clicked capturamos el evento y con connect podemos el estado abierto. 
        qbtn.clicked.connect(QApplication.instance().quit)
        #Con Resize podemos modificar el tamaño del Boton.
        qbtn.resize(qbtn.sizeHint())
        
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Boton Salir')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()