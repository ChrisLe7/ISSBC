# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 11:25:46 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        exitAct = QAction (QIcon ('exit.png'), '&Salir', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Salir de la Aplicación')
        exitAct.triggered.connect(qApp.quit)
        
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        self.setGeometry(400, 400, 350, 250)
        self.setWindowTitle('Menu Simple')
        self.show()
        
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
    
        