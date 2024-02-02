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
	radius = agent.getMaxRadius() * 2

	for node in pathnodes:
		for node2 in pathnodes:
			if node != node2 and rayTraceWorld(node, node2, obstacleLines) == None:
				# For each non-colliding path, we will draw perpendicular lines of length 2*agentRadius at every single point on the path
				# If these perpendicular "width-check" lines collide with an obstacle, we know that path is too close to an obstacle so it will not be returned
				adequateWidth = True
				width_check_lines = []
				dx = node2[0] - node[0]
				dy = node2[1] - node[1]
				length = distance(node2, node)
				for i in range(0, int(length) + 1): 
					t = i / int(length)
					# Calculate the next point on the segment
					nextPoint = (node[0] + t * dx, node[1] + t * dy)
					# Calculate a perpendicular vector of length radius
					# Normalize the perpendicular vector
					perp_dx, perp_dy = dy, -dx
					norm = ((perp_dx**2) + (perp_dy**2))**0.5
					perp_dx, perp_dy = perp_dx / norm, perp_dy / norm
					# Calculate endpoints of the perpendicular line of length radius
					perp_line_start = (nextPoint[0] + perp_dx * radius / 2, nextPoint[1] + perp_dy * radius / 2)
					perp_line_end = (nextPoint[0] - perp_dx * radius / 2, nextPoint[1] - perp_dy * radius / 2)
					# Append the perpendicular line to the width lines list
					width_check_lines.append((perp_line_start, perp_line_end))
					# Uncomment below to see the width lines
					#lines.append((perp_line_start, perp_line_end))
				for width_line in width_check_lines:
					if rayTraceWorld(width_line[0], width_line[1], obstacleLines) != None:
						adequateWidth = False
				if adequateWidth:
					lines.append((node, node2))
	### YOUR CODE GOES ABOVE HERE ###
	return lines
