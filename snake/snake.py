# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 00:12:38 2020

@author: Vegard Stenberg
"""

import pygame
from pygame.locals import *
import time
import random
import numpy as np

def main():
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    
    pygame.init()
    pygame.display.set_caption("Snake by Vegard Stenberg")
    screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    
    speed = 20
    
    X_pos = 0
    Y_pos = 0
    X_speed = 0
    Y_speed = 0
    
    X_pos_food = random.choice(np.arange(0, 500, 20))
    Y_pos_food = random.choice(np.arange(0, 500, 20))
    
    bods = 1
    X_pos_bod = [0]
    Y_pos_bod = [0]
    
    head_color = (0, 200, 100)
    body_color = (0, 100, 200)
    food_color = (255, 0, 0)
    background_color = (255, 255, 255)
    
    font = pygame.font.SysFont('Comic Sans MS', 32)
    text = font.render(str(bods-1), False, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200)
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_UP:
                    X_speed = 0
                    Y_speed = -speed
                elif event.key == K_DOWN:
                    X_speed = 0
                    Y_speed = speed
                elif event.key == K_RIGHT:
                    X_speed = speed
                    Y_speed = 0
                elif event.key == K_LEFT:
                    X_speed = -speed
                    Y_speed = 0   
    
        screen.blit(text, textRect)
        pygame.display.update()
        
        screen.fill(background_color)
        
        #draw the player
        X_pos += X_speed
        Y_pos += Y_speed
        
        X_pos_bod.insert(0, X_pos)
        Y_pos_bod.insert(0, Y_pos)
        
        pygame.draw.rect(screen, head_color, (X_pos, Y_pos, 20, 20))  
        
        if X_pos >= SCREEN_WIDTH or X_pos < 0 or Y_pos >= SCREEN_HEIGHT or Y_pos < 0:
            running = False
        
        #check if the player thouches the food
        if X_pos == X_pos_food and Y_pos == Y_pos_food:
            X_pos_food = random.choice(np.arange(0, 500, 20))
            Y_pos_food = random.choice(np.arange(0, 500, 20))
        
            if X_speed < 0:
                X_pos_bod.append(X_pos_bod[bods-2]+20)
                Y_pos_bod.append(Y_pos_bod[bods-2])
                bods += 1
            elif X_speed > 0:
                X_pos_bod.append(X_pos_bod[bods-2]-20)
                Y_pos_bod.append(Y_pos_bod[bods-2])
                bods += 1
            elif Y_speed > 0:
                X_pos_bod.append(X_pos_bod[bods-2])
                Y_pos_bod.append(Y_pos_bod[bods-2]-20)
                bods += 1
            elif Y_speed < 0:
                X_pos_bod.append(X_pos_bod[bods-2])
                Y_pos_bod.append(Y_pos_bod[bods-2]+20)
                bods += 1
        
            text = font.render(str(bods-1), False, (0, 0, 0))
            screen.blit(text, textRect)
        
        for i in range(bods):
            if i != 0:
                pygame.draw.rect(screen, body_color, (X_pos_bod[i], Y_pos_bod[i], 20, 20))
        
                if X_pos == X_pos_bod[i] and Y_pos == Y_pos_bod[i]:
                    running = False
                
    
        pygame.draw.rect(screen, food_color, (X_pos_food, Y_pos_food, 20, 20)) 
         
        time.sleep(.1)

    print("Your score is:", bods-1)
    
if __name__ == "__main__":
    main()