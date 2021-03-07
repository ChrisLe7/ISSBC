# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:44:44 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QSizePolicy, 
                                     QLabel, QFontDialog, QApplication)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        vBox = QVBoxLayout()
        
        button = QPushButton('Dialogo',self)
        
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        button.move(20,20)
        
        vBox.addWidget(button)
        
        button.clicked.connect (self.showDialog)
        
        self.label = QLabel ('Texto de Prueba', self)
        
        self.label.move (130,20)
        
        vBox.addWidget(self.label)
        
        self.setLayout(vBox)
        
        self.setGeometry(300, 300, 450, 350)
        self.setWindowTitle('Dialogo de Fuentes')
        self.show()
        
    def showDialog(self):
        
        font, ok = QFontDialog.getFont()
        
        if ok:
            self.label.setFont(font)
    

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    
    