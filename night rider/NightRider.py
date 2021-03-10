import pygame
import random
import math
import entity



#start the game
pygame.init()


height = 600
width = 800
screen = pygame.display.set_mode((width, height))

#Title and Icon setup
pygame.display.set_caption("Night Rider")
#icon = pygame.image.load('car.png')
#pygame.display.set_icon(icon)

def draw(entity):
        screen.blit(entity.Img, (entity.X, entity.Y))

#TODO: Dont hard code these numbers, use the height and width to create something
player = entity.Player('car.png', 600, 480, 100 , 0)
#spawns the oil slightly above screen so you cant see it until it comes
oil = entity.Oil('car.png', random.randint(0, width), 800)


# Game Loop

running = True
while running:
    #allows you to escape
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #keystroke register
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("pressing left arrow")
                player.X_Change = -1.5
            if event.key == pygame.K_RIGHT:
                print("pressing right arrow")
                player.X_Change = 1.5
            if event.key == pygame.K_UP:
                print("pressing up arrow")
                player.Y_Change = -1.5
            if event.key == pygame.K_DOWN:
                print("pressing down arrow")
                player.Y_Change = 1.5
                
        
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
        
    
    #draws background
    screen.fill((30,12,56))
    draw(player)
    draw(oil)
    player.inBounds(height, width)
    player.update()
    oil.update()
    pygame.display.update()
    
