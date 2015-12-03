'''
Created on 2015. 11. 5.

@author: ahn
'''
from google.appengine.ext import db
from Morocon.models import Map, Robot, Mission

class MapDao(object):
    def add(self, map):
        map.put()
    def delete(self, key):
        db.delete(key)
    def getAll(self):
        return Map.all()
    def get(self, key):
        return db.get(key)
        
class MissionDao(object):
    def add(self, mission):
        mission.put()
    def getAll(self):
        return Mission.all()
    def get(self, key):
        return db.get(key)
        
class RobotDao(object):
    def add(self, robot):
        robot.put()
    def getAll(self):
        return Robot.all()
    def get(self, key):
        return db.get(key)
        
        
        