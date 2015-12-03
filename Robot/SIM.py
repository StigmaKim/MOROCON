'''
Created on 2015. 11. 11.

@author: Kim
'''
from random import random

class SIM(object):
    def __init__(self):
        '''
        Constructor
        '''
        
    HazardPossi = 0.1 # Hazard Blob spot possibility
    ColorPossi = 0.2 # Color Blob spot possibility
    
    # For getHazardInfo
    def checkHazard(self):
        if random() < self.HazardPossi :
            return True
        else :
            return False
        
    # For getColorInfo
    def checkForward(self):
        if random() < self.ColorPossi :
            return True
        else :
            return False
        
    def checkRight(self):
        if random() < self.ColorPossi :
            return True
        else :
            return False
    
    def checkLeft(self):
        if random() < self.ColorPossi :
            return True
        else :
            return False        
        
    ##############################
    def getHazardInfo(self):
        if self.checkHazard() :
            return 1
        else :
            return 0 
    
    #############################
    def getColorInfo(self):
        arr = [] # [ a, b ,c ]    a - forward, b - right, c - left // 1 - hazard exist, 0 - No hazard
        
        if self.checkForward() :
            arr.append(1)
        
        else :
            arr.append(0)
            
        if self.checkRight() :
            arr.append(1)
        
        else :
            arr.append(0)
            
        if self.checkLeft() :
            arr.append(1)
        
        else :
            arr.append(0)
        
        return arr
    
    def getPositionInfo(self):
        return 1