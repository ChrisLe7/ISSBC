# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:46:39 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example (QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        
        barraMenu = self.menuBar()
        fileMenu = barraMenu.addMenu('File')
        
        impMenu = QMenu ('Importar', self)
        impAct = QAction('Importar Email',self)
        impMenu.addAction(impAct)
        
        newAct = QAction('New',self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        
        self.setGeometry(300, 300, 450,450)
        self.setWindowTitle('Submenus')
        self.show()
        
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()
    