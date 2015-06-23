# -*- coding: utf-8 -*-

class Auto():

  def __init__(self):
    self.cantidad_personas = 0

  def subir_persona(self):
    self.cantidad_personas = self.cantidad_personas + 1

  def bajar_persona(self):
    self.cantidad_personas = self.cantidad_personas - 1

  def subir5_personas(self):
    self.cantidad_personas = self.cantidad_personas + 5

  def bajar5_personas(self):
    self.cantidad_personas = self.cantidad_personas - 5

  def subirN_personas(self, N):
    self.cantidad_personas = self.cantidad_personas + N

  def bajarN_personas(self, N):
    self.cantidad_personas = self.cantidad_personas - N
