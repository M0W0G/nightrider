import pygame
import random
import math

class Entity:
    def __init__(self, img, X = 0, Y = 0, X_Change = 0, Y_Change = 0):
        self.Img = pygame.image.load(img)
        self.X = X
        self.Y = Y
        self.X_Change = X_Change
        self.Y_Change = Y_Change
        
        
    def isCollision(self, ent_1, ent_2):
        pass
        #distance = math.sqrt((math.pow(ent_1.X - ent_2.X, 2)) + (math.pow(ent_1.Y - ent_2.Y , 2 )))
        #if distance < 27
        #   return True
        #return False
    
    #insures the entity cant leave the bounds of the given window
    #get size accounts for width of image with bounds collision 
    def inBounds(self, height, width):
        if self.X <= 0:
            self.X = 0
        elif self.X >= width - self.Img.get_size()[0]:
            self.X = width - self.Img.get_size()[0]
        if self.Y <= 0:
            self.Y = 0
        elif self.Y >= height - self.Img.get_size()[1]:
            self.Y = height - self.Img.get_size()[1]
    
    #updates the entity position etc
    def update(self):
        self.X += self.X_Change
        self.Y += self.Y_Change
    

#IDK why i inherited, I had a future plan but have forgotten.

class Player(Entity):
    def __init__(self, img, X = 0, Y = 0, X_Change = 0, Y_Change = 0):
        super().__init__(img, X = 0, Y = 0, X_Change = 0, Y_Change = 0)
        
        
class Enemy(Entity):
    def __init__(self, img, X = 0, Y = 0, X_Change = 0, Y_Change = 0):
        super().__init__(img, X = 0, Y = 0, X_Change = 0, Y_Change = 0)
 
 #oil spills hurt the player, they subtract a point
 
class Oil(Entity):
    def __init__(self, img, X = 0, Y = 0, X_Change = 0, Y_Change = 0):
        super().__init__(img, X = 0, Y = 0, X_Change = 0, Y_Change = 0)
        self.Y_Change = 1.5
