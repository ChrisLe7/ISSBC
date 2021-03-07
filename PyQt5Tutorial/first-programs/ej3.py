# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 09:21:54 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        #Con los objetos QToolTip creamos mensajes de ayuda para los objetos de
        #la aplicación. Estos ToolTip apareceran cuando pongamos el raton por encima de los objetos.
        #setFont: Permite asignar la fuente del mensaje, junto con el tamaño de la letra.
        
        QToolTip.setFont(QFont('SansSerif', 10))

        #Con setToolTip introducimos el mensaje el cual puede ser enriquecido con HTML.
        self.setToolTip('This is a <b>QWidget</b> widget')

        button = QPushButton('Button', self)
        button.setToolTip('This is a <b>QPushButton</b> widget')
        button.resize(button.sizeHint())
        button.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()