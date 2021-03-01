# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:04:23 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout 

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
     
        opcion1 = QLabel ('Pulse Esc para salir')
        opcion2 = QLabel ('Pulse 0 para ampliar la ventana')
        opcion3 = QLabel ('Pulse 1 para reducir el tamaño de la ventana')
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(opcion1, 1, 0)
        grid.addWidget(opcion2, 2, 0)
        grid.addWidget(opcion3, 3, 0)
        
        self.setLayout(grid)  
        self.setGeometry(350, 350, 500, 300)
        self.setWindowTitle('Capturardora de Eventos')
        self.show()
        
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_0 :
            self.resize(800, 600)
        elif e.key () == Qt.Key_1 :
            self.resize(200, 100)
    
    
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
