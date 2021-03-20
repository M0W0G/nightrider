import math
import pygame


class Timer:
    def __init__(self, clock):
        
        self.clock = clock
        self.time = 0
        
    
    def Run(self):
        mS = clock.tick() # how many miliseconds have passed
    
        seconds = mS / 1000
    
        time += seconds
        
        return math.trunc(time)
        
    
    
    
    
    