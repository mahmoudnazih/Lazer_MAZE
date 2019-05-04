import tkinter as tk
from tkinter import *
import socket
import sys
from threading import Thread

class communication:
    def __init__(self, *args, **kwargs):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 10000)
        #print('starting up on %s port %s' % self.server_address)
    def server(self):
        self.s.bind(self.server_address)
        self.s.listen(1)
    def client(self):
        try:
            self.s.connect(self.server_address)
        except:
            pass
    
    def acceptConnections(self):
    
        self.conn,self.addr = self.s.accept()
        #print("Connected")
        self.conn.settimeout(0.010)
                
    def sendData(self,message):
        try:
            self.conn.sendall(message.encode('ascii'))
        
        except:
            pass
    def recieveData(self,message):
        
        try:
            self.data = self.conn.recv(16)
        except:
            pass
    def closeConnection(self):
        self.conn.close()

a=communication()
a.server()

while True:
    
    thread1 = Thread(target=a.acceptConnections, args=()).start() 
        
    try:  
        data = input("Enter Message:")
        a.sendData(data) 

    except:
        break;