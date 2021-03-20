import pygame
import random
import math
import entity
#import timer
#from pygame_functions import *
import time
from pygame import mixer



clock = pygame.time.Clock()
time_elapsed_Oil = 0
time_elapsed_Line = 0


#TODO: 3/15/2021
#Make background scroll
#Add second player
#Add music
#COMPLETED: Stop finish line and oils from spawning at the same time
    
    


#start the game
pygame.init()


height = 600
width = 800
screen = pygame.display.set_mode((width, height))

#Title and Icon setup
pygame.display.set_caption("Night Rider")
#icon = pygame.image.load('car.png')
#pygame.display.set_icon(icon)

#background
bg = pygame.image.load("road.png")
#scales iamge to fit screen
bg = pygame.transform.scale(bg,(width, height))

#Background sound
#mixer.music.load('mooncrystal.mp3')
#mixer.music.play(-1)


#game score
score_value = 0
score_value2 = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

textX2 = 10
textY2 = 50
def show_score(x,y, num):
    if num == 1:
        score = font.render(f"Score: {score_value}", True, (255,255,255))
    else:
        score = font.render(f"Score: {score_value2}", True, (255,255,255))
    screen.blit(score, (x, y))


#spawns the given entity at the given rate
#Time : Seconds, Rate: How many seconds you want to pass before it rolls a number, Chance: Likelihood that it spawns out of 100
def randomSpawnOil(time, rate, percent_chance):
    if time > rate:
        if random.randint(0, 100) <= percent_chance:
            oils.append(entity.Oil('oilspill.png', random.randint(0, width - 32), 0))
        return True
    return False
        
def randomSpawnLine(time, rate, percent_chance):
    if time > rate:
        if random.randint(0,100) <= 100:
            finish_lines.append(entity.finishLine('finishline.png', 0, 0))
        return True
    return False

def draw(entity):
        screen.blit(entity.Img, (entity.X, entity.Y))

oils = []
finish_lines = []
#TODO: Dont hard code these numbers, use the height and width to create something
player = entity.Player('car.png', width / 2, height / 2, 100 , 0)

player2 = entity.Player('car.png', width / 2, height / 2, 100, 0)
#Finish Line
finish_lines.append(entity.finishLine('finishline.png', 0, 0))


#spawns the oil slightly above screen so you cant see it until it comes
#oils.append(entity.Oil('car.png', random.randint(0, 600), 800))
oils.append(entity.Oil('oilspill.png', random.randint(0, width - 32), 0))



# Game Loop

running = True
while running:
    #game timer
    #.scroll(10, 0)
    mS = clock.tick() # how many miliseconds have passed
    
    time_elapsed_Oil += mS
    time_elapsed_Line += mS
    #print(time_elapsed)
    
    #every 5000 miliseconds (5 seconds), spawn an oil slick 100% of the time
    if randomSpawnOil(time_elapsed_Oil, 150, 100):
        time_elapsed_Oil = 0
        
    if randomSpawnLine(time_elapsed_Line, 2000, 100):
        time_elapsed_Line = 0
    
    #allows you to escape
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
        #speed variable
        speed = 9
        #keystroke register for player 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("pressing left arrow")
                player.X_Change = -speed
            if event.key == pygame.K_RIGHT:
                print("pressing right arrow")
                player.X_Change = speed
            if event.key == pygame.K_UP:
                print("pressing up arrow")
                player.Y_Change = -speed
            if event.key == pygame.K_DOWN:
                print("pressing down arrow")
                player.Y_Change = speed
                
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("left key release")
                player.X_Change = 0
            if event.key == pygame.K_RIGHT:
                print("right key release")
                player.X_Change = 0
            if event.key == pygame.K_UP:
                print("up key release")
                player.Y_Change = 0
            if event.key == pygame.K_DOWN:
                print("down key release")
                player.Y_Change = 0
                
                
        #keystroke register for player 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("pressing left arrow")
                player2.X_Change = -speed
            if event.key == pygame.K_d:
                print("pressing right arrow")
                player2.X_Change = speed
            if event.key == pygame.K_w:
                print("pressing up arrow")
                player2.Y_Change = -speed
            if event.key == pygame.K_s:
                print("pressing down arrow")
                player2.Y_Change = speed
                
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("left key release")
                player2.X_Change = 0
            if event.key == pygame.K_d:
                print("right key release")
                player2.X_Change = 0
            if event.key == pygame.K_w:
                print("up key release")
                player2.Y_Change = 0
            if event.key == pygame.K_d:
                print("down key release")
                player2.Y_Change = 0
    #oil collision detection
    for o in oils:
        if o.isCollision(player):
            print("hit")
            oils.remove(o)
            score_value -= 1
    
    #TODO: figure out way to detect finish line all the way accross, override isCollision method? have the detection just be one straight line going down?
    #finish line detection
    for l in finish_lines:
        if l.isCollision(player):
            print("crossed line")
            finish_lines.remove(l)
            score_value += 1
    
    #player 2 detection
    for o in oils:
        if o.isCollision(player2):
            print("hit")
            oils.remove(o)
            score_value2 -= 1
    
    for l in finish_lines:
        if l.isCollision(player2):
            print("crossed line")
            finish_lines.remove(l)
            score_value2 += 1
    #draws background
    screen.fill((30,12,56))
    screen.blit(bg, (0,0))
 
    draw(player)
    draw(player2)
    
    for l in finish_lines:
        draw(l)
        
    
    
    
    for o in oils:
        draw(o)
    
    player.inBounds(height, width)
    player.update()
    player2.inBounds(height, width)
    player2.update()
    for o in oils:
        o.update()
    for l in finish_lines:
        l.update()
    
    show_score(textX, textY, 1)
    show_score(textX2, textY2, 2)
    
    pygame.display.update()
    
