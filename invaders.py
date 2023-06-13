from turtle import pos
import pygame 
from pygame.locals import * 
import os 
import random 


INVADER_WIDTH, INVADER_HEIGHT = 40,40 ## constants for invader width and height 
INVADER_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets',"invader.png")),(INVADER_WIDTH,INVADER_HEIGHT)) ## stores image path 


class Invader():

    def __init__(self,xpos,ypos): ## takes in an x position and y position for invader placement on screen 
        self.invader_img = INVADER_IMG
        self.rect = pygame.Rect(xpos,ypos,INVADER_WIDTH,INVADER_HEIGHT)
        self.x = xpos
        self.y = ypos 
        self.bullet = None 
        
    
    def move(self,direction) : 
        self.direction = direction 
        self.x += direction 
        self.rect.x = self.x 
       
    def shoot(self) :
        self.bullet.y += 5
        self.bullet.rect.y = self.bullet.y 
    
    def reload(self) : 
        self.bullet = pygame.Rect(self.x,self.y+INVADER_HEIGHT//2,4,20)

    def death(self) :
        self.invader_img = None 
        self.rect = None 