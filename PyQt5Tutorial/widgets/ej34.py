# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:17:40 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QFrame, QSplitter, QApplication)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        hBox = QHBoxLayout(self)
        
        topLeft = QFrame(self)
        
        topLeft.setFrameShape(QFrame.StyledPanel)
        
        topRight = QFrame (self)
        
        topRight.setFrameShape(QFrame.StyledPanel)
        
        fondo = QFrame (self)
        
        fondo.setFrameShape(QFrame.StyledPanel)
        
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topLeft)
        splitter1.addWidget(topRight)
        
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(fondo)
    
        hBox.addWidget(splitter2)
        self.setLayout(hBox)
        
        self.setGeometry(300,300,750,600)
        self.setWindowTitle('QSplitter')
        self.show()
        
def main ():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
