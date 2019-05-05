class Server:
    connections=[]
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def __init__(self):
        self.sock.bind(("localhost",5050))
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
    def __init__(self,"localhost"):
        self.sock.connect(("localhost",5050))
        while True:
            data = self.sock.recv(1024)
            print(str(data,'utf-8'))
            if not data:
                break
