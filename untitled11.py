# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:51:10 2021

@author: LuisAneri
"""

# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QComboBox,QWidget, QCheckBox
import modelo as md

def getNameBC():
    return md.cd.getNombreBC()
            
def eventCoberturaCausal(cdDiagnostico,tr=False):
    '''
    Inferencia de cobertura causal.
    '''
    fallos=[]#Vamos a captar los fallos del cuadro de di�logo
    if tr:
        print ('entra')
    for i in range(cdDiagnostico.sintomasWindget.rowCount()):
        item1=cdDiagnostico.sintomasWindget.cellWidget(i,0)
        text = cdDiagnostico.sintomasWindget.item(i,1)
        if item1.isChecked():
            print (item1.checkState())
            item2=cdDiagnostico.sintomasWindget.cellWidget(i, 2)
            print (item2, item2.currentText())
            fallos.append( (text.text(),item2.currentText()) )
    if tr:
        print (fallos)
    cc=md.CoberturaCausal(fallos)#Invocamos a la inferencia de cobertura causal del diagn�stico
    cc.execute()
    lHipotesis=[]
    for h in cc.listaHipotesis:
        lHipotesis.append(h.nombre)#Obtenemos la lista de hip�tesis
    cdDiagnostico.HipotesisList.clear()#Borramos la informaci�n del listWidget
    cdDiagnostico.HipotesisList.addItems(lHipotesis)#a�adimos la nueva informaci�n al listWidgwet
    
            
def eventDiagnostica(cdDiagnostico,tr=False):
    '''
    Controla el evendo de diagn�stico
    '''
    cdDiagnostico.plainTextEdit.clear()
    pass
    eventCoberturaCausal(cdDiagnostico,tr=False)
    fallos=[]
        #print cdDiagnostico.listWidgetFallos.count()
    if tr:
        print ('entra')
    for i in range(cdDiagnostico.sintomasWindget.rowCount()):
        item1=cdDiagnostico.sintomasWindget.cellWidget(i,0)
        text = cdDiagnostico.sintomasWindget.item(i,1)
        if item1.isChecked():
            print (item1.checkState())
            item2=cdDiagnostico.sintomasWindget.cellWidget(i, 2)
            print (item2, item2.currentText())
            fallos.append( (text.text(),item2.currentText()) )#Creamos una tupla del fallo y sus posibles
                                                               #valores
    if tr:        
        print ('Presentando los fallos',fallos)
        print ('======================')
    
    #Comprueba que los fallos captados son compatibles con la base de conocimiento
    observables=md.identificaSignosSintomas(fallos)
    if tr:
        print ('Obteniendo Observables:', observables)
    if not observables==None:#Continuo porque todo es correcto
        pass
        mcc=md.MetodoCoberturaCausal(observables)#Creamos una instancia del m�todo cc
        mcc.execute()
        if tr:
            pass
        print ('Justificacion')
        print ('=============')
        print (mcc.explicacion)
        print ('')
        print ('Diagnostico: ' )
        print ('============ ')
        for d in mcc.diagnostico:
            print( d.nombre)
        print ('fin')
        cdDiagnostico.plainTextEdit.clear()
        cdDiagnostico.plainTextEdit.appendPlainText(mcc.explicacion)
        cdDiagnostico.plainTextEdit.moveCursor(QtGui.QTextCursor.Start)
        
        
        #tc=cdDiagnostico.plainTextEdit.textCursor()
        #tc.movePosition(QtGui.QTextCursor.Start)
        #print tc.position()
        cdDiagnostico.listWidgetDiagnosticos.clear()
        lDiag=[]
        for d in mcc.diagnostico:
            lDiag.append(d.nombre)
            cdDiagnostico.listWidgetDiagnosticos.addItems(lDiag)
    
    
        
        
    
    return
    mcc=md.MetodoCoberturaCausal(fallos)
    mcc.execute()
    print (mcc.diagnostico)
    print (mcc.explicacion)
    
    
 
def observables():
    return 
       
    

if __name__=='__main__':  
    pass