from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox,QAction, QToolTip, QStackedWidget, QHBoxLayout, QVBoxLayout, QSplitter, QFormLayout, QLabel, QFrame, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QFileSystemModel, QTreeView, QWidget, QHeaderView
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QFont, QIcon
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, QEvent, pyqtSignal, pyqtSlot, QSize, QDir

import sys
import socket
from client import Client
from threading import *

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        self.ui = uic.loadUi('form.ui', self)
        self.setButtons()
        self.createStatusBar()
        self.show()
        self.cl = Client()
        self.cl.createClient()
        self.thread()
        quit = QAction("Quit", self)
        quit.triggered.connect(self.closeEvent)


    def setButtons(self):
        self.stopButton.clicked.connect(lambda: self.stopButtonClicked())
        self.stopButton.setStyleSheet("background-color : red")
        self.startButton.clicked.connect(lambda: self.startButtonClicked())
        self.startButton.setStyleSheet("background-color : green")

    def stopButtonClicked(self):
        print("stop button clicked")
        self.cl.sendMessage("STOP")
    def startButtonClicked(self):
        print("start button clicked")
        self.cl.sendMessage("START 55 120")

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")
    def thread(self):
        self.t1=Thread(target=self.cl.readIncome)
        self.t1.start()
        

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
            self.cl.sendMessage("STOP")
            self.cl.sendMessage("QUIT")
            self.cl.connect=False
            self.t1.join()
            self.t1.terminate()
            self.cl.closeClient()
            print('Window closed')
        else:
            event.ignore()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
