# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:22:54 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
     
        grid = QGridLayout()
    
        x, y = 0, 0
        self.text = f'x: {x}, y: {y}'
        self.label = QLabel (self.text, self)
        grid.addWidget (self.label, 0,0, Qt.AlignTop)
        
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event object')
        self.show()
        
        
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = f'x: {x},  y: {y}'
        self.label.setText(text)  
        
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()