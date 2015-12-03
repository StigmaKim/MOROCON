'''
Created on 2015. 11. 11.

@author: ahn
'''
from Robocon.Dao import MissionDao, MapDao, RobotDao
from Robot.interface import interface
from PathManager import PathManager

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
    def start_Explore(self, path, targetPos, PathManagerIns):
        if interface.explore(interface(), path, self, targetPos, PathManagerIns) == 'printPath' :
            return 'printPath'
    def makeNewPath(self, hazard, curPos, targetPos, PathManagerIns): # curPos - Start Point 
        print 'Find New Path'
        PathManagerIns.pathGenerator(hazard, self, curPos, targetPos, PathManagerIns)
    def AddColorBolb(self, colorArr, PathManagerIns):
        PathManagerIns.addColorBlob(colorArr)
    def setPreviousPath(self, path, PathManagerIns):
        PathManagerIns.setPreviousPath(path)
        
def main():
    mIns = MissionManager()
    PathManagerIns = PathManager()
    targetPos = [7, 5] # set target position
    startPos = [0, 0] # set start position
    PathManagerIns.pathGenerator(0, mIns, startPos, targetPos, PathManagerIns)
    
if __name__ == '__main__':
    main()
    
    
    
    
    
        