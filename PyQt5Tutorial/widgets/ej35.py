# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 12:30:44 2021

@author: ChrisLe
"""

import sys

from PyQt5.QtWidgets import (QWidget, QLabel,
                             QComboBox, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl = QLabel('Ubuntu', self)

        #Con el objeto QCombo podemos añadir como un selector con diferentes opciones
        # Siendo posible escoger uno.
        
        combo = QComboBox(self)
        combo.addItem('Ubuntu')
        combo.addItem('Mandriva')
        combo.addItem('Fedora')
        combo.addItem('Arch')
        combo.addItem('Gentoo')

        combo.move(50, 50)
        self.lbl.move(50, 150)

        #Posteriormente con connect vinculamos la función al cambio del selector.
        
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()