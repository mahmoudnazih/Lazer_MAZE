'''
Imported Modules
---------------------
communication module: has the implementation of server and client
LaserFrenzyOperation: has the implementaion on,sound,effects and GPIO 
and their manipulation

'''

import communication
import sys
from LaserFrenzyOperation import *
import numpy as np

'''
Called Classes:
-------------------
Client> Recieving data
sound> Sound Collection
Laser> Laser Sources
sensor> Laser sensors
outputBtn> Refers to Leds on the Btns
inputBtn> Btns that users will interact with to get score
control> some settings like levels time and win pin 
'''

client = communication.Client()    
sound = Sound()     
laser = laserGroup()
sensor = sensorGroup()
outputBtn = outputBtnGroup()
inputBtn = inputBtnGroup()
control = controlGroup()
playerOne = player()
control.generalSetup()
flag = False            #Used to begin the calculation of initial time
while True:             # The Main program loop
    
    data = client.info()    #Recieve the game level (data)
    flag = True             # Set the flag to True to initialize time calculations
    
    if data =='1':          # If recieved data is equal to 1 means easy level
        score = 0
        f1 = True
        f2 = True
        f3 = True
        f4 = True
        f1_randomBtns = True
        f2_randomBtns = True
        f3_randomBtns = True
        f4_randomBtns = True
        randomBtns = 0
        while True:         # Level 1 running loop
            
            if flag:        # The game time starts at this moment
                
                '''set the flag to false in order not to start
                the time calculations each iteration of the loop '''
                
                initialTime = time.time()
                flag = False   
                
            '''Culculate the current time and the game remaining time depending 
            on the game level '''
            
            currentTime = time.time()-initialTime
            remainingTime = control.Level_1_Time() - currentTime
            
            ''' Actual Game operation'''
            ''' Checks if the game time is greater than zero
            which means the player has time to continue playing'''
            
            
            if remainingTime>0:
    
                ''' In Level 1 Two laser sources will be turned on 
                the turn on will be in sequence for example: if the game has five
                laser sources at pins 1,2,3,4,5 the sources at pins 1 and 2 will
                be turned on
                '''
                laser.turnOn(2)         #Turn on 2 Laser Sources
                sound.gameSound()       # Play the background music
                
                '''Read the sensors for any user interception the first two sensors 
                data will be read at level 1
                 '''
                sensorsReadings = sensor.readSensors(2)
                for i in sensorsReadings: # Checks for intercepted beams
                    if i:   

                        '''If there is any user interaction with the beams 
                        1- pause the background music
                        2- Play the Buzzer sound
                        3- Decrease score by 5 points
                        '''
                        sound.pause()
                        sound.buzzer()
                        #Red Light
                        control.makeBuzzer()
                        
                        score = score - 5
                        time.sleep(1)
                sound.unpause() # Continue playing the background music
                
                
                
                
                # if (remainingTime > 37 and remainingTime <41) or (remainingTime > 27 and remainingTime <31) or (remainingTime > 17 and remainingTime <21):
                #     '''
                #     During a period of 3 seconds each 10 secs 3 Buttons Leds will
                #      turn on They are in sequence as well
                #     operation:
                #     1- Read if any of them is pressed
                #         if any btn is pressed
                #         1- increase the score by 10 points
                #         2- pause the background music
                #         3- play collectin points sound

                #     The time that not in this period the LEDS will be off
                #     '''

                #     outputBtn.setBtnHigh(3)             #Turn on Btns LEDS
                #     btnReadings = inputBtn.readBtn(3)   #Read for Btns inputs
                #     for i in range(len(btnReadings)):   
                #         if btnReadings(i):                           #if any btn is pressed
                #             score = score + 10          #increment the score
                #             sound.pause()               #pause background music
                #             sound.pointsSound()         #play score collecting sound
                #             sound.unpause()             #continue the background music
                    
                # else:
                #     outputBtn.setBtnLow(3)      #otherwise LEDS are turned off
                
                
                ''' wining '''
                winBtn = 4
                outputBtn.setBtnHigh(winBtn)                                    # light the Win Button
                btnWinReadings = inputBtn.readBtn(winBtn)                       # take Win Button reading
                if(btnWinReadings):                                             # celebrating wining 
                    sound.pause() 
                    sound.winSound()
                    score += 40
                
                
                if (remainingTime > 17 and remainingTime <21 and f1 == True):
                    '''
                    During a period of 3 seconds each 10 secs 3 Buttons Leds will
                     turn on They are in sequence as well
                    operation:
                    1- Read if any of them is pressed
                        if any btn is pressed
                        1- increase the score by 10 points
                        2- pause the background music
                        3- play collectin points sound

                    The time that not in this period the LEDS will be off
                    '''
                    
                    ''' Generate random numbers for buttons'''
                    if(f1_randomBtns):
                        randomBtns = np.random.randint(4, size=4)
                        randomBtns = list(dict.fromkeys(randomBtns))
                        f1_randomBtns = False
                        
                    outputBtn.setBtnHigh(randomBtns)             #Turn on Btns LEDS
                    btnReadings = inputBtn.readBtn(randomBtns)   #Read for Btns inputs
                    for i in range(len(btnReadings)-1):   
                        if btnReadings[i]:                           #if any btn is pressed
                            f1 = False
                            score = score + 10          #increment the score
                            sound.pause()               #pause background music
                            sound.pointsSound()         #play score collecting sound
                            sound.unpause()             #continue the background music
                        
                elif (remainingTime > 27 and remainingTime <31 and f2 == True):
                    if(f2_randomBtns):
                        randomBtns = np.random.randint(4, size=4)
                        randomBtns = list(dict.fromkeys(randomBtns))
                        f1_randomBtns = False
                    outputBtn.setBtnHigh(randomBtns)             #Turn on Btns LEDS
                    btnReadings = inputBtn.readBtn(randomBtns)   #Read for Btns inputs
                    for i in range(len(btnReadings)-1):   
                        if btnReadings[i]:                           #if any btn is pressed
                            f1 = False
                            score = score + 10          #increment the score
                            sound.pause()               #pause background music
                            sound.pointsSound()         #play score collecting sound
                            sound.unpause()             #continue the background music
                            
                elif (remainingTime > 37 and remainingTime <41 and f3 == True):
                    if(f3_randomBtns):
                        randomBtns = np.random.randint(4, size=4)
                        randomBtns = list(dict.fromkeys(randomBtns))
                        f1_randomBtns = False
                    outputBtn.setBtnHigh(randomBtns)             #Turn on Btns LEDS
                    btnReadings = inputBtn.readBtn(randomBtns)   #Read for Btns inputs
                    for i in range(len(btnReadings)-1):   
                        if btnReadings[i]:                           #if any btn is pressed
                            f1 = False
                            score = score + 10          #increment the score
                            sound.pause()               #pause background music
                            sound.pointsSound()         #play score collecting sound
                            sound.unpause()             #continue the background music
                else:
                    outputBtn.setBtnLow(4)      #otherwise LEDS are turned off    
                    
                    
            else:
                laser.turnOff(5)
                break
            
        



