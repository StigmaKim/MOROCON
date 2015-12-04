'''
Created on 2015. 11. 11.

@author: ahn
'''
from Morocon.Dao import RobotDao

class RobotManager(object):
    def _init_(self):
        print 'aa'
    def addRobot(self, robot):
        RobotDao.add(RobotDao(),robot)
    def getRobotList(self):
        return RobotDao.getAll(RobotDao())
    def getInstance(self):
        return RobotManager()