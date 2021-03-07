# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:06:57 2021

@author: ChrisLe
"""

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QApplication)

import sys

class Example(QWidget):
    
    def __init__(self):
        super ().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.label = QLabel (self)
        
        lineEdit = QLineEdit(self)
        
        lineEdit.move (60,100)
        self.label.move(60,40)
        
        lineEdit.textChanged[str].connect(self.onChanged)
        
        self.setGeometry(300, 300, 450, 250)
        self.setWindowTitle('QLineEdit')
        self.show()
    
    def onChanged(self,text):
        '''
        Parameters
        ----------
        text : Texto
            Texto que se encuentra en el QLineEdit.
        Returns
        -------
        None.
        Do
        -------
        Realiza el cambio de la Etiqueta de la ventana.
        '''
        self.label.setText(text)
        self.label.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example ()
    sys.exit (app.exec_())

if __name__ == '__main__':
    main()        
        