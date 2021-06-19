# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vista.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QComboBox,QWidget
import controlador

class MainWindow(QWidget):
    
    def __init__(self,name=None,observables=None,parent=None):
        super(MainWindow,self).__init__(parent)
        self.name = name
        
        
        self.setObjectName("MainWindow")
        self.resize(839, 630)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        
#*************************************************************************#         
        
        observables_list = [(f.nombre , f.valor)  for f in observables]
        self.sintomasWindget = QtWidgets.QTableWidget(self.centralwidget)
        self.sintomasWindget.setGeometry(QtCore.QRect(60, 30, 391, 261))
        self.sintomasWindget.setObjectName("sintomasWindget")
        self.sintomasWindget.setColumnCount(2)
        self.sintomasWindget.setRowCount(len(observables_list))
        
        for i in range(len(observables)):
            item1 = QtWidgets.QTableWidgetItem(observables[i].nombre)
            #item1 = setCheckState(QtCore.Qt.Unchecked)
            #item1 = setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            
            if observables[i].tipo == 'multiple':
                combobox = QComboBox()
                for j in observables[i].valoresPermitidos:
                    combobox.addItem(j)
                
                self.sintomasWindget.setCellWidget(i,1,combobox)
            elif observables[i].tipo=='boleano':
                combobox = QComboBox()
                combobox.addItem('True')
                combobox.addItem('False')
                self.sintomasWindget.setCellWidget(i, 1, combobox)
            
            self.sintomasWindget.setItem(i,0,item1)

        
        item = QtWidgets.QTableWidgetItem()
        self.sintomasWindget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sintomasWindget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sintomasWindget.setHorizontalHeaderItem(1, item)
        
        
        
        
#*************************************************************************# 
        
        
        
        
        self.HipotesisList = QtWidgets.QListWidget(self.centralwidget)
        self.HipotesisList.setGeometry(QtCore.QRect(60, 320, 391, 171))
        self.HipotesisList.setObjectName("HipotesisList")
        
#*************************************************************************# 
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 111, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 300, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 500, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(620, 10, 61, 16))
        self.label_4.setObjectName("label_4")
        
#*************************************************************************# 

        self.DiagnosticoList = QtWidgets.QListWidget(self.centralwidget)
        self.DiagnosticoList.setGeometry(QtCore.QRect(60, 520, 391, 31))
        self.DiagnosticoList.setObjectName("DiagnosticoList")
        
#*************************************************************************#       

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 540, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.diagnostica)
        
        self.cobertura = QtWidgets.QPushButton(self.centralwidget)
        self.cobertura.setGeometry(QtCore.QRect(550, 540, 75, 23))
        self.cobertura.setObjectName("cobertura")
        self.pushButton.clicked.connect(self.coberturaCausal)
        
#*************************************************************************#

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(470, 30, 321, 501))
        self.plainTextEdit.setObjectName("plainTextEdit")
       
        
#*************************************************************************#
        #self.setCentralWidget(self.centralwidget)
        '''self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
'''
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.sintomasWindget.verticalHeaderItem(0)
        #item.setText(_translate("MainWindow", "1"))
        item = self.sintomasWindget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Observable"))
        item = self.sintomasWindget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dolor"))
        self.label.setText(_translate("MainWindow", "Selecciona los Síntomas"))
        self.label_2.setText(_translate("MainWindow", " Hipotesis"))
        self.label_3.setText(_translate("MainWindow", "Diagnostico"))
        self.pushButton.setText(_translate("MainWindow", "Diagnosticar"))
        self.cobertura.setText(_translate("MainWindow", "Cobertura Causal"))
        self.label_4.setText(_translate("MainWindow", "Explicación"))
   
    def diagnostica(self):
        controlador.eventDiagnostica(self)
        
    def coberturaCausal(self):
        #Recolecta datos de las vistas y se lo pasamos al controlador
        # Al pasar self pasamos toda la informaci�n de la ventana
        controlador.eventCoberturaCausal(self)    

if __name__ == '__main__':
    
    app = QApplication(sys.argv[1:])

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())