'''
Created on 2015. 11. 29.

@author: HANJU
'''
from Robocon.MapManager import MapManager

class ADDON(object):

	def __init__(self, mapInfo, maxSearchDistance):
		self.map = mapInfo
		self.maxSearchDistance = maxSearchDistance
		self.heuristic = Heuristic()
		self.nodes = [[self.Node(x,y) for y in range(mapInfo.width)] for x in range(mapInfo.height)]
		self.test = [[[x,y] for y in range(mapInfo.width)] for x in range(mapInfo.height)]
		
	def findPath(self, sx, sy, tx, ty):	
		if self.map.isBlocked(tx, ty):
			print("Target Point is Blocked!")
			return None
		
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
			print("return none! check this")
			return None			
		
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
	
def pathGenerator(newHazard, missionMIns, curPos):
	WIDTH = 7
	HEIGHT = 8
	HAZARD = [[0,2],[1,0],[1,2],[2,0],[2,5],[3,1],[3,3],[4,5],[5,3],[5,5],[6,3],[7,4]]
	
	# new Hazard append -> get new Hazard Array
	if newHazard == 0:
		pass
	else:
		try:
			HAZARD.remove(newHazard)
			print 'Hazard Deleted'
		except ValueError as e:
			pass
		
		HAZARD.append(newHazard)
		print 'hazard appended',
		print newHazard
	HAZARD.sort()
	
	print 'Hazard Array : ',
	print HAZARD
	
	
	# set map, explore info
	if curPos == 0:
		START = [0, 0]
	else:
		START = curPos
		
	TARGET = [7, 5]
	
	sx = START[0]
	sy = START[1]
	tx = TARGET[0]
	ty = TARGET[1]
	
	MAP = MapManager.getMapInfo(MapManager())
	
	MAP.width = 15
	MAP.height = 17
	MAP.hazard = HAZARD
	
	ADDONIns = ADDON(MAP, 500)
	PATH = ADDONIns.findPath(sx, sy, tx, ty)
	print 'new Path gotten, go explore'
	print 'Path : ',
	print PATH
	missionMIns.start_Explore(PATH)



			
			