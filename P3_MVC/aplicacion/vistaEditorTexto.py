# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:06:47 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication, QWidget, 
                             QPushButton, QLabel, QLineEdit, QHBoxLayout,
                             QGridLayout, QVBoxLayout, QListWidget)

from pathlib import Path

 
from aplicacion import controladorEditorTexto as controlador

class EditorText (QWidget):
    
    def __init__(self):
       super().__init__()
       self.initEditor()
       self.rutaCarpeta = ''
       self.direccionArchivo = ''
       self.directorio_home = str(Path.home())
        
    def initEditor(self):
        
        #En primer lugar crearemos las etiquetas y paneles necesarios 
        # las diferentes opciones.
            
        #Creacion de las Etiquetas
        labelCarpeta = QLabel ('Carpeta:', self)
        labelArchivo = QLabel ('Archivos:', self)
        
        #Creacion de los Botones
         
        botonSeleccionarCarpeta = QPushButton ('Seleccionar',self)           
        botonGuardar = QPushButton ('Guardar',self)           
        botonGuardarComo = QPushButton ('Guardar Como',self)           
        botonNuevoArchivo = QPushButton ('Nuevo Archivo',self)  
        #Creacion del editor de textos 
        self.editorTexto = QTextEdit()
        
        self.listArchivos = QListWidget()    
          
        #Creamos la linea para mostrar la ruta de la carpeta
        
        self.editCarpeta = QLineEdit()
        self.editArchivo = QLineEdit()

        # Una vez creado todos los Widgets ya podemos 
        # proceder a su posicionamiento
        
        layoutBotones = QHBoxLayout()
        layoutBotones.addWidget(botonNuevoArchivo)
        layoutBotones.addWidget(botonGuardar)
        layoutBotones.addWidget(botonGuardarComo)        
        layoutBotones.addStretch()
        # Ahora creamos la rejilla para el listado de archivos y el editor
        
        layoutListArchivos = QVBoxLayout()
        layoutListArchivos.addWidget(labelArchivo)
        layoutListArchivos.addWidget(self.listArchivos)
        layoutListArchivos.addSpacing(3)
        
        layoutEditorTextos = QHBoxLayout()
        layoutEditorTextos.addSpacing(3)
        layoutEditorTextos.addLayout(layoutListArchivos)
        layoutEditorTextos.addSpacing(1)
        layoutEditorTextos.addWidget(self.editorTexto)
      
        # Creamos el Layout de la seccion superior
        
        layoutCarpeta = QHBoxLayout()

        layoutCarpeta.addWidget(labelCarpeta)
        layoutCarpeta.addSpacing(2)
        layoutCarpeta.addWidget(self.editCarpeta)
        layoutCarpeta.addWidget(botonSeleccionarCarpeta)
        
        # Ahora una vez gestionados todos los layout los introducimos en el
        # layout principal
        
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layoutCarpeta)
        mainLayout.addLayout(layoutEditorTextos)
        mainLayout.addLayout(layoutBotones)
        
        #Finalizado el posicionamiento ya podemos proceder a las conexiones de
        #eventos
        
        botonSeleccionarCarpeta.clicked.connect(self.seleccionarCarpeta)
        botonGuardar.clicked.connect(self.guardarArchivo)
        botonGuardarComo.clicked.connect(self.guardarArchivoComo)
        botonNuevoArchivo.clicked.connect(self.nuevoArchivo)
        self.listArchivos.itemDoubleClicked.connect(self.abrirArchivo)
        
        self.setLayout(mainLayout)
        
        self.setGeometry(300, 300, 750, 650)
        self.setWindowTitle(u"Editor de Textos")
        self.show()
        
    
    #Funciones de la Vista
    
    def abrirArchivo(self, archivoSeleccionado):
      
        self.direccionArchivo = self.rutaCarpeta + '/' + archivoSeleccionado.text()
        contenidoArchivo = controlador.abrirArchivo(self.direccionArchivo)        
        self.editorTexto.clear()
        self.editorTexto.setText(contenidoArchivo)

    def guardarArchivo(self):
        
        if self.direccionArchivo != '':
            contenidoArchivo = self.editorTexto.toPlainText()
            controlador.guardarArchivo(self.direccionArchivo, contenidoArchivo)
        else:
            self.guardarArchivoComo()
        
    def guardarArchivoComo(self):
        direccionFicheroCompleto = QFileDialog.getSaveFileName(self, 'Guardar Archivo', self.directorio_home)
        self.direccionArchivo = direccionFicheroCompleto[0]
        self.guardarArchivo()
       
    
    def seleccionarCarpeta(self):
        self.rutaCarpeta = QFileDialog.getExistingDirectory(self, 'Abrir Carpeta', self.directorio_home) 
        self.editCarpeta.setText(self.rutaCarpeta)
        self.listarDirectorio()
        
        
    def listarDirectorio (self):
        listadoDirectorio = controlador.listarDirectorio(self.rutaCarpeta)
        self.listArchivos.clear()        
        self.listArchivos.addItems(listadoDirectorio)
        
    def nuevoArchivo(self):
        self.editorTexto.clear()
        self.direccionArchivo = ''

         
         
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = EditorText()
    sys.exit(app.exec_())
        