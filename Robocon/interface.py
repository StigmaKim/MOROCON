'''
Created on 2015. 11. 26.

@author: Kim
'''
from SIM import SIM

simulator = SIM()
        
class interface(object):
    def __init__(self):
        '''
        Constructor
        '''
        self.direction = 0 # Initial Direction - North
        self.position = 0
        self.path = []
    
    # Attribute
    direction = None # Direction 0 = North, 1 = east, 2 = south, 3 = west
    position = None # Path array index
    path = None
    
    # Method
    def curDirection(self): # for Call by Reference
        return self.direction
    
    def curPosition(self): # for Call by Reference
        return self.position
    
    def setDirection(self, di):
        self.direction = di
        
    def setPosition(self, po):
        self.position = po
        
    def getCurrentPos(self):
        # simulator.getPositionInfo() # We don't have abnormal move.
        return self.path[self.curPosition()]
        
    def turn(self):
        #print 'turn!'
        pass
    
    def move(self):
        print 'move forward!, curPosition :',
        print self.path[self.curPosition()+1]
        self.setPosition(self.curPosition()+1)
        
    def explore(self, pathArr, missionMIns): # Explore Logic Included
        self.path = pathArr; # path array
        
        while self.curPosition() != len(self.path)-1:
            # Set Direction
            self.isRightDirection(self.path[self.curPosition()], self.path[self.curPosition()+1], self.curDirection())
            
            # Check Hazard
            Hazard = simulator.getHazardInfo()
            if Hazard : ## Go to Server & Save Hazard Info & Generate New Path
                        ## path[self.curPosition()+1]  <-- Spotted Hazard info      type [a, b]
                print 'Hazard blob is spotted :', 
                print self.path[self.curPosition()+1]
                missionMIns.makeNewPath(self.path[self.curPosition()+1], self.path[self.curPosition()])
                return 
            
            # Check Color
            arrColor = simulator.getColorInfo()
            di = self.curDirection() # Current Direction
            arrColorPos = []
            
            ## Convert relative position info to static position info
            if di == 0 :
                if arrColor[0] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0], pos[1]+1])
                        
                if arrColor[1] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0]+1, pos[1]])
                    
                if arrColor[2] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0]-1, pos[1]])
            
            if di == 1 :
                if arrColor[0] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0]+1, pos[1]])
            
                if arrColor[1] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0], pos[1]-1])
                    
                if arrColor[2] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0], pos[1]+1])
            
            if di == 2 :
                if arrColor[0] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0], pos[1]-1])
            
                if arrColor[1] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0]-1, pos[1]])
                    
                if arrColor[2] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0]+1, pos[1]])
                    
            if di == 3 :
                if arrColor[0] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0]-1, pos[1]])
            
                if arrColor[1] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0], pos[1]+1])
                    
                if arrColor[2] == 1 :
                    pos = self.path[self.curPosition()]
                    arrColorPos.append([pos[0], pos[1]-1])
                
            if arrColorPos != [] :  ## Go to Server & Save color blob info
                                    ## arrColorPos Array has Color blob info      type [[a, b], [c, d]]     Minimum 0 point, Maximum 3 point 
                print 'Color Blob is Spotted',
                print arrColorPos
            
            # Move
            self.move()
            
            # EndofPath
            if self.curPosition() == len(self.path)-1:
                print 'EndOfPath'
            
            
    
    # check direction & turn to right direction
    def isRightDirection(self, cur, next, di):
        cur_x = cur[0]
        cur_y = cur[1]
        next_x = next[0]
        next_y = next[1]
        
        if next_x == cur_x+1 : # make direction 1
            while 1-di != 0 :
                self.turn()
                di = (di + 1) % 4 
                self.setDirection(di)
         
        if next_y == cur_y+1 :
            while 0-di != 0 :
                self.turn()
                di = (di + 1) % 4
                self.setDirection(di)
                
        if next_x + 1 == cur_x:
            while 3-di != 0:
                self.turn()
                di = (di + 1) % 4
                self.setDirection(di)
        
        if next_y + 1 == cur_y:
            while 2-di != 0:
                self.turn()
                di = (di+1) % 4
                self.setDirection(di)
                        
                        
#if __name__ == '__main__':
    #path = [[1,1], [2,1], [2,2], [2,3], [3,3], [4,3], [5,3], [5,4], [5,5], [5,6], [5,7]]
    #interface = interface() # Make Instance
    #interface.explore(path) # Explore Start
    
    