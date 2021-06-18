# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vista.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

class MainWindow(QMainWindow):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi()
        
        
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(839, 630)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        
#*************************************************************************#         
        
        
        self.sintomasWindget = QtWidgets.QTableWidget(self.centralwidget)
        self.sintomasWindget.setGeometry(QtCore.QRect(60, 30, 391, 261))
        self.sintomasWindget.setObjectName("sintomasWindget")
        self.sintomasWindget.setColumnCount(2)
        self.sintomasWindget.setRowCount(1)
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

        self.DiagnosticoList = QtWidgets.QListView(self.centralwidget)
        self.DiagnosticoList.setGeometry(QtCore.QRect(60, 520, 391, 31))
        self.DiagnosticoList.setObjectName("DiagnosticoList")
        
#*************************************************************************#       

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(600, 540, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
#*************************************************************************#

        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(470, 30, 321, 501))
        self.plainTextEdit.setObjectName("plainTextEdit")
       
        
#*************************************************************************#
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.sintomasWindget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.sintomasWindget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Observable"))
        item = self.sintomasWindget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Dolor"))
        self.label.setText(_translate("MainWindow", "Selecciona los Síntomas"))
        self.label_2.setText(_translate("MainWindow", " Hipotesis"))
        self.label_3.setText(_translate("MainWindow", "Diagnostico"))
        self.pushButton.setText(_translate("MainWindow", "Diagnosticar"))
        self.label_4.setText(_translate("MainWindow", "Explicación"))
   


if __name__ == '__main__':
    
    app = QApplication(sys.argv[1:])

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())