import time
import RPi.GPIO as GPIO
import pygame
import random

#Sound Class
class Sound:
    def __init__(self):
        self.sounds=["winSound.wav","errorSound.wav","gameSound.wav","loseSound.wav","success.wav"]
        
        
    #Plays the Buzzer Sound when a laser beam hits a player
    def buzzer(self):
        error_sound = pygame.mixer.Sound(self.sounds[1])
        pygame.mixer.Sound.play(error_sound)
    
    #Game Music in BackGround runs all over the game game
    def gameSound(self):
        game_sound = pygame.mixer.music.load(self.sounds[2])
        pygame.mixer.music.play(-1)
    
    #Win Sound runs if the player wins at the end of the game
    def winSound(self):
        pygame.mixer.music.load(self.sounds[0])
        pygame.mixer.music.play(1)
    
    #Loss Sound runs if the player Losses at the end of the game
    def loseSound(self):
        pygame.mixer.music.load(self.sounds[3])
        pygame.mixer.music.play(1)
    
    def pointsSound(self):
        pygame.mixer.music.load(self.sounds[4])
        pygame.mixer.music.play(1)
        
    #Pauses the Game Music
    def pause(self):
        pygame.mixer.music.pause()
    
    #Unpauses the game Music
    def unpause(self):
        pygame.mixer.music.unpause()
    def stopSound(self):
        pygame.mixer.music.stop()

#Laser Class
class laserGroup:
    def __init__(self):
        self.systemLasers = 5
        #Output Pins for Switching lasers on/off
        self.LazerPin_1 = 7
        self.LazerPin_2 = 11
        self.LazerPin_3 = 13
        self.LazerPin_4 = 15
        self.LazerPin_5 = 19
        #Concatinating pins in an array
        self.LazerPins = [self.LazerPin_1,self.LazerPin_2,self.LazerPin_3,self.LazerPin_4,self.LazerPin_5]
        for i in range(len(self.LazerPins)):
            GPIO.setup(self.LazerPins[i],GPIO.OUT)
        
    def turnOn(self,NumberOfLasers):         #Turns on # ofLasers in sequence
        for n in range(NumberOfLasers):
            GPIO.output(self.LazerPins[n],True)
    
    def turnOff(self,NumberOfLasers):         #Turns off # ofLasers in sequence
        for n in range(NumberOfLasers):
            GPIO.output(self.LazerPins[n],False)
            
    def randomTurnOn(self,NumberOfLasers):         #Turns on # ofLasers randomly
        for n in range(NumberOfLasers):
            GPIO.output(self.LazerPins[random.randrange(0, self.systemLasers, 1)],True)
        
    def randomTurnOff(self,NumberOfLasers):         #Turns off #ofLasers randomly
        for n in range(NumberOfLasers):
            GPIO.output(self.LazerPins[random.randrange(0, self.systemLasers, 1)],False)
            
#Sensors Class
class sensorGroup:
    def __init__(self):
        #Input Pins for reading sensors data
        self.SensorPin_1 = 8
        self.SensorPin_2 = 10
        self.SensorPin_3 = 12
        self.SensorPin_4 = 16
        self.SensorPin_5 = 18
        #Concatinating pins in an array
        self.SensorPins = [self.SensorPin_1,self.SensorPin_2,self.SensorPin_3,self.SensorPin_4,self.SensorPin_5]
        for i in range(len(self.SensorPins)):
            GPIO.setup(self.SensorPins[i],GPIO.IN)
    def readSensors(self,NumberOfSensors):
        SensorValues = [0,0,0,0,0]
        for n in range(NumberOfSensors):
            SensorValues[n] = GPIO.input(self.SensorPins[n])
        return SensorValues
#Output Buttons Class
class outputBtnGroup:
    def __init__(self):
        self.Button1PinOUT = 29
        self.Button2PinOUT = 31
        self.Button3PinOUT = 33
        self.Button4PinOUT = 35
        self.Button5PinOUT = 37
        self.ButtonPinsOUT = [self.Button1PinOUT,self.Button2PinOUT,self.Button3PinOUT,self.Button4PinOUT,self.Button5PinOUT]
        for i in range(len(self.ButtonPinsOUT)):
            GPIO.setup(self.ButtonPinsOUT[i],GPIO.OUT)
    def setBtnHigh(self,noOfBtns):
        for i in range(noOfBtns):
            GPIO.output(self.ButtonPinsOut[i],True)
    def setBtnLow(self,noOfBtns):
        for i in range(noOfBtns):
            GPIO.output(self.ButtonPinsOut[i],False)
            
            
#Output Buttons Class
class inputBtnGroup:
    def __init__(self):
        self.Button1PinIN = 24
        self.Button2PinIN = 26
        self.Button3PinIN = 32
        self.Button4PinIN = 36
        self.Button5PinIN = 38
        self.ButtonPinsIN = [self.Button1PinIN,self.Button2PinIN,self.Button3PinIN,self.Button4PinIN,self.Button5PinIN]
        for i in range(len(self.ButtonPinsIN)):
            GPIO.setup(self.ButtonPinsIN[i],GPIO.IN)
    def readBtn(self,NumberOfBtns):
        btnsValues = [0,0,0,0,0]
        for n in range(NumberOfBtns):
            btnsValues[n] = GPIO.input(self.ButtonPinsIN[n])
        return btnsValues

class controlGroup:
    def __init__(self):
        #Define the playing time of each level in seconds
        self.Level_1_Time = 50
        self.Level_2_Time = 70
        self.Level_3_Time = 100
        self.Level_4_Time = 120
        self.WinPin = 22
        self.BuzzerPin = 21
        self.celebPin = 23
        GPIO.setup(self.BuzzerPin,GPIO.OUT)
        GPIO.setup(self.celebPin,GPIO.OUT)
        GPIO.setup(self.WinPin,GPIO.IN)

class player():
    def __init__(self):
        self.levelOneScore = 40
        self.levelTwoScore = 60
        self.levelThreeScore = 80
        self.levelFourScore = 100
        self.errors = 0
    def decreaseScore(self,numberOfErrors):
        pass
    def increaseScore(self):
        pass
    def mistakes(self):
        self.errors +=1 
        return self.errors
    def playTime(self):
        pass

def generalSetup():
    
    pygame.init()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
def main_program():
    generalSetup()
    
    #Instance of called classes
    sound = Sound()
    laser = laserGroup()
    sensor = sensorGroup()
    outputBtn = outputBtnGroup()
    inputBtn = inputBtnGroup()
    control = controlGroup()
    
    laser.systemLasers = 5    #Number of all lasers in the maze

    laser.turnOn(3)
    sound.gameSound()
    time.sleep(13)
    sound.pause()
    sound.buzzer()
    time.sleep(2.5)
    sound.unpause()
    time.sleep(10)
    sound.pause()
    sound.buzzer()
    time.sleep(2.5)
    sound.unpause()
    sound.loseSound()
    
main_program()
        