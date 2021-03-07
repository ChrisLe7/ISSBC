# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:15:20 2021

@author: ChrisLe
"""

from PyQt5.QtWidgets import (QWidget, QSlider, QLabel, QApplication)

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

import sys

class Example (QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        slider = QSlider (Qt.Horizontal, self)
        slider.setFocusPolicy (Qt.NoFocus)
        slider.setGeometry (30,40,200,30)
        
        slider.valueChanged[int].connect(self.changeValue)
        
        self.label = QLabel(self)
        self.label.setPixmap (QPixmap ('mute.png'))
        self.label.setGeometry (250,40,80,40)
        
        self.setGeometry(300,300,350,250)
        
        self.setWindowTitle ('QSlider')
        self.show()
        
        
    def changeValue (self, value):
        
        if value == 0:
             self.label.setPixmap(QPixmap('mute.png'))
        elif 0 < value <= 30:

            self.label.setPixmap(QPixmap('min.png'))
        elif 30 < value < 80:

            self.label.setPixmap(QPixmap('med.png'))
        else:

            self.label.setPixmap(QPixmap('max.png'))
            
    
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()