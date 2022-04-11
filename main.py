from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('form.ui', self)
        self.setButtons()
        self.createStatusBar()
        self.show()


    def setButtons(self):
        self.stopButton.clicked.connect(lambda: self.stopButtonClicked())
        self.stopButton.setStyleSheet("background-color : red")
        self.startButton.clicked.connect(lambda: self.startButtonClicked())
        self.startButton.setStyleSheet("background-color : green")

    def stopButtonClicked(self):
        print("stop button clicked")
    def startButtonClicked(self):
        print("start button clicked")

    def createStatusBar(self):
        self.statusBar().showMessage("Ready")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
