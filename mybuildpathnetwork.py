'''
 * Copyright (c) 2014, 2015 Entertainment Intelligence Lab, Georgia Institute of Technology.
 * Originally developed by Mark Riedl.
 * Last edited by Mark Riedl 05/2015
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import sys, pygame, math, numpy, random, time, copy, operator
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates the path network as a list of lines between all path nodes that are traversable by the agent.
def myBuildPathNetwork(pathnodes, world, agent = None):
	lines = []
	### YOUR CODE GOES BELOW HERE ###
	obstacleLines = world.getLines()
	obstaclePoints = world.getPoints()
	radius = agent.getMaxRadius()

	for node in pathnodes:
		for node2 in pathnodes:
			if node != node2 and rayTraceWorld(node, node2, obstacleLines) == None:
				# we will check at every point in the path if a perpendicular ray from that point intersects an obstacle
				pathPoints = []
				dx = node[0] - node2[0]
				dy = node[1] - node2[1]
				add = True
				dist = distance(node, node2)
				steps = 10
				for i in range(steps):
					t = i / steps  
					x = node[0] + (dx * t)
					y = node[1] + (dy * t)
					pathPoints.append((x, y))
				for p in pathPoints:
					radiusPoint1 = (p[0] + ((node2[0]-node[0])*radius/dist), p[1] + ((node[1]-node2[1])*radius/dist))
					lines.append((p, radiusPoint1))
				lines.append((node, node2))
	### YOUR CODE GOES ABOVE HERE ###
	return lines
