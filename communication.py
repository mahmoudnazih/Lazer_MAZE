import socket
import select
import threading
import sys
port = 5005
address = "localhost"
class Server:
    connections=[]
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self):
        self.sock.bind((address,port))
        self.sock.listen(1)
        inputs=[self.sock]

    def handler(self,c,a):
        while True:
            data=input("Enter Message: ")
            for connection in self.connections:
                try:
                    connection.sendall(data.encode('ascii'))
                except:
                    pass
    def run(self):
        while True:
            c,a = self.sock.accept()
            self.connections.append(c)
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.daemon=True
            cThread.start()

class Client:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self):
        self.sock.connect((address,port))
    def info(self):
        while True:
            self.data = self.sock.recv(1024)
            return str(self.data,'utf-8')
            if not self.data:
                break
