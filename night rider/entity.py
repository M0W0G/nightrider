import pygame
import random
import math

height = 600
width = 800


class Entity:
    def __init__(self, img, X = 0, Y = 0, X_Change = 0, Y_Change = 0):
        self.Img = pygame.image.load(img)
        self.X = X
        self.Y = Y
        self.X_Change = X_Change
        self.Y_Change = Y_Change
        
        
    def isCollision(self, ent):
        
        distance = math.sqrt((math.pow(ent.X - self.X,2)) + (math.pow(ent.Y - self.Y,2)))
        if distance < 27:
            return True
        return False
 
    
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
        super().__init__(img, X, Y, X_Change = 0, Y_Change = 0)
        
        self.cooldown = 0
        
    #gives the player a 5 second cooldown to prevent something from happening    
    def giveCooldown(self):
        self.cooldown = 5
        
        
    def isCollision(self, ent):
        
        distance = math.sqrt((math.pow(ent.X - self.X,2)) + (math.pow(ent.Y - self.Y,2)))
        if distance < 27:
            return True
        return False
        
        
class Enemy(Entity):
    def __init__(self, img, X = 0, Y = 0, X_Change = 0, Y_Change = 0):
        super().__init__(img, X = 0, Y = 0, X_Change = 0, Y_Change = 0)
        
    def isCollision(self, ent):
        
        distance = math.sqrt((math.pow(ent.X - self.X,2)) + (math.pow(ent.Y - self.Y,2)))
        if distance < 27:
            return True
        return False
 
 #oil spills hurt the player, they subtract a point
 
class Oil(Entity):
    def __init__(self, img, X = 0, Y = 0, X_Change = 0, Y_Change = 0):
        super().__init__(img, X, Y, X_Change = 0, Y_Change = 10)
        self.Y_Change = 7

class finishLine(Entity):
    def __init__(self, img, X = 0, Y = 0, X_Change = 0, Y_Change = 0):
        super().__init__(img, X, Y, X_Change = 0, Y_Change = 7)
        
    def isCollision(self, ent):
        
        # X position + height of finishLine sprite
        if self.Y + 75 >= ent.Y:
            print('yes')
            return True
        print
        return False
        

#----------------------------------------------
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('road.png')
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = self.rectBGimg.height
            self.bgX2 = 0
 
            self.moving_speed = 5
         
      def update(self):
        self.bgY1 -= self.moving_speed
        self.bgY2 -= self.moving_speed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height
        if self.bgY2 <= -self.rectBGimg.height:
            self.bgY2 = self.rectBGimg.height
             
      def render(self):
         DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
         DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))