# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 17:22:30 2021

@author: ChrisLe
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        panelLcd = QLCDNumber(self)
        panelSld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(panelLcd)
        vbox.addWidget(panelSld)

        self.setLayout(vbox)
        panelSld.valueChanged.connect(panelLcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()