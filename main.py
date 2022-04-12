from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import * #QMessageBox,QAction, QToolTip, QStackedWidget, QHBoxLayout, QVBoxLayout, QSplitter, QFormLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem
#from PyQt5.QtWidgets import * QApplication, QFileSystemModel, QTreeView, QWidget, QHeaderView
from PyQt5.QtGui import *# QPainter, QBrush, QPen, QColor, QFont, QIcon
from PyQt5.QtCore import *# Qt, QPoint, QRect, QObject, QEvent, pyqtSignal, pyqtSlot, QSize, QDir

import sys
import socket
from client import Client
from sftp import SFTPClient
from threading import *

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        self.ui = uic.loadUi('form.ui', self)
        self.setButtons()
        self.setLineEdits()
        self.createStatusBar()
        self.show()
        self.cl = Client()
        self.cl.createClient()
        self.thread()
        self.messageArray=[]
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)

    def setLineEdits(self):
        self.timeValidator = QIntValidator(10,600,self)
        self.timeEdit.setValidator(self.timeValidator)
        self.speedValidator=QIntValidator(0,50,self)
        self.speedEdit.setValidator(self.speedValidator)

    def setButtons(self):
        self.stopButton.clicked.connect(lambda: self.stopButtonClicked())
        self.stopButton.setStyleSheet("background-color : red")
        self.startButton.clicked.connect(lambda: self.startButtonClicked())
        self.startButton.setStyleSheet("background-color : green")
        self.downloadButton.clicked.connect(lambda: self.downloadButtonClicked())

    def stopButtonClicked(self):
        self.cl.sendMessage("STOP")
    def startButtonClicked(self):
        if self.speedEdit.text().isdigit() and self.timeEdit.text().isdigit():
            self.cl.sendMessage(f"START {self.speedEdit.text()} {self.timeEdit.text()}")
        else:
            QMessageBox.question(self, 'Wrong input', "Passed parameters was wrong", QMessageBox.Ok)

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")
    def thread(self):
        self.t1=Thread(target=self.cl.readIncome,args=(self.ui,))
        self.t1.start()
        

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.cl.sendMessage("STOP")
            self.cl.sendMessage("QUIT")
            self.cl.connect=False
            self.t1.join()
            #self.t1.terminate()
            self.cl.closeClient()
            print('Window closed')
        else:
            event.ignore()
    
    def downloadButtonClicked(self):
        self.sftp = SFTPClient()
        self.path = QFileDialog.getSaveFileName(self, 'Save File',"testbench.log")
        self.sftp.getFile(self.path[0])
        self.sftp.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
