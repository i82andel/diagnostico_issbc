#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QPushButton, QLabel, QDesktopWidget, QLineEdit, QComboBox,QFileDialog

import controlador as ctrl

class DiagnosticDlg(QMainWindow):
    '''
    Cuadro de dialogo para la tarea de diangostico
    '''
    def __init__(self, name, observables=None, fallos=None, parent=None):
        '''
        Inicio del cuadro de dialogo   
        @param name: Nombre del cuadro
        @type name: string
        @param observables: Posibles observables
        @type obsevables: tupla de dos valores 
        '''
        super(DiagnosticDlg, self).__init__(parent)

        self.name = name #Coloca el nombre al cuadro de dialogo
        #Label
        labelListA=QLabel("Selecione los Fallos Presentados",self)
        labelListB=QLabel("",self)
        
        labelFallosA = QLabel("Seleccione los valores para observables", self)
        labelFallosB = QLabel("", self)
    
        headerObservables = ['Nombre del observable', 'Valor observado']
        headerFallos = ['Nombre del fallo']
        
        #Creamos el tableWidget para los observables
        self.tableWidgetObservables = QtGui.QTableWidget(len(observables),2) #Crea la tabla de elementos observables de dps columnas
        self.tableWidgetObservables.setColumnWidth(0, 250) #Asignan ancho a las columnas
        self.tableWidgetObservables.setColumnWidth(1, 400) #Asignan ancho a las columnas
        self.tableWidgetObservables.setHorizontalHeaderLabels(headerObservables) #Asigna etiquetas a las columnas
        

        #Rellenamos la tabla de observables
        for i in range(len(observables)): 
            #print i, observables[i].nombre,observables[i].tipo,observables[i].valoresPermitidos
            item1 = QtGui.QTableWidgetItem(observables[i].nombre) #Crea un item y le asigna el nombre de la observable

            if observables[i].tipo=='multiple':#Si el tipo de observable es multiple creamos un combox
                combobox = QtGui.QComboBox()
                for j in observables[i].valoresPermitidos:#añadimmos al combox los valeores permitidos
                    combobox.addItem(j) 
                self.tableWidgetObservables.setCellWidget(i, 1, combobox)#Establecemos en la celda i el combox
            elif observables[i].tipo=='boleano':#Si es boleano creamos otro combox con dos posibles valores
                combobox = QtGui.QComboBox()
                combobox.addItem('True') 
                combobox.addItem('False') 
                self.tableWidgetObservables.setCellWidget(i, 1, combobox)

            self.tableWidgetObservables.setItem(i, 0, item1)#Establecemos el item en la columna 0
            
     
        #ListWidget para las hipotesis  
        labelHipotesisL=QLabel("Posibles Hipotesis",self)#Creamos un listwidget para las posibles hipotesis
        labelHipotesisR=QLabel("",self)
        self.listWidgetHipotesis = QtGui.QListWidget()#Lista de hipotesis
        
        #ListWidget para el diagnostico
        labelDiagnosticoL=QLabel("Diagnostico",self)
        labelDiagnosticoR=QLabel("",self)
        self.listWidgetDiagnosticos = QtGui.QListWidget()#Lista de diagnosticos
        
        #Texto para la explicacion
        labelExplicacionL=QLabel("Explicacion",self)
        labelExplicacionR=QLabel("     ",self)
        self.PlainTextEditExplicacion = QtGui.QPlainTextEdit("Todavía no se ha realizado al diagnostico")#Cuadro de texto de la explicacion 
          
        #Botones
        self.diagnosticaButton=QtGui.QPushButton('Diagnosticar') #Para ejecutar el diagnostico
        
        self.buttonsLayout = QtGui.QHBoxLayout() #Gestor de diseño horizontal
        self.buttonsLayout.addStretch() 
        self.buttonsLayout.addWidget(self.diagnosticaButton)
        self.buttonsLayout.addStretch()
        
        #Rejilla de distribucion de los controles
        #========================================
        grid = QtGui.QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelListA, 0, 0)
        grid.addWidget(self.tableWidgetFallos, 2, 0,1,2)
        grid.addWidget(labelListB, 0, 1)
        
        grid.addWidget(labelFallosA, 0, 4)
        grid.addWidget(labelFallosB, 0, 5)
        grid.addWidget(self.tableWidgetObservables, 2, 2, 1, 8)
        
        grid.addWidget(labelHipotesisL, 0, 10)
        grid.addWidget(labelHipotesisR, 0, 11)
        grid.addWidget(self.listWidgetHipotesis, 2, 10,1,3)
        
        grid.addWidget(labelDiagnosticoL, 4, 0)
        grid.addWidget(labelDiagnosticoR, 4, 1)
        grid.addWidget(self.listWidgetDiagnosticos, 5, 0,1,2)
        grid.addWidget(labelExplicacionL, 4, 2)
        grid.addWidget(labelExplicacionR, 4, 3)
        grid.addWidget(self.PlainTextEditExplicacion, 5, 2,1,11)
        
        #Diseño principal
        mainLayout = QtGui.QVBoxLayout() #Se crea el diseño principal en forma vertical
        mainLayout.addLayout(grid) #Le añadimos la rejilla de los controles
        mainLayout.addLayout(self.buttonsLayout) #Añadimos la disposicion de controles horizontal
        self.setLayout(mainLayout) #Asignar a la ventana la distribucion de los controles
        
    
        self.setGeometry(300, 300, 1240, 700)
        self.setWindowTitle(u"Diagnostico de " + ctrl.getNameBC() + " - Juan Carlos Gomez Duran / Miguel Lama del Valle".format(self.name))
        self.show()
 
        self.center()
        
        #Conexiones de los botones y eventos en las listas:
        #==================================================
        self.diagnosticaButton.clicked.connect(self.diagnostica)

    
    def diagnostica(self):
        ctrl.eventDiagnostica(self) #Se invoca al gestor del controlador
        
    
    def center(self):        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        



        

         
    

 