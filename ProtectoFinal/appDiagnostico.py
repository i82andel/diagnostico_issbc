# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:57:46 2021

@author: youne
"""
import sys
from PyQt5 import QtGui, QtWidgets
import controlador
import vista

observables =  controlador.md.conocimiento.observables()
app = QtWidgets.QApplication(sys.argv) #Se crea una instancia de aplicación
form = vista.MainWindow("Fallos", observables) #Se crea una instancia de de una ventana
sys.exit(app.exec_())


