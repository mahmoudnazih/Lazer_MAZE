import tkinter as tk
from tkinter import *
import socket
import sys
import communication


server = communication.Server()
class AppContainer(tk.Frame):
    
    def __init__(self, parent, *args, **kwargs):
        self.btnColors=['#ffeead','#96ceb4','#ff9eb0','#ff6f69','#969595']
        self.displayText=tk.StringVar()
        self.displayText.set("Lazer Frenzy Main Panel")
        self.level= tk.IntVar()
        self.easyImage = PhotoImage(file="easy.png")
        self.medImage = PhotoImage(file="med.png")
        self.hardImage = PhotoImage(file="hard.png")
        self.bruImage = PhotoImage(file="bru.png")
        
        self.logoImage = PhotoImage(file="logo.png")
        self.startImage = PhotoImage(file="start.png")
        self.stopImage = PhotoImage(file="stop.png")
        self.resetImage = PhotoImage(file="reset.png")
        super().__init__(parent, *args, **kwargs)
        
        self.titleLabel = tk.Label(self,textvariable=self.displayText,anchor='center',bg='#3b5998',border=0,fg='white',width=200,height=60,pady=10,font=("Courier", 15, "bold"))
        self.titleLabel.grid(row = 0, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        self.titleLabel.config(image=self.logoImage,compound="left")
        
        self.spaceLabel=tk.Label(self,text="",anchor='center',width=200,height=1,pady=0,border=0)
        self.spaceLabel.grid(row = 1, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        
        self.levelOneBtn = tk.Button(self,text="",command=self.levelOneSelection,width=50,height=60,pady=10,border=0,bg='white',font=("Courier", 13, "bold"))
        self.levelOneBtn.grid(row=2,column=0,columnspan =4,sticky=(tk.W + tk.E))
        self.levelOneBtn.config(image=self.easyImage,compound="left")
       
        
        self.levelTwoBtn = tk.Button(self,text="",command=self.levelTwoSelection,width=50,height=60,pady=10,border=0,bg='white',fg='yellow',font=("Courier", 13, "bold"))
        self.levelTwoBtn.grid(row=3,column=0,columnspan =4,sticky=(tk.W + tk.E))
        self.levelTwoBtn.config(image=self.medImage,compound="left")
       
        
        self.levelThreeBtn = tk.Button(self,text="",command=self.levelThreeSelection,width=50,height=60,pady=10,border=0,bg='white',fg='black',font=("Courier", 13, "bold"))
        self.levelThreeBtn.grid(row=4,column=0,columnspan =4,sticky=(tk.W + tk.E))
        self.levelThreeBtn.config(image=self.hardImage,compound="left")
        
        
        self.levelFourBtn = tk.Button(self,text="",command=self.levelFourSelection,width=50,height=60,pady=10,border=0,bg='white',fg='black',font=("Courier", 13, "bold"))
        self.levelFourBtn.grid(row=5,column=0,columnspan =4,sticky=(tk.W + tk.E))
        self.levelFourBtn.config(image=self.bruImage,compound="left")
        
        self.spaceLabel=tk.Label(self,text="",anchor='center',width=200,height=1,border=0,pady=0)
        self.spaceLabel.grid(row =6, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        self.startBtn = tk.Button(self,text="Start",command=self.onStart,width=100,height=30,pady=10,border=0,bg="#fefefe",fg='#0aaf9d',font=("Courier", 12, "bold"))
        self.startBtn.config(image=self.startImage,compound="left")
        self.startBtn.grid(row=7,column=0,columnspan =1)
        
        self.stopBtn = tk.Button(self,text="Stop",command=self.onStop,width=100,height=30,pady=10,border=0,bg="#fefefe",fg='#0aaf9d',font=("Courier", 12, "bold"))
        self.stopBtn.config(image=self.stopImage,compound="left")
        self.stopBtn.grid(row=7,column=1,columnspan =1)
        
        self.resetBtn = tk.Button(self,text="Reset",command=self.onReset,width=100,height=30,pady=10,border=0,bg="#fefefe",fg='#0aaf9d',font=("Courier", 12, "bold"))
        self.resetBtn.config(image=self.resetImage,compound="left")
        self.resetBtn.grid(row=7,column=2,columnspan =1)
        
        self.columnconfigure(1, weight=1)
    def levelOneSelection(self):
        self.levelOneBtn.configure(bg = self.btnColors[0])
        self.levelTwoBtn.configure(bg = "white")
        self.levelThreeBtn.configure(bg = "white")
        self.levelFourBtn.configure(bg = "white")
        self.stopBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.startBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.displayText.set("Level 1 Selected")
        self.level.set(1)
        
        
        
        
        
        
    def levelTwoSelection(self):
        self.levelOneBtn.configure(bg = "white")
        self.levelTwoBtn.configure(bg = self.btnColors[1])
        self.levelThreeBtn.configure(bg = "white")
        self.levelFourBtn.configure(bg = "white")
        self.stopBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.startBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.displayText.set("Level 2 Selected")
        self.level.set(2)
        
    def levelThreeSelection(self):
        self.levelOneBtn.configure(bg = "white")
        self.levelTwoBtn.configure(bg = "white")
        self.levelThreeBtn.configure(bg = self.btnColors[2])
        self.levelFourBtn.configure(bg = "white")
        self.stopBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.startBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.displayText.set("Level 3 Selected")
        self.level.set(3)
        
    def levelFourSelection(self):
        self.levelOneBtn.configure(bg = "white")
        self.levelTwoBtn.configure(bg = "white")
        self.levelThreeBtn.configure(bg = "white")
        self.levelFourBtn.configure(bg = self.btnColors[3])
        self.stopBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.startBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.displayText.set("Level 4 Selected")
        self.level.set(4)
        
    def onStart(self):
        self.startBtn.configure(bg=self.btnColors[4],fg="#fefefe")
        self.stopBtn.configure(bg="#fefefe",fg='#0aaf9d')
        level = str(self.level.get())
        server.run(level)
    def onStop(self):
        self.stopBtn.configure(bg=self.btnColors[4],fg="#fefefe")
        self.startBtn.configure(bg="#fefefe",fg='#0aaf9d')
        server.run('stop')
    def onReset(self):
            self.levelOneBtn.configure(bg ='white' )
            self.levelTwoBtn.configure(bg = 'white')
            self.levelThreeBtn.configure(bg = 'white')
            self.levelFourBtn.configure(bg = 'white')
            self.stopBtn.configure(bg="#fefefe",fg='#0aaf9d')
            self.startBtn.configure(bg="#fefefe",fg='#0aaf9d')
            self.displayText.set("Lazer Frenzy Main Panel")
            self.level.set(0)
            level = str(self.level.get())
            server.run(level)

            
            
            
class AppInterface(tk.Tk):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.title("Lazer Frenzy")
        self.geometry("600x480")
        self.resizable(width=True, height=True)
        AppContainer(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = AppInterface()
    app.mainloop()
    


  

