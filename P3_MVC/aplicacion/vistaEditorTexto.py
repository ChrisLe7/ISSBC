# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:06:47 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import (QTextEdit, QFileDialog, QApplication, 
                             QWidget, QPushButton, QLabel, QLineEdit, 
                             QHBoxLayout, QGridLayout, QVBoxLayout, QListWidget)

from pathlib import Path

from PyQt5.QtGui import QIcon
 
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
         
        self.botonSeleccionarCarpeta = QPushButton ('Seleccionar',self)           
        self.botonGuardar = QPushButton ('Guardar',self)           
        self.botonGuardarComo = QPushButton ('Guardar Como',self)           
        self.botonNuevoArchivo = QPushButton ('Nuevo Archivo',self)  
        
        #Creacion del editor de textos 
        self.editorTexto = QTextEdit()
        
        self.listArchivos = QListWidget()    
          
        #Creamos la linea para mostrar la ruta de la carpeta
        
        self.editCarpeta = QLineEdit()
        self.editArchivo = QLineEdit()

        # Una vez creado todos los Widgets ya podemos 
        # proceder a su posicionamiento
        
        layoutBotones = QHBoxLayout()
        layoutBotones.addWidget(self.botonNuevoArchivo)
        layoutBotones.addWidget(self.botonGuardar)
        layoutBotones.addWidget(self.botonGuardarComo)        
        layoutBotones.addStretch()
        # Ahora creamos la rejilla para el listado de archivos y el editor
        
        layoutListArchivos = QVBoxLayout()
        layoutListArchivos.addWidget(labelArchivo)
        layoutListArchivos.addWidget(self.listArchivos)
        layoutListArchivos.addSpacing(3)
        
        
        #Ahora crearemos el Grid para la gestión del layout del listArchivos y
        # el editorTexto

        layoutEditorTexto = QHBoxLayout()
        layoutEditorTexto.addWidget(self.editorTexto)
        
        
        layoutEditor = QGridLayout() 
        layoutEditor.addLayout(layoutListArchivos,0,0)
        
        layoutEditor.addLayout(layoutEditorTexto,0,1)
        layoutEditor.setColumnStretch(0, 1)
        layoutEditor.setColumnStretch(1, 2)
      
        # Creamos el Layout de la seccion superior
        
        layoutCarpeta = QHBoxLayout()

        layoutCarpeta.addWidget(labelCarpeta)
        layoutCarpeta.addSpacing(2)
        layoutCarpeta.addWidget(self.editCarpeta)
        layoutCarpeta.addWidget(self.botonSeleccionarCarpeta)
        
        # Ahora una vez gestionados todos los layout los introducimos en el
        # layout principal
        
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layoutCarpeta)
        mainLayout.addLayout(layoutEditor)
        mainLayout.addLayout(layoutBotones)
        
        #Finalizado el posicionamiento ya podemos proceder a las conexiones de
        #eventos
        
        self.makeConnections()
        
        self.setLayout(mainLayout)
        
        self.setGeometry(300, 300, 750, 650)
        self.setWindowTitle(u"Editor de Textos")
        self.setWindowIcon(QIcon('imagenes/logo.jfif'))
        self.show()
        
    
    #Funciones de la Vista
    
    def makeConnections(self):
        self.botonSeleccionarCarpeta.clicked.connect(self.seleccionarCarpeta)
        self.botonGuardar.clicked.connect(self.guardarArchivo)
        self.botonGuardarComo.clicked.connect(self.guardarArchivoComo)
        self.botonNuevoArchivo.clicked.connect(self.nuevoArchivo)
        self.listArchivos.itemDoubleClicked.connect(self.abrirArchivo)

    
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
        
        fileDialog = QFileDialog()
        fileDialog.setDefaultSuffix('.txt')
        direccionFicheroCompleto = fileDialog.getSaveFileName(self, 'Guardar Archivo', self.directorio_home, 'Text files (.txt)')
        DireccionFicheroSinExtension = direccionFicheroCompleto[0].split(".")
        
            
        self.direccionArchivo = DireccionFicheroSinExtension[0] + '.txt'
        
        self.guardarArchivo()
        self.listarDirectorio()
       
    
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
        