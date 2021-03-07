# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 08:46:41 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class VentanaGrid (QWidget):
    def __init__ (self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        
        #Almacenaremos los diferetnes nombres de los botones.
        contenidoBotones = ['Cls','Bck', '', 'Close',
                '7', '8', '9', '/',
                '4', '5', '6','*',
                '1','2','3', '-',
                '0', '.', '=', '+']
        
        # Lo que hacemos con esta linea es hacer  un doble bucle para  
        # recorrer la matrix : ya que la matrix tiene 5 filas y 4 columnas.
        # Y así almacenar en positions todas las posiciones para los botones
        
        positions = [(i, j) for i in range(5) for j in range(4)]
        
        #La función zip lo que hace es coger varias tuplas y 
        # te devuelve una a una sus posiciones juntas.
        
        for position, nombre in zip(positions, contenidoBotones):

            if nombre == '':
                continue
            button = QPushButton(nombre)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculadora')
        self.show()
        
def main():
    app = QApplication(sys.argv)
    ejemplo = VentanaGrid()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()