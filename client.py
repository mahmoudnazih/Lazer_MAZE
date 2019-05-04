import tkinter as tk
from tkinter import *
import socket
import sys

class communication:
    def __init__(self, *args, **kwargs):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 10000)
        print('starting up on %s port %s' % self.server_address)
    def server(self):
        self.s.bind(self.server_address)
        self.s.listen(1)
    def client(self):
        self.s.connect(self.server_address)
    def acceptConnections(self):
        
        self.conn,self.addr = self.s.accept()
        self.conn.settimeout(0.010)
    def sendData(self,message):
        
        try:
            self.s.sendall(message)
        except:
            pass
    def recieveData(self):
        
        try:
            self.data = self.s.recv(1024)
            self.data=self.data.decode('ascii')
            
        except:
            pass
        return self.data
    def closeServerConnection(self):
        self.conn.close()
    def closeClientConnection(self):
        self.s.close()

a=communication()
a.client()
while True:
    try:
        data=a.recieveData()
        if not data:
            break
        print(data)
    except:
        a.closeClientConnection()

