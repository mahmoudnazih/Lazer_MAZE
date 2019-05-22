'''
Application for the server program to run the maze
the GUI is based on python tkinter module

'''


import tkinter as tk
from tkinter import *
import socket
import sys
import communication

server = communication.Server() #initiate server for communication

class AppContainer(tk.Frame):
    
    '''
    Setting up the GUI including labels, buttons,....
    '''
    def __init__(self, parent, *args, **kwargs):
        self.btnColors=['#ffeead','#96ceb4','#ff9eb0','#ff6f69','#969595']
        self.displayText=tk.StringVar()
        

        self.displayText.set("Lazer Frenzy Main Panel")
        
        self.level= tk.IntVar() #Variable that we send to client
        
        self.easyImage = PhotoImage(file="easy.png") # Easy mode image
        self.medImage = PhotoImage(file="med.png")  # Medium mode image
        self.hardImage = PhotoImage(file="hard.png")    #hard mode image
        self.bruImage = PhotoImage(file="bru.png")  #brutal mode image
        
        self.logoImage = PhotoImage(file="logo.png") #logo image
        self.startImage = PhotoImage(file="start.png")  # start btn image
        self.stopImage = PhotoImage(file="stop.png")    # stop btn image
        self.resetImage = PhotoImage(file="reset.png")  # reset btn image
        
        super().__init__(parent, *args, **kwargs)

        '''
        Text label that appears at the top of the program and changes
        upon selection of different levels
        '''
        
        self.titleLabel = tk.Label(self,textvariable=self.displayText,anchor='center',bg='#3b5998',border=0,fg='white',width=200,height=60,pady=10,font=("Courier", 15, "bold"))
        self.titleLabel.grid(row = 0, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        self.titleLabel.config(image=self.logoImage,compound="left")
        

        '''
        space between the top section and the rest of the program
        '''
        self.spaceLabel=tk.Label(self,text="",anchor='center',width=200,height=1,pady=0,border=0)
        self.spaceLabel.grid(row = 1, column = 0,columnspan = 4,sticky=(tk.W + tk.E))
        
        

        '''Level one to four Buttons'''
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
        

        '''Space between buttons and the bottom control buttons 
        start, stop, reset
        '''
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

        '''Called when level on is selected'''
    def levelOneSelection(self):
        self.levelOneBtn.configure(bg = self.btnColors[0])
        self.levelTwoBtn.configure(bg = "white")
        self.levelThreeBtn.configure(bg = "white")
        self.levelFourBtn.configure(bg = "white")
        self.stopBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.startBtn.configure(bg="#fefefe",fg='#0aaf9d')
        self.displayText.set("Level 1 Selected") #display at the top 
        self.level.set(1)       # set the level to 1
        
        
        
        
        
        
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
        

        ''' Sends the value of level to client when clicked'''
    def onStart(self):
        self.startBtn.configure(bg=self.btnColors[4],fg="#fefefe")
        self.stopBtn.configure(bg="#fefefe",fg='#0aaf9d')
        level = str(self.level.get())
        server.run(level)   #Send the level to the client
        
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
    


  

