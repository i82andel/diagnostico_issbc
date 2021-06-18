# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:57:46 2021

@author: youne
"""
import sys
from PyQt5 import QtGui
import controlador
import untitled6

observables =  controlador.ckModApDiagnostico.bcEnfermedades.observables()
app = QtGui.QApplication(sys.argv) #Se crea una instancia de aplicación
form = untitled6.DiagnosticDlg("Fallos", observables) #Se crea una instancia de de una ventana
sys.exit(app.exec_())


