'''
Created on 2015. 11. 11.

@author: ahn
'''
from Robocon.Dao import MapDao

mapDaoIns = MapDao()
class MapManager():
    def addMap(self, map):
        mapDaoIns.add(map)
        
    def deleteMap(self, key):
        mapDaoIns.delete(key)

    def getMapList(self):
        return mapDaoIns.getAll()