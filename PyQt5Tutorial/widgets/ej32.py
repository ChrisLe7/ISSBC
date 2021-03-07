# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 10:01:14 2021

@author: ChrisLe
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QLabel, QApplication)

from PyQt5.QtGui import QPixmap

import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        hBox = QHBoxLayout(self)
        pixmap = QPixmap('logo.jfif')
        label = QLabel(self)
        
        label.setPixmap (pixmap)
        
        hBox.addWidget (label)
        
        self.setLayout(hBox)
        
        self.move(300, 200)
        self.setWindowTitle('Wolf')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()        
        