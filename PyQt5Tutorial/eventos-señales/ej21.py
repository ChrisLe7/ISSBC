# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:44:04 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Example (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI (self):
        boton1 = QPushButton ("Boton 1", self)
        boton1.move (30,50)

        boton2 = QPushButton ("Boton 2", self)
        boton2.move (150,50)
        
        boton1.clicked.connect(self.buttonClicked)
        boton2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(500,500,750,450)
        self.setWindowTitle("Ventana, envio de Eventos")
        self.show()
        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' fue precionado.')
        
def main ():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
        