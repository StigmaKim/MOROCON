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
    image = db.BlobProperty()
    date = db.DateTimeProperty(auto_now_add=True)
    
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
    
    
    
    
    