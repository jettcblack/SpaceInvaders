import pygame 
from ship import * 
from pygame.locals import * 
import os 
from invaders import *  
import random 
from score import * 

############ Constants for framing game, background, WINDOW, etc ##########################################
FPS = 60 ## Frame per second for the game 
WIDTH, HEIGHT = 1000,800 ## width and height constants for our window 
BG = pygame.transform.scale(pygame.image.load(os.path.join('Assets',"background.png")),(WIDTH,HEIGHT)) ## background constant for the background of the game 
############################################################################################################


####### Constants for Ships and Invaders (rects of the game) ###############################################
SHIP = Ship() ## creates ship object , which will store only one constant ship 
INVADERS = [] ## creates constant for list of invaders 
INVADER_BULLETS = []
SCORE = Score()  

for i in range(50,550,100) : ## appends invaders to list of invaders 
        for n in range(100,925,75) :
            invader = Invader(n,i) 
            INVADERS.append(invader) 

DIRECTION_CHANGE = -1 ## constant that will change the direction of the group of invaders once reached left bound or right bound 
RED = (255,0,0) ## constant for rgb value of red 
############################################################################################################



############################################### User Events ################################################
INVADER_FIRE = USEREVENT + 1
SPACESHIP_HIT = USEREVENT + 2 
INVADER_KILLED = USEREVENT + 3 
############################################################################################################



###################### Initializing the Game ###############################################################
pygame.init() ## initialize pygame 
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT)) ## window variable that sets up window for pygame 
BG = BG.convert() ## convert background after setting up WINDOW, helps with performance of game 
############################################################################################################



################ METHOD THAT DRAWS WINDOW EVERY ITERATION OF GAME , WILL BE CALLED IN MAIN LOOP ############
def draw_window(ship,bullets,invaders,invader_bullets) : ## draw window function that will be called to updated different things needed on screen each loop in main loop 

    WINDOW.fill((0,0,0)) ## fill window with black so we can blit on window 
    WINDOW.blit(BG,(0,0)) ## blit the background to the window 
    WINDOW.blit(SCORE.score_text,(20,10)) 
    WINDOW.blit(SCORE.level_text, (450,10)) 
    WINDOW.blit(SCORE.health_text, (750,10)) 

    i = 850

    for miniship in SCORE.mini_ship_imgs :
        WINDOW.blit(miniship, (i,10)) 
        i+=50 

    for bullet in bullets : ## for each bullet in bullet list, blit it onto screen continuously each loop 
        pygame.draw.rect(WINDOW,RED,bullet) 
    
    for invader_bullet in invader_bullets : 
        pygame.draw.rect(WINDOW,RED,invader_bullet) 

        
    for invader in INVADERS : ## for every invader in group of invaders, blit their respective positions on screen 
        WINDOW.blit(invader.invader_img,(invader.x,invader.y))
    
    

    WINDOW.blit(ship.img, (ship.x,ship.y)) ## blits ship onto screen 
    
        
    pygame.display.update() ## this will update screen each loop 

    if (SHIP.img == SHIP_EXPLOSION) : 
        pygame.time.wait(2000)

##############################################################################################################



############################ MAIN FUNCTION, WHERE GAME LOOP IS LOCATED #######################################

def main(): ## main function, where game loop will run 

     

    invader_direction = -1 ## direction variable that will control where enemy invaders go 

    clock = pygame.time.Clock() ## clock that ticks at FPS to run 

    pygame.time.set_timer(INVADER_FIRE,1000) ## Timer that will trigger event every decided seconds that way different invaders can shoot at different times 

    run = True ## variable that will be used to keep game running or to break loop 



    while run : ## main game loop 
    

        SHIP.img = SHIP_IMG 

        clock.tick(FPS) ## keeps game running at 60 frames per second 

        for event in pygame.event.get(): ## in pygame all events are kept within pygame.event.get()  
            
            if event.type == pygame.QUIT : ## detects player hitting red x on window 
                run = False 
            elif event.type == pygame.KEYDOWN : ## for shooting a bullet, this does not need to be continous, so pass in a keydown event command 
                if event.key == pygame.K_SPACE : ## if the key is equal to space, "reload" the gun which will create a bullet object within ship and append it to bullets list 
                    SHIP.reload() 
            if event.type == INVADER_FIRE :
                shooting_invader = random.choice(INVADERS)
                shooting_invader.reload() 
                INVADER_BULLETS.append(shooting_invader.bullet)

            if event.type == SPACESHIP_HIT :
                SCORE.lose_life(WINDOW) 
                SHIP.img = SHIP_EXPLOSION 
                if SCORE.lives == 0 :
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
    

            if event.type == INVADER_KILLED :
                SHIP.kill_confirmed() 
                SCORE.kill() 
               
                
            
        ''' Need to fix the rectangle / alien dispersion between the space invader and its' rect. Its causing my bullets to not hit on target '''
            
        for bullet in SHIP.bullets :
            for invader in INVADERS :
                if invader.rect.colliderect(bullet) :
                    pygame.event.post(pygame.event.Event(INVADER_KILLED))       
                    SHIP.bullets.remove(bullet) 
                    INVADERS.remove(invader) 


        for invader_bullet in INVADER_BULLETS : 
            invader_bullet.y += 10 
            if invader_bullet.y > 800 :
                INVADER_BULLETS.remove(invader_bullet) 
            if SHIP.rect.colliderect(invader_bullet) :
                pygame.event.post(pygame.event.Event(SPACESHIP_HIT))
                INVADER_BULLETS.remove(invader_bullet) 
              

        keys_pressed = pygame.key.get_pressed() ## keeps a list of keys pressed, good for continuous key press (like moving)
        
        '''
        where bug is occurring possibly, python could be handling the multiplication of invader direction wrongly, but it is only happening to the top row of invaders? 
        '''
        for invader in INVADERS : ## for every invader in invader, move the invader in specified direction 
            invader.move(invader_direction) 
            if invader.x <= 50 : ## if invaders move too far left, change direction 
                invader_direction *= DIRECTION_CHANGE 
                break 
            elif invader.x >= 950 : ## same with right 
                invader_direction *= DIRECTION_CHANGE 
                break 
        
        
       
            
        
        SHIP.shoot() ## shoots the ship if there are bullets in chamber (ship.bullets) 
        SHIP.move(keys_pressed) ## pass keys pressed into move, if its left or right ship will do as so 

        
        draw_window(SHIP,SHIP.bullets,INVADERS,INVADER_BULLETS) ## updates the window each while loop 
        

    SCORE.game_over(WINDOW) 
    pygame.display.update() 

    pygame.time.wait(5000) 

    pygame.quit() ## once while loop is broken from red x, code will go here to quit pygame 



if __name__ == "__main__":
    main() 