# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append("../Controlador")
from maincontroller import *

class MainWindow(QtGui.QWidget):

  def __init__(self):
    super(MainWindow, self).__init__()
    self.controlador = MainController(self)
    self.init_ui()

  def init_ui(self):
    self.label = QtGui.QLabel("CANTIDAD DE PERSONAS")
    self.entrada_valores = QtGui.QLineEdit()
    h_layout = QtGui.QHBoxLayout()
    button_subir = QtGui.QPushButton("Subir persona")
    button_bajar = QtGui.QPushButton("Bajar persona")
    button_subir5 = QtGui.QPushButton("Subir 5 personas")
    button_bajar5 = QtGui.QPushButton("Bajar 5 personas")
    button_subirN = QtGui.QPushButton("Subir N:")
    button_bajarN = QtGui.QPushButton("Bajar N:")
    h_layout.addWidget(self.label)
    h_layout.addWidget(button_subir)
    h_layout.addWidget(button_bajar)
    h_layout.addWidget(button_subir5)
    h_layout.addWidget(button_bajar5)
    h_layout.addWidget(button_subirN)
    h_layout.addWidget(button_bajarN)
    h_layout.addWidget(self.entrada_valores)

    button_subir.clicked.connect(self.controlador.handler_subir_persona)
    button_bajar.clicked.connect(self.controlador.handler_bajar_persona)
    button_subir5.clicked.connect(self.controlador.handler_subir5_personas)
    button_bajar5.clicked.connect(self.controlador.handler_bajar5_personas)
    button_subirN.clicked.connect(self.controlador.hanlder_subirN)
    button_bajarN.clicked.connect(self.controlador.hanlder_bajarN)

    self.setLayout(h_layout)
    self.setWindowTitle("Primer Auto")
    self.setGeometry(200, 200, 200, 200)
    self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())

