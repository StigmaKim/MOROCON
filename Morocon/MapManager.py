'''
Created on 2015. 11. 11.

@author: ahn
'''
from Morocon.Dao import MapDao
from models import Map

mapDaoIns = MapDao()

class MapManager():
    def addMap(self, map):
        mapDaoIns.add(map)
        
    def deleteMap(self, key):
        mapDaoIns.delete(key)

    def getMapList(self):
        return mapDaoIns.getAll()
    
    def getMap(self, key):
        return mapDaoIns.get(key)
    
    def getMapInfo(self):
        return Map()
    
    