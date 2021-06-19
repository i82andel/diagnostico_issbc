# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 22:53:31 2021

@author: youne
"""

import sys
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget,QTableWidgetItem, QMainWindow, QAction, QApplication, QPushButton, QLabel, QDesktopWidget, QLineEdit, QComboBox,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


        
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        
        
    


    def initUI(self):
        
        header = ['NOMBRE', 'VALOR']

        self.createTable()
        
        #self.tableWidget.setColumnWidth(0, 500)
        #self.tableWidget.setColumnWidth(1, 250)
        
        #self.tableWidget.setHorizontalHeaderLabels(header) #Asigna etiquetas a las columnas
       
#*************************************************************************# 
       

        self.setGeometry(700, 700, 1000, 700)
        self.setWindowTitle('Diagnostico')
        self.center()
        self.show()
        
    def createTable(self):
        
        vbox = QVBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setColumnCount(2)
        tableWidget.setRowCount(4)
        tableWidget.setItem(0,0, QTableWidgetItem("NAME"))
        
        vbox.addWidget(tableWidget)
        self.setLayout(vbox)
       
        
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    
     
           
   
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()