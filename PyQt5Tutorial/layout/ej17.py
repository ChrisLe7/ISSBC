# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:13:43 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)

class Example(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()
        
    def initUI(self):
        titulo = QLabel ('Titulo')
        autor = QLabel ('Autor')
        review = QLabel ('Review')
        
        tituloEdit = QLineEdit()
        autorEdit = QLineEdit()
        reviewEdit = QLineEdit()
        
        grid = QGridLayout()
        grid.setSpacing(10)
        
        grid.addWidget(titulo, 1, 0)
        grid.addWidget(tituloEdit, 1, 1)
        grid.addWidget(autor, 2, 0)
        grid.addWidget(autorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1)
        
        self.setLayout(grid)
        
        self.setGeometry(450, 450, 550, 450)
        self.setWindowTitle('Ejemplo Final')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
    
if __name__=='__main__':
    main()