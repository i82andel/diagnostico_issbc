# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:51:10 2021

@author: LuisAneri
"""

# -*- coding: utf-8 -*-


from PyQt5 import QtGui
from PyQt5 import QtCore
import modelo as md

def getNameBC():
    return md.cd.getNombreBC()
            
def eventDiagnostica(cdDiagnostico,tr=False):
    '''
    Controla el evento de diagnostico.
    '''
    
    cdDiagnostico.listWidgetDiagnosticos.clear() #Borramos la informacion del los diagnosticos    
    cdDiagnostico.PlainTextEditExplicacion.clear()
    cdDiagnostico.listWidgetHipotesis.clear()
    
    
    fallos = []
    if tr:
        print ('entra')
    for i in range(cdDiagnostico.tableWidgetFallos.rowCount()):
        item1=cdDiagnostico.tableWidgetFallos.item(i,0)
        if item1.checkState()==QtCore.Qt.Checked:
            fallos.append(item1.text())#Creamos una tupla del fallo y sus posibles
                                                               #valores
    if tr:        
        print ('Presentando los fallos',fallos)
        print ('======================')
        
    
    if not fallos==None:
        
        lObservables = []
        for i in range(cdDiagnostico.tableWidgetObservables.rowCount()):
            item1=cdDiagnostico.tableWidgetObservables.item(i,0)
            item2=cdDiagnostico.tableWidgetObservables.cellWidget(i, 1)
            lObservables.append((item1.text(),item2.currentText()))        
        
        
        
        mcc=md.MetodoCoberturaCausal(fallos)
        mcc.setObservables(lObservables)
        mcc.execute(True)
        

        lHipotesis = []        
        for h in mcc.getDiferencial():
            lHipotesis.append(h.nombre)#Obtenemos la lista de hipótesis
            cdDiagnostico.listWidgetHipotesis.clear()#Borramos la información del listWidget
            cdDiagnostico.listWidgetHipotesis.addItems(lHipotesis)#añadimos la nueva información al listWidgwet

        print ('Justificacion')
        print ('=============')
        print (mcc.getExplicacion())
        print ()
        print ('Diagnostico: ' )
        print ( '============ ')
        for d in mcc.getDiagnostico():
            print (d.nombre)
        print ('fin')
        cdDiagnostico.PlainTextEditExplicacion.clear()
        cdDiagnostico.PlainTextEditExplicacion.appendPlainText(mcc.explicacion)
        cdDiagnostico.PlainTextEditExplicacion.moveCursor(QtGui.QTextCursor.Start)
        cdDiagnostico.listWidgetDiagnosticos.clear()
        lDiag=[]
        if len(mcc.getDiagnostico()) <= 0:
            lDiag.append("No hay diagnostico")
            cdDiagnostico.listWidgetDiagnosticos.addItems(lDiag)
        else:
            for d in mcc.getDiagnostico():
                if d.nombre not in lDiag:
                    lDiag.append(d.nombre)
            cdDiagnostico.listWidgetDiagnosticos.addItems(lDiag)
        
    else:
        cdDiagnostico.listWidgetDiagnosticos.addItems(["No hay diagnosticos."])        
        cdDiagnostico.PlainTextEditExplicacion.appendPlainText("No hay diagnostico valido. Ninguna de las hipotesis planteadas es posible.")
    
    return    
    
 
def observables():
    return   

