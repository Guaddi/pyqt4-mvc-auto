# -*- coding: utf-8 -*-
import sys
sys.path.append("../Modelo")
from Auto import *

class MainController():

    def __init__(self, una_ventana):
        self.auto = Auto()
        self.ventana = una_ventana

    def handler_subir_persona(self):
        self.auto.subir_persona()
        print (self.auto.cantidad_personas)
        self.actualizar_label()

    def handler_bajar_persona(self):
        self.auto.bajar_persona()
        print (self.auto.cantidad_personas)
        self.actualizar_label()

    def actualizar_label(self):
        self.ventana.label.setText(str(self.auto.cantidad_personas))

    def handler_subir5_personas(self):
        self.auto.subir5_personas()
        print (self.auto.cantidad_personas)
        self.actualizar_label()

    def handler_bajar5_personas(self):
        self.auto.bajar5_personas()
        print (self.auto.cantidad_personas)
        self.actualizar_label()

    def hanlder_subirN(self):
        x = self.ventana.entrada_valores.text()
        n = int(x)
        self.auto.subirN_personas(n)
        print (self.auto.cantidad_personas)
        self.actualizar_label()

    def hanlder_bajarN(self):
        x = self.ventana.entrada_valores.text()
        n = int(x)
        self.auto.bajarN_personas(n)
        print (self.auto.cantidad_personas)
        self.actualizar_label()