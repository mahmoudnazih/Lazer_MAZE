import socket
import select
import threading
import sys
port = 5005
address = "localhost"

class Server:

    connections=[]
    threads=[]
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self):
        self.sock.bind((address,port))
        self.sock.listen(1)
        inputs=[self.sock]
        self.c,self.a = self.sock.accept()
        self.connections.append(self.c)
        

    def handler(self,c,a,msg):
        while True:
            data=msg
            for connection in self.connections:
                try:
                    connection.sendall(data.encode('ascii'))
                    self.cThread.join()
                    self.iThread.join()
                    break
                    
                except:
                    pass
            break
    def run(self,msg):
        
        while True:
            try:
                iThread = threading.Thread(target=self.accepConnections, args=())
                iThread.daemon=True
                iThread.start()
                
                cThread = threading.Thread(target=self.handler, args=(self.c,self.a,msg))
                cThread.daemon=True
                cThread.start()
                
                break
            except:
                pass
    def accepConnections(self):
        while True:
            try:
                
                self.c,self.a = self.sock.accept()
                self.connections.append(self.c)
                
                break
            except:
                pass
            



class Client:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self):
        self.sock.connect((address,port))
    def info(self):
        while True:
            try:
                self.data = self.sock.recv(1024)
                self.data = str(self.data,'utf-8')
                return self.data
                if not self.data:
                    break
            except:
                self.sock.close()
                self.sock.connect((address,port))
                self.data = self.sock.recv(1024)
                self.data = str(self.data,'utf-8')
                return self.data
                if not self.data:
                    break
