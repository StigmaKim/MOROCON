'''
Created on 2015. 11. 11.

@author: ahn
'''
from Robocon.Dao import MissionDao, MapDao

class MissionManager():
    def __init__(self):
        self.missionDaoIns = MissionDao()
        self.mapDaoIns = MapDao()
    
    def getCurrentMissionList(self):
        return self.missionDaoIns.getAll()
    def getMission(self, key):
        return self.missionDaoIns.get(key)
    def getMap(self, mission):
        return self.mapDaoIns.get(mission.map_key)
        