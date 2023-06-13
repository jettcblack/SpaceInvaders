import pygame 
from pygame.locals import * 
import os 

MINI_SHIP_IMG = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'ship.png')),(40,40)) ## find the spaceship png image in our assets folder, also transforms to better scale 
MINI_SHIP_IMG = MINI_SHIP_IMG.convert_alpha()
WHITE = (255,255,255) 
GAME_OVER = pygame.transform.scale(pygame.image.load(os.path.join('Assets','gameover.png')),(1000,800)) 
START_IMG = pygame.image.load(os.path.join('Assets','title.png')) 

class Score() :

    def __init__(self) :
        pygame.font.init() 
        self.score = 0
        self.level = 1 
        self.lives = 3 
        self.score_font = pygame.font.SysFont("scoreboard",30) 
        self.score_text = self.score_font.render(f"SCORE: {self.score}", False, (WHITE))
        self.level_text = self.score_font.render(f"LEVEL {self.level}", False, (WHITE)) 
        self.health_text = self.score_font.render(f"LIVES", False, (WHITE)) 
        self.mini_ship_imgs = [MINI_SHIP_IMG,MINI_SHIP_IMG,MINI_SHIP_IMG]  
       

    def kill(self) :
        self.score += 100 
        self.score_text = self.score_font.render(f"SCORE: {self.score}",False,(WHITE)) 

    def lose_life(self,window) : 
        self.lives -= 1
        self.mini_ship_imgs.remove(MINI_SHIP_IMG)

    def game_over(self,window) : 
        window.blit(GAME_OVER,(0,0))
        