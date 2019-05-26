# from LaserFrenzyOperation import *
import time
import pygame

class Sound:
    def __init__(self):
        self.sounds=["winSound.wav","errorSound.wav","gameSound.wav","loseSound.wav","success.wav"]
        pygame.mixer.init()
        
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
        
      
sound = Sound()
sound.gameSound()
time.sleep(3)
sound.pause()
sound.buzzer()
time.sleep(1)
sound.buzzer()
time.sleep(3)

sound.unpause()
time.sleep(3)
