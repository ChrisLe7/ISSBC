# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 18:28:20 2021

@author: ChrisLe
"""

import sys 

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QInputDialog, QApplication)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.button = QPushButton('Dialog', self)
        self.button.move(20,20)
        self.button.clicked.connect(self.showDialog)
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(130,22)
        
        self.setGeometry(300, 300, 750, 350)
        self.setWindowTitle('Ejemplo InputDialog')
        self.show()
        
    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Introduce tu nombre:')
        
        if ok:
            self.lineEdit.setText(str(text))

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    


                 