'''
Created on 2015. 11. 11.

@author: ahn
'''
from Robocon.Dao import MissionDao, MapDao, RobotDao
from Robocon.interface import interface
from Robocon.ADDON import pathGenerator


class MissionManager(object):
    def __init__(self):
        self.missionDaoIns = MissionDao()
        self.mapDaoIns = MapDao()
        self.robotDaoIns = RobotDao()
        
    
    def getCurrentMissionList(self):
        return self.missionDaoIns.getAll()
    def getMission(self, key):
        return self.missionDaoIns.get(key)
    def getMap(self, mission):
        return self.mapDaoIns.get(mission.map_key)
    def getRobot(self, mission):
        return self.robotDaoIns.get(mission.robot_key)
    def start_Explore(self, path):
        interface.explore(interface(), path, self)
    def makeNewPath(self, hazard, curPos): # curPos - Start Point 
        print 'Find New Path'
        pathGenerator(hazard, self, curPos)
    
def main():
    mIns = MissionManager()
    pathGenerator(0, mIns, 0)
    
if __name__ == '__main__':
    main()
    
    
    
    
    
        