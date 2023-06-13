import pygame 
from pygame.locals import * 
import os 

pygame.display.set_mode((1,1), pygame.NOFRAME)
SHIP_WIDTH, SHIP_HEIGHT = 80,80
SHIP_X, SHIP_Y = 475,650
SHIP_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ship.png')),(SHIP_WIDTH,SHIP_HEIGHT)) ## find the spaceship png image in our assets folder, also transforms to better scale 
SHIP_IMG = SHIP_IMG.convert_alpha()
SHIP_EXPLOSION = pygame.transform.scale(pygame.image.load(os.path.join('Assets','explode.png')),(SHIP_WIDTH,SHIP_HEIGHT)) ## finds the explosion png and scales for ship death 
SHIP_EXPLOSION = SHIP_EXPLOSION.convert_alpha()
VELOCITY = 3.5
MAX_BULLETS = 3

class Ship():

    def __init__(self): 
        self.img = SHIP_IMG ## hold ship image path
        self.rect = pygame.Rect(SHIP_X,SHIP_Y,SHIP_WIDTH,SHIP_HEIGHT) ## sprite that represents the image (ship) 
        self.x = SHIP_X ## x coordinate for sprite 
        self.y = SHIP_Y ## y coordinate for sprite 
        self.bullets = [] ## list for the chamber of bullets , will only store 3 at a time to avoid spamming of bullets 
  

    def move(self,key): ## function that will move the ship in given direction based on key input 
        ## if the key entered is right, move right as long as not too far to right of screen, and same concept with left 
        if (key[pygame.K_RIGHT]) :
            if self.x < 1000 - SHIP_WIDTH: 
                self.x += VELOCITY
                self.rect.x = self.x 
        elif (key[pygame.K_LEFT]) : 
            if self.x > 0 :
                self.x -= VELOCITY
                self.rect.x = self.x 
    
    def shoot(self): ## function that fires gun, removes bullet once it is off screen or hits enemy (not implemented yet) 
        for bullet in self.bullets :
            bullet.y -= 5 
            if bullet.y < 0 :
                self.bullets.remove(bullet) 

    def reload(self): ## function that creates bullet object and appends it to the chamber 
        if len(self.bullets) < 3 : 
            bullet = pygame.Rect(self.x + SHIP_WIDTH//2, self.y - SHIP_HEIGHT//2-2,4,20) 
            self.bullets.append(bullet)

   
    
    def kill_confirmed(self) :
        pass 
    
        
        

    def game_over(self) :
        print("game over") 
        
        
    
                
               

        