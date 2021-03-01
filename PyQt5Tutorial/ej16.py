# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:51:27 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example (QWidget):
    
    
    def __init__ (self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        names = ['Cls','Bck', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6','*',
                '1','2','3', '-',
                '0', '.', '=', '+']
        
        #Preguntar Esta linea de código
        #Respuesta: Ya lo he entendido, lo que hacemos con esta linea es hacer
        # un doble bucle para recorrer la matrix : ya que la matrix tiene 5 filas y 4 columnas.
        
        positions = [(i, j) for i in range(5) for j in range(4)]
        
        #La función zip lo que hace es coger varias tuplas y te devuelve una a una sus posiciones juntas.
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()