import tkinter as tk
from tkinter import *
import socket
import sys
from threading import Thread

class communication:
    connections=[]
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
        thread1 = Thread(target=self.sendData)
        thread1.daemon=True
        thread1.start()
        self.connections.append(self.conn)
        
    def sendData(self):
            
             
            while True:
                self.data=input("Enter Message: ")
                self.conn.send(bytes(self.data,'utf-8'))
                    
    
    def recieveData(self):
        
        while True:
            self.data = self.s.recv(1024)
            self.data=self.data.decode('ascii')
            if not self.data:
                break
        self.conn.close()

a=communication()
a.server()
while True:
    a.acceptConnections()   
