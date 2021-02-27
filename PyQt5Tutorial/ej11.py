# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:54:34 2021

@author: ChrisLe

NO HACE NADA PREGUNTAR / REVISAR
"""

import sys

from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Example (QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(450, 450, 300, 250)
        self.setWindowTitle('Context Menu')
        self.show()
    
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        nuevoAct = cmenu.addAction("Nuevo")
        abriAct = cmenu.addAction("Open")
        salirAct = cmenu.addAction("Salir")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == salirAct:
            qApp.quit()
            
            
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
    