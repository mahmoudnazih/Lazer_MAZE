import tkinter as tk
from tkinter import *
import socket
import sys

class communication:
    def __init__(self, *args, **kwargs):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 10000)
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
    def closeConnection(self):
        self.s.close()

class AppContainer(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        self.btnColors=['#ffeead','#96ceb4','#ff6f69','red']
        self.displayText=tk.StringVar()
        self.displayText.set("Lazer Frenzy Main Panel")
        self.level= tk.IntVar()
        super().__init__(parent, *args, **kwargs)
        
        self.titleLabel = tk.Label(self,textvariable=self.displayText,anchor='center',bg='brown',fg='black',width=200,height=2,pady=10,bd=4)
        self.titleLabel.grid(row = 0, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        self.spaceLabel=tk.Label(self,text="",anchor='center',width=200,height=1,pady=0,bd=4)
        self.spaceLabel.grid(row = 1, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        self.levelOneBtn = tk.Button(self,text="Level One",command=self.levelOneSelection,width=50,height=2,pady=10,bg='#ffeead',fg='black',font=("Courier", 10, "bold"))
        self.levelOneBtn.grid(row=2,column=0,columnspan =4,sticky=(tk.W + tk.E))
        
        self.spaceLabel=tk.Label(self,text="",anchor='center',width=200,height=1,pady=0)
        self.spaceLabel.grid(row = 3, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        self.levelTwoBtn = tk.Button(self,text="Level Two",command=self.levelTwoSelection,width=50,height=2,pady=10,bg='#96ceb4',fg='black',font=("Courier", 10, "bold"))
        self.levelTwoBtn.grid(row=4,column=0,columnspan =4,sticky=(tk.W + tk.E))
        
        self.spaceLabel=tk.Label(self,text="",anchor='center',width=200,height=1,pady=0)
        self.spaceLabel.grid(row = 5, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        self.levelThreeBtn = tk.Button(self,text="Level Three",command=self.levelThreeSelection,width=50,height=2,pady=10,bg='#ff6f69',fg='black',font=("Courier", 10, "bold"))
        self.levelThreeBtn.grid(row=6,column=0,columnspan =4,sticky=(tk.W + tk.E))
        
        self.spaceLabel=tk.Label(self,text="",anchor='center',width=200,height=1,pady=0)
        self.spaceLabel.grid(row = 7, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        self.levelFourBtn = tk.Button(self,text="Level Four",command=self.levelFourSelection,width=50,height=2,pady=10,bg='red',fg='black',font=("Courier", 10, "bold"))
        self.levelFourBtn.grid(row=8,column=0,columnspan =4,sticky=(tk.W + tk.E))
        
        self.spaceLabel=tk.Label(self,text="",anchor='center',width=200,height=1,pady=0)
        self.spaceLabel.grid(row =9, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        self.startBtn = tk.Button(self,text="Start",command=self.onStart,width=15,height=2,pady=10,bg='green',fg='black',font=("Courier", 10, "bold"))
        self.startBtn.grid(row=10,column=0,columnspan =1)
        
        self.stopBtn = tk.Button(self,text="Stop",command=self.onStop,width=20,height=2,pady=10,bg='brown',fg='black',font=("Courier", 10, "bold"))
        self.stopBtn.grid(row=10,column=1,columnspan =1)
        
        self.resetBtn = tk.Button(self,text="Reset",command=self.onReset,width=15,height=2,pady=10,bg='purple',fg='white',font=("Courier", 10, "bold"))
        self.resetBtn.grid(row=10,column=2,columnspan =1)
        
        self.columnconfigure(1, weight=1)
    def levelOneSelection(self):
        self.levelOneBtn.configure(bg = "red")
        self.levelTwoBtn.configure(bg = "white")
        self.levelThreeBtn.configure(bg = "white")
        self.levelFourBtn.configure(bg = "white")
        self.displayText.set("Level 1 Selected")
        self.level.set(1)
        print(self.level.get())
        
    def levelTwoSelection(self):
        self.levelOneBtn.configure(bg = "white")
        self.levelTwoBtn.configure(bg = "red")
        self.levelThreeBtn.configure(bg = "white")
        self.levelFourBtn.configure(bg = "white")
        self.displayText.set("Level 2 Selected")
        self.level.set(2)
        print(self.level.get())
    def levelThreeSelection(self):
        self.levelOneBtn.configure(bg = "white")
        self.levelTwoBtn.configure(bg = "white")
        self.levelThreeBtn.configure(bg = "red")
        self.levelFourBtn.configure(bg = "white")
        self.displayText.set("Level 3 Selected")
        self.level.set(3)
        print(self.level.get())
    def levelFourSelection(self):
        self.levelOneBtn.configure(bg = "white")
        self.levelTwoBtn.configure(bg = "white")
        self.levelThreeBtn.configure(bg = "white")
        self.levelFourBtn.configure(bg = "red")
        self.displayText.set("Level 4 Selected")
        self.level.set(4)
        print(self.level.get())
    def onStart(self):
        pass
    def onStop(self):
        pass
    def onReset(self):
            self.levelOneBtn.configure(bg = self.btnColors[0],bd=3)
            self.levelTwoBtn.configure(bg = self.btnColors[1])
            self.levelThreeBtn.configure(bg = self.btnColors[2])
            self.levelFourBtn.configure(bg = self.btnColors[3])
            self.displayText.set("Lazer Frenzy Main Panel")
            self.level.set(0)
            print(self.level.get())
            
class AppInterface(tk.Tk):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.title("Lazer Frenzy")
        self.geometry("800x600")
        self.resizable(width=True, height=True)
        AppContainer(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        #self.var = AppContainer(self).level.get()
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = AppInterface()
    app.mainloop()
    #print(app.var)


  

