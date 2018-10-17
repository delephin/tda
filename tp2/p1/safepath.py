#!/usr/bin/env python

import sys
import time
import random
import os
from collections import deque

def whichSideOfLine (lineEndptA, lineEndptB, ptSubject):
    return (ptSubject[0] - lineEndptA[0]) * (lineEndptB[1] - lineEndptA[1]) - (ptSubject[1] - lineEndptA[1]) * (lineEndptB[0] - lineEndptA[0])

def fuerzabruta(root, end, safe_points):
	print("fuerzabruta [%s] [%s] [%s]" % (root, end, safe_points))
	
	minimum_convex_hull = []
	
	for i in range(0, len(safe_points)):
		for j in range(0, len(safe_points)):
			if i == j:
				continue
			
			pointI = safe_points[i]
			pointJ = safe_points[j]
			
			allPointsOnTheRight = True
			
			for k in range(0, len(safe_points)):
				if k == i or k == j:
					continue
				
				d = whichSideOfLine(pointI, pointJ, safe_points[k])
				if d < 0:
					allPointsOnTheRight = False
					break
			
			if allPointsOnTheRight:
				if pointI not in minimum_convex_hull:
					minimum_convex_hull.append(pointI)
					
				if pointJ not in minimum_convex_hull:
					minimum_convex_hull.append(pointJ)
			
	
	return minimum_convex_hull
	
def graham():
	print("graham")

def division():
	print("division")

if len(sys.argv) != 3 :
	print("Invalid input.\nUsage: \n\t safepath inputFilepath F|G|D")
	sys.exit(1)
	
filename = sys.argv[1]
mode=sys.argv[2]

#
#
path1 = []
path2 = []
root = ()
end = ()
safe_points = []

input = open(filename, "r")

for line in input:
	line = line.rstrip('\n')
	coordenates = line.split(" ")
	safe_points.append((int(coordenates[0]), int(coordenates[1])))

#root = safe_points.pop(0)
#end = safe_points.pop(0)
root = safe_points[0]
end = safe_points[1]

if mode == 'F':
	path1 = fuerzabruta(root, end, safe_points)
elif mode == 'G':
	graham()
elif mode == 'D':
	division()
else:
	print("booooo")

print("Initial Point [%s], Final Point [%s]" % (root,end))
print("Safe Points %s" % safe_points)
	
print("Camino 1: Longitud [%s]" % len(path1))
print("Recorrido: " + str(path1))

print("Camino 2: Longitud [%s]" % len(path2))
print("Recorrido: " + str(path2))

print("Camino seleccionado: [%s]" % min(len(path1), len(path2)) )