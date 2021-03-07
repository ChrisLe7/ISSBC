# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 10:16:35 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,450,250)
        self.setWindowTitle('Ventana Mensaje Emergente')
        self.show()
        
    def closeEvent(self, event):
        #La estructura de la función question es (WidgetPadre,TituloVentana,MensajeVentana,Posibles_Estados, ValorPorDefecto )
        respuestaEvento = QMessageBox.question(self,'Mensaje Emergente', "¿Estás seguro de salir?",
                                               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuestaEvento == QMessageBox.Yes:
            print('Se cerrará la ventana')
            event.accept()
        else:
            print('Se ignorará el evento')
            event.ignore()
    
def main():
    app= QApplication(sys.argv)
    ex= Example()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()    
        