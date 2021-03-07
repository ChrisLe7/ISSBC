# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 08:21:26 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication

from PyQt5.QtGui import QIcon

class Ventana (QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initVentana()
        
    def initVentana(self):
        editorTexto = QTextEdit()
        self.setCentralWidget(editorTexto)
        
        
        exitAct = QAction(QIcon('exit.png'), 'Salir', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Salir de la Aplicacion')
        exitAct.triggered.connect(self.close)
        
        #Con esto crearemos nuestra barra de estados.
        self.statusBar()
        
        #Con menuBar a nuestro objeto Ventana 
        #podremos crear nuestra barra de menu
        
        menubar = self.menuBar()

        #Añadiendo las opciones mediante la función addMenu 
        #posteriormente podemos añadir a dichas opciones 
        #actiones que desencaden.
        fileMenu = menubar.addMenu('&Archivo')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Salir')
        toolbar.addAction(exitAct)

        
        self.setGeometry(450, 450, 350, 250)
        self.setWindowTitle('Ventana Principal')
        self.setWindowIcon(QIcon('logo.jfif'))
        self.show()
    
def main():
    aplicacion = QApplication(sys.argv)
    ventanaEjemplo = Ventana()
    sys.exit(aplicacion.exec_()) 

if __name__ == '__main__':
    main()