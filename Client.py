import communication
import sys
from LaserFrenzyOperation import *

client = communication.Client()

sound = Sound()
laser = laserGroup()
sensor = sensorGroup()
outputBtn = outputBtnGroup()
inputBtn = inputBtnGroup()
control = controlGroup()
playerOne = player()


while True:
    data = str(client.info())
    if data == '1':
        timerInit = 0
        score = 40
        while True:
            if timerInit==0:
                initialTime = time.time()   
            
            currentTime = time.time()-initialTime
            remainingTime = control.Level_1_Time() - currentTime
            
            if remainingTime>0:
                
                laser.turnOn(2)
                sound.gameSound()
                sensorsReadings = sensor.readSensors(2)
                for i in range(len(sensorsReadings)):
                    if i:
                        sound.pause()
                        sound.buzzer()
                        #Red Light
                        score = score - 5
                sound.unpause()
                
                currentTime = time.time()-initialTime
                remainingTime = control.Level_1_Time() - currentTime
                if (remainingTime > 37 and remainingTime <41) or (remainingTime > 27 and remainingTime <31) or (remainingTime > 17 and remainingTime <21):
                    outputBtn.setBtnHigh(3)
                    btnReadings = inputBtn.readBtn(3)
                    for i in range(len(btnReadings)):
                        if i:
                            score = score + 10
                            sound.pause()
                            sound.pointsSound()
                            sound.unpause()
                else:
                    outputBtn.setBtnLow(3)
                    
                
            else:
                break
    elif data == '2':
        timerInit = 0
        score = 60
        while True:
            if timerInit==0:
                initialTime = time.time()   
            
            currentTime = time.time()-initialTime
            remainingTime = control.Level_2_Time() - currentTime
            
            if remainingTime>0:
                
                laser.turnOn(3)
                sound.gameSound()
                sensorsReadings = sensor.readSensors(3)
                for i in range(len(sensorsReadings)):
                    if i:
                        sound.pause()
                        sound.buzzer()
                        #Red Light
                        score = score - 5
                sound.unpause()
                
                currentTime = time.time()-initialTime
                remainingTime = control.Level_1_Time() - currentTime
                if (remainingTime > 45 and remainingTime <51) or (remainingTime > 35 and remainingTime <41) or (remainingTime > 25 and remainingTime <31):
                    outputBtn.setBtnHigh(3)
                    btnReadings = inputBtn.readBtn(3)
                    for i in range(len(btnReadings)):
                        if i:
                            score = score + 10
                            sound.pause()
                            sound.pointsSound()
                            sound.unpause()
                else:
                    outputBtn.setBtnLow(3)
                    
                
            else:
                break
    elif data == '3':
        sound.gameSound()
        laser.turnOn(4)
    elif data == '4':
        sound.gameSound()
        laser.turnOn(5)
    elif data=='stop':
        print('stop')
        
