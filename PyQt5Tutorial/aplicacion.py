# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:00:35 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QGridLayout, QPushButton,
                             QTextEdit, QAction, QFileDialog)
from pathlib import Path

from PyQt5.QtGui import QIcon

class Ventana (QMainWindow):
    
    def __init__(self):
        super().__init__()
           
        self.init()
        
        self.ruta = ''
        
    def init(self):
        self.editorTexto = QTextEdit()
        self.setCentralWidget(self.editorTexto)
        self.statusBar()
        
        #Primero haremos las opciones disponibles
        
        #Leer y Editar Fichero
        openFile = QAction('Abrir', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Abrir Archivo')
        openFile.triggered.connect(self.AbrirArchivo)
        
        
        #Guardar Fichero
        
        saveFile = QAction('Guardar', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Guardar Archivo')
        saveFile.triggered.connect(self.GuardarArchivo)
        
        #Guardar Como Fichero
        
        saveAsFile = QAction('Guardar Como', self)
        saveAsFile.setShortcut('Ctrl+Shift+S')
        saveAsFile.setStatusTip('Guardar Como')
        saveAsFile.triggered.connect(self.GuardarComoArchivo)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu ('&File')
        fileMenu.addAction (openFile)
        
        fileMenu.addAction (saveFile)

        fileMenu.addAction (saveAsFile)
                
        
        self.setGeometry (450,450, 750, 550)
        self.setWindowTitle('Gestor de Archivos')
        self.show()
        
        
    def AbrirArchivo(self):
        directorio_home = str(Path.home())
        self.ruta = QFileDialog.getOpenFileName(self, 'Abrir Archivo', directorio_home)
        
        if self.ruta[0]:
            f = open(self.ruta[0], 'r')
            
            with f:
                data = f.read()
                self.editorTexto.setText(data)
                f.close()

    def GuardarArchivo (self):
        
        if self.ruta != '':
            contenido = self.editorTexto.getContentsMargins()
            fichero =  open(self.ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
        else: 
            self.GuardarComoArchivo()
    
    def GuardarComoArchivo(self):
        
        directorio_home = str(Path.home())
        self.ruta = QFileDialog.getSaveFileName(self, 'Guardar Archivo', directorio_home)
        
        if self.ruta[0]:
        
            contenido = self.editorTexto.toPlainText()
            fichero = open(self.ruta[0], 'w+')
            fichero.write(contenido)
            fichero.close()
        else:
            self.setWindowTitle('Guardado Cancelado')
            ruta = ''
        
        
def main():
    app = QApplication (sys.argv)
    ex = Ventana ()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
    

