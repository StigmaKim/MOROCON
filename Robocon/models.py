from django.db import models
from google.appengine.ext import db
  
class Map(db.Model):
    name = db.StringProperty()
    map_x = db.IntegerProperty()
    map_y = db.IntegerProperty()
    map_danger1_x = db.IntegerProperty()
    map_danger1_y = db.IntegerProperty()
    map_danger2_x = db.IntegerProperty()
    map_danger2_y = db.IntegerProperty()
    map_danger3_x = db.IntegerProperty()
    map_danger3_y = db.IntegerProperty()
    map_danger4_x = db.IntegerProperty()
    map_danger4_y = db.IntegerProperty()
    map_danger5_x = db.IntegerProperty()
    map_danger5_y = db.IntegerProperty()
    map_danger6_x = db.IntegerProperty()
    map_danger6_y = db.IntegerProperty()
    map_danger7_x = db.IntegerProperty()
    map_danger7_y = db.IntegerProperty()
    map_danger8_x = db.IntegerProperty()
    map_danger8_y = db.IntegerProperty()
    map_danger9_x = db.IntegerProperty()
    map_danger9_y = db.IntegerProperty()
    map_danger10_x = db.IntegerProperty()
    map_danger10_y = db.IntegerProperty()
    newPos = []
    newPos.append([map_danger1_x, map_danger1_y])
    newPos.append([map_danger2_x, map_danger2_y])
    newPos.append([map_danger3_x, map_danger3_y])
    newPos.append([map_danger4_x, map_danger4_y])
    newPos.append([map_danger5_x, map_danger5_y])
    newPos.append([map_danger6_x, map_danger6_y])
    newPos.append([map_danger7_x, map_danger7_y])
    newPos.append([map_danger8_x, map_danger8_y])
    newPos.append([map_danger9_x, map_danger9_y])
    newPos.append([map_danger10_x, map_danger10_y])
    hazard = newPos
    visited = []
    
    image = db.BlobProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
    def getWidth(self):
        return self.map_x
    
    def getHeight(self):
        return self.map_y
    
    def pathFinderVisited(self, x, y):
        self.visited.append([x, y])
        self.visited.sort()
    
    def isBlocked(self, x, y):
        if [x, y] in self.hazard:
            return 1
    
    def getCost(self):
        return 1
    
class Robot(db.Model):
    name = db.StringProperty()
    serial = db.IntegerProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
class Mission(db.Model):
    name = db.StringProperty()
    map_key = db.StringProperty()
    robot_key = db.StringProperty()
    start_date =  db.DateTimeProperty(auto_now_add=True)
    end_date = db.DateTimeProperty()
    state = db.StringProperty()
    
    
    
    
    