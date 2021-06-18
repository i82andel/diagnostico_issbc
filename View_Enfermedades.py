# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:25:26 2021

@author: youne
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:11:45 2021

@author: youne
"""

from PyQt5 import QtCore
from os import environ


from PyQt5.QtWidgets import QVBoxLayout,QGridLayout, QHBoxLayout, QPlainTextEdit,QListWidget,QTableWidget,QTableWidgetItem,QMainWindow, QAction, QApplication, QPushButton, QLabel, QDesktopWidget, QLineEdit, QComboBox,QFileDialog
import sys

class DiagnosticDlg(QMainWindow):
    '''
    Cuadro de dialógo para la tarea de diangóstico
    '''
    def __init__(self, name, observables=None, parent=None):
        '''
        Inicio del cuadro de diálogo
        
        @param name: Nombre del cuadro
        @type name: string
        
        @param observables: Posibles observables
        @type obsevables: tupla de dos valores 
        
        '''
        self.name = name #Coloca el nombre al cuadro de diálogo
        super(DiagnosticDlg, self).__init__(parent)

        
        #Label
        labelListA=QLabel("Selecione los Fallos Presentados",self)
        labelListB=QLabel("",self)#quitar
        observables_list = [(f.nombre , f.valor)  for f in observables]
        header = ['NOMBRE', 'VALOR']
        #posiblesFallos = Fallos(self,   observables_list, header)
        self.tableWidgetPosiblesFallos = QTableWidget(len(observables_list),2) #Crea la tabla de elementos
        self.tableWidgetPosiblesFallos.setColumnWidth(0, 400) #Asignan ancho a las columnas
        self.tableWidgetPosiblesFallos.setColumnWidth(1, 400)
        self.tableWidgetPosiblesFallos.setHorizontalHeaderLabels(header) #Asigna etiquetas a las columnas
        
        #print observables
        for i in range(len(observables)):
            #print i, observables[i].nombre,observables[i].tipo,observables[i].valoresPermitidos
            item1 = QTableWidgetItem(observables[i].nombre) #Crea un item y le asigna el nombre de la observable
            item1.setCheckState(QtCore.Qt.Checked) # Establece propiedades a las celdas de la primera columna
            item1.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)

            if observables[i].tipo=='multiple':#Si el tipo de observable es múltiple creamos un combox
                combobox = QComboBox()
                for j in observables[i].valoresPermitidos:#añadimmos al combox los valeores permitidos
                    combobox.addItem(j) 
                self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)#Establecemos en la celda i el combox
            elif observables[i].tipo=='boleano':#Si es boleano creamos otro combox
                combobox = QComboBox()
                combobox.addItem('True') 
                combobox.addItem('False') 
                self.tableWidgetPosiblesFallos.setCellWidget(i, 1, combobox)

            self.tableWidgetPosiblesFallos.setItem(i, 0, item1)#Establecemos el item en la columna 0
                
        labelHipotesisL=QLabel("Posibles Hipotesis",self)#Creamos un listwidget para las posibles hipótesis
        labelHipotesisR=QLabel("",self)
        self.listWidgetHipotesis = QListWidget()#Lista de hipótesis
        
        labelDiagnosticoL=QLabel("Diagnóstico",self)
        labelDiagnosticoR=QLabel("",self)
        self.listWidgetDiagnosticos = QListWidget()#Lista de diagnósticos
        
        labelExplicacionL=QLabel("Explicacion",self)
        labelExplicacionR=QLabel("     ",self)
        self.PlainTextEditExplicacion = QPlainTextEdit()#Cuadro de texto    de la explicación           
        #Botones
        self.coberturaCausalButton=QPushButton('Cobertura Causal')#Para invocar el método de cobretura causal
        self.diagnosticaButton=QPushButton('Diagnostica') #Para ejecutar el diagnóstico
        self.exitButton=QPushButton('Exit') #Para salir del programa
        
        self.buttonsLayout = QHBoxLayout() #Gestor de diseño horizontal
        #http://stackoverflow.com/questions/20452754/how-exactly-does-addstretch-work-in-qboxlayout
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.coberturaCausalButton)
        self.buttonsLayout.addWidget(self.diagnosticaButton)
        self.buttonsLayout.addWidget(self.exitButton)
        self.buttonsLayout.addStretch()
        
        #Rejilla de distribución de los controles
        #Ver http://srinikom.github.io/pyside-docs/PySide/QtGui/QGridLayout.html
        grid = QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(labelListA, 0, 0)
        grid.addWidget(self.tableWidgetPosiblesFallos, 1, 0,1,2)
        grid.addWidget(labelListB, 0, 1)
        
        grid.addWidget(labelHipotesisL, 2, 0)
        grid.addWidget(labelHipotesisR, 2, 1)
        grid.addWidget(self.listWidgetHipotesis, 3, 0,1,2)
        
        grid.addWidget(labelDiagnosticoL, 4, 0)
        grid.addWidget(labelDiagnosticoR, 4, 1)
        grid.addWidget(self.listWidgetDiagnosticos, 5, 0,1,2)
        grid.addWidget(labelExplicacionL, 6, 0)
        grid.addWidget(labelExplicacionR, 6, 1)
        grid.addWidget(self.PlainTextEditExplicacion, 7, 0,1,2)
        
        #Diseño principal
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(grid)
        mainLayout.addLayout(self.buttonsLayout)
        self.setLayout(mainLayout) #Asignar a la ventana la distribución de los controles
        
    
        self.setGeometry(300, 300, 900, 1200)
        self.setWindowTitle(u"TAREA DE DIAGNOSTICO".format(self.name))
        self.show()
 
        self.center()
        
        #Conexiones de los botones y eventos en las listas:
        #==========
        self.tableWidgetPosiblesFallos.itemDoubleClicked.connect(self.moveRight)
        #self.listWidgetFallos.itemDoubleClicked.connect(self.moveLeft)
        self.coberturaCausalButton.clicked.connect(self.coberturaCausal)
        self.diagnosticaButton.clicked.connect(self.diagnostica)
        self.exitButton.clicked.connect(self.close)


    '''def dl(self,item):
        print (item.text())

    def diagnostica(self):
        ckCtrlDiagnostico.eventDiagnostica(self)
        
        
    def coberturaCausal(self):
        #Recolecta datos de las vistas y se lo pasamos al controlador
        # Al pasar self pasamos toda la información de la ventana
        ckCtrlDiagnostico.eventCoberturaCausal(self)
    
    def center(self):        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topRight())

'''
    def suppress_qt_warnings():
        environ["QT_DEVICE_PIXEL_RATIO"] = "0"
        environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        environ["QT_SCREEN_SCALE_FACTORS"] = "1"
        environ["QT_SCALE_FACTOR"] = "1"


    suppress_qt_warnings()

if __name__ == "__main__":
    if True:
        #Podemos probar el módulo de vistas de forma autónoma
       # observables =  ckCtrlDiagnostico.ckModApDiagnostico.bcEnfermedades.observables()
        
        app = QApplication(sys.argv)
       # form = DiagnosticDlg("Fallos", observables)
        sys.exit(app.exec_())
    if False:
        #observables =  ckCtrlDiagnostico.ckModApDiagnostico.bcEnfermedades.observables()
        #print (observables)
        #l = [(f.nombre , f.valor)  for f in observables]
        #print( l)
        header = ['Nombre', 'Valor']
    

 