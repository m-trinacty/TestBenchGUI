from curses.ascii import NUL
import socket
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class Client(QObject):
    def __init__(self):
        super(Client, self).__init__()
        self.IP = "192.168.151.1"
        self.PORT = 1500
        self.ADDR = (self.IP, self.PORT)
        self.SIZE = 1024
        self.FORMAT = "ISO-8859-1"
        self.client = NUL

    def createClient(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.connect = True

        
            
        
    def closeClient(self):
        print("Connection ended")
        self.client.close()
    

    def sendMessage(self,msg):
        print(f"Sending: {msg}")
        #msg = str(input("InputMesaage:"))
        strLen=len(msg)
        sendMsg= list(msg)
        for x in range(strLen,128):
            sendMsg.append('\0')
        self.client.send(bytes(msg,self.FORMAT))    

    
    def readIncome(self,ui):
        

        while self.connect:
            
            data = self.client.recv(self.SIZE)

            serverMsg= data.decode(self.FORMAT)
            serverMsg = serverMsg.split('\0')
            ui.logText.append(serverMsg[0])
            print(f"[SERVER] {serverMsg[0]}")