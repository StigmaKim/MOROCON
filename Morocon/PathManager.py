'''
Created on 2015. 11. 29.

@author: HANJU
'''
from Morocon.MapManager import MapManager

class PathManager(object):
	def __init__(self):
		self.HazardArr = []
		self.NewHazardArr = []
		self.ColorArr = []
		self.FullPath = []
	
	def getColorArr(self):
		return self.ColorArr
	def getNewHazardArr(self):
		return self.NewHazardArr
	
	def setMapInfo(self, mapInfo, maxSearchDistance):
		self.map = mapInfo
		self.maxSearchDistance = maxSearchDistance
		self.heuristic = Heuristic()
		self.nodes = [[self.Node(x,y) for y in range(mapInfo.width)] for x in range(mapInfo.height)]
		self.test = [[[x,y] for y in range(mapInfo.width)] for x in range(mapInfo.height)]
		
	def findPath(self, sx, sy, tx, ty):	
		self.nodes[sx][sy].cost = 0
		self.nodes[sx][sy].depth = 0
		self.closedList = list()
		self.openList = list()
		self.openList.append(self.nodes[sx][sy])
		self.nodes[tx][ty].parent = None
		
		maxDepth = 0
		while (maxDepth < self.maxSearchDistance) and (len(self.openList) != 0):
			
			##print Open List
			#for i in range(len(self.openList)):
			#	print [self.openList[i].x, self.openList[i].y], 
			#print	
			
			current = self.openList[0]
			if current == self.nodes[tx][ty]:
				break
			self.openList.remove(current)
			self.closedList.append(current)
			
			for x in range(-1, 2):
				for y in range(-1, 2):
					
					if ((x==0) and (y==0)) or ((x!=0) and (y!=0)):
						continue
					else:
						xp = x + current.x
						yp = y + current.y
						
						if self.isValidLocation(sx, sy, xp, yp):
							nextStepCost = current.cost + self.map.getCost()
							neighbour = self.nodes[xp][yp]
							self.map.pathFinderVisited(xp, yp)
							
							if nextStepCost < neighbour.cost:
								if neighbour in self.openList:
									self.openList.remove(neighbour)
								if neighbour in self.closedList:
									self.closedList.remove(neighbour)
									
							if (neighbour not in self.openList) and (neighbour not in self.closedList):
								neighbour.cost = nextStepCost
								neighbour.heuristic = self.heuristic.getHeuristicCost(xp, yp, tx, ty)
								neighbour.depth = current.depth + 1
								neighbour.parent = current
								maxDepth = max(maxDepth, neighbour.depth)
								self.openList.append(neighbour)
							
		if self.nodes[tx][ty].parent is None:
			return 20		
		
		path = list()
		target = self.nodes[tx][ty]
		while target != self.nodes[sx][sy]:
			path.append([target.x, target.y])
			target = target.parent
		path.append([sx, sy])
		path.reverse()
		
		return path
			
		
	def isValidLocation(self, sx, sy, x, y):
		invalid = (x < 0) or (y < 0) or (x >= self.map.getHeight()) or ( y >= self.map.getWidth())
		if (not invalid) and ((sx != x) or (sy != y)):
			invalid = self.map.isBlocked(x, y)
		valid = not invalid
		return valid
	
	def addColorBlob(self, colorArr):
		for i in colorArr:
			self.ColorArr.append(i)
			
		print 'accumulated colorblob info : ',
		print self.ColorArr
	
	def setPreviousPath(self, path):
		if len(self.FullPath) == 0:
			for i in path:
				self.FullPath.append(i)
		else:
			self.FullPath.pop()
			for i in path:
				self.FullPath.append(i)
				
		#self.FullPath.append(path)
		
	def pathGenerator(self, newHazard, missionMIns, curPos, targetPos, PathManagerIns, HazardArr):
		if len(self.HazardArr) == 0:
			self.HazardArr = HazardArr
			# set from DB
			
		# new Hazard append -> get new Hazard Array
		if newHazard == 0:
			pass
		else:
			try:
				self.HazardArr.remove(newHazard)
				print 'Hazard Deleted'
			except ValueError as e:
				pass
			
			self.HazardArr.append(newHazard)
			self.NewHazardArr.append(newHazard)
			print 'hazard appended',
			print newHazard
		self.HazardArr.sort()
		self.NewHazardArr.sort()
		
		print 'Hazard Array : ',
		print self.HazardArr
		
		# Set MapInfo
		MAP = MapManager.getMapInfo(MapManager())
		MAP.width = 15
		MAP.height = 17
		MAP.hazard = self.HazardArr
		self.setMapInfo(MAP, 500)
		
		# set map, explore info
		if curPos == 0:
			START = [0, 0]
		else:
			START = curPos
			
		TARGET = targetPos
		
		sx = START[0]
		sy = START[1]
		tx = TARGET[0]
		ty = TARGET[1]
		
		PATH = PathManagerIns.findPath(sx, sy, tx, ty)	
		
		if PATH == 20:
			# Target Hazard Popup
			print 'No Path existed'
			print 'FullPath : ',
			print self.FullPath
			return
			
		print 'Path : ',
		print PATH
		str = missionMIns.start_Explore(PATH, targetPos, PathManagerIns)
		if (PATH[len(PATH)-1] in self.HazardArr) and str == 'printPath' :
			self.setPreviousPath(PATH[0:len(PATH)-2])
			# Target is Hazard Popup
			print 'Target is Hazard'
			print 'FullPath : ',
			print self.FullPath
			return
		elif str == 'printPath' :
			print 'FullPath : ',
			print self.FullPath
			return
		
		
	class Node():
		def __init__(self, x, y):
			self.x = x
			self.y = y
			self.cost = 0
			self.heuristic = 0
			self.depth = 0
			self.parent = None
			
class Map(object):
	def __init__(self, width, height, hazardList):
		self.width = width
		self.height = height
		self.hazard = hazardList
		self.visited = list()
		
	def getWidth(self):
		return self.width
	
	def getHeight(self):
		return self.height
	
	def pathFinderVisited(self, x, y):
		self.visited.append([x, y])
		self.visited.sort()
	
	def isBlocked(self, x, y):
		if [x, y] in self.hazard:
			return 1
	
	def getCost(self):
		return 1
	
class Heuristic():
	def getHeuristicCost(self, x, y, tx, ty):
		result = abs((tx - x)+(ty - y))
		return result
	


			
