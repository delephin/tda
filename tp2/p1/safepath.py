#!/usr/bin/env python

import sys
import time
import math
import os
import operator
import functools
from collections import deque, namedtuple
import grahamScan

Edge = namedtuple('Edge', 'start, end, distance')
Coordinate = namedtuple('Coordinate', 'x,y')
WeightedPath = namedtuple('WeightedPath', 'path,weight')

centroid = Coordinate(0,0)

#####		
def get_key(item):
    return item.x	
	
def distance(p1, p2):
	return math.sqrt(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2))

## Checks whether the line is crossing the polygon, 
# Se utiliza para saber de que lado esta el punto c con respecto
# a la linea segmento de linea ab
def orientation(a, b, c):
	res = (b.y-a.y)*(c.x-a.x) - (c.y-a.y)*(b.x-a.x)
	
	if res == 0:
		return 0
	if res > 0:
		return 1
	return -1	

def quad(p):
	if (p.x >= 0 and p.y >= 0):
		return 1
	if (p.x <= 0 and p.y >= 0):
		return 2
	if (p.x <= 0 and p.y <= 0):
		return 3
	return 4
	
def counterclockwise_sorting(item1, item2):
	result = 0
	
	p = Coordinate(x=(item1.x-centroid.x),y=(item1.y-centroid.y))
	q = Coordinate(x=(item2.x-centroid.x),y=(item2.y-centroid.y))
	
	quad_item1=quad(p)
	quad_item2=quad(q)
	
	if quad_item1 != quad_item2: 
		result = -1 if quad_item1 < quad_item2 else 1
	else:
		result = -1 if (p.y*q.x < q.y*p.x) else 1
	
	return result

def merger(left_hull,right_hull):
	
	len_left = len(left_hull)
	len_right = len(right_hull)
	
	idx_righmost_a = 0
	idx_leftmost_b = 0

	for i in range(1,len_left):
		if left_hull[i].x > left_hull[idx_righmost_a].x:
			idx_righmost_a=i
	
	for i in range(1,len_right):
		if right_hull[i].x < right_hull[idx_leftmost_b].x:
			idx_leftmost_b=i
	
	#finding the upper tangent
	inda = idx_righmost_a
	indb = idx_leftmost_b
	done = False
	while not done:
		done = True
				
		while (orientation(right_hull[indb], left_hull[inda], left_hull[(inda+1)%len_left]) >= 0):
			inda = (inda+1)%len_left
			
		while (orientation(left_hull[inda],right_hull[indb],right_hull[(len_right+indb-1)%len_right]) <= 0):
			indb = (len_right+indb-1)%len_right
			done = False
		
	uppera = inda
	upperb = indb
	inda = idx_righmost_a
	indb = idx_leftmost_b
	done = 0

	# The edge ab is a tangent if the two points about a and the two points about b are on the same side of ab.
	
	g = 0
	# finding the lower tangent 
	while not done:
		done = 1
		while (orientation(left_hull[inda], right_hull[indb], right_hull[(indb+1)%len_right])>=0): 
			indb=(indb+1)%len_right 
	
		while orientation(right_hull[indb], left_hull[inda], left_hull[(len_left+inda-1)%len_left])<=0:
			inda=(len_left+inda-1)%len_left
			done=0
	
	lowera = inda
	lowerb = indb
	ret = []

	# ret contains the convex hull after merging the two convex hulls 
	# with the points sorted in anti-clockwise order 
	ind = uppera
		
	last_point = left_hull[uppera]
	ret.append(left_hull[uppera])
	
	while (ind != lowera):
		ind = (ind+1)%len_left
		new_point = left_hull[ind]
		ret.append(new_point)
		last_point = new_point

	ind = lowerb
	
	new_point = right_hull[lowerb]
	
	last_point = new_point
	
	ret.append(right_hull[lowerb])
	while ind != upperb:
		ind = (ind+1)%len_right
		new_point = right_hull[ind]
		ret.append(new_point)
		last_point = new_point
	
	return ret
	
def divide(s,t,points):
	if len(points) > 2 and len(points) <= 6:
		return fuerza_bruta(s,t,points)
	
	half = len(safe_points)//2
	right=points[half:]
	left=points[:half]

	fuerza_bruta_der = divide(s,t,right)
	fuerza_bruta_izq = divide(s,t,left)
	
	if (s not in fuerza_bruta_der and s not in fuerza_bruta_izq):
		print("ERROR: Convex Hull does not contain source.")
		sys.exit(500)
	
	if (t not in fuerza_bruta_izq and t not in fuerza_bruta_der):
		print("ERROR: Convex Hull does not contain tail.")
		sys.exit(500)
	
	merge = merger(fuerza_bruta_izq, fuerza_bruta_der)
	
	return merge
#####

def fuerza_bruta(s, t, safe_points):	
	global centroid
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
				
				d = orientation(pointI, pointJ, safe_points[k])
				if d < 0:
					allPointsOnTheRight = False
					break
					
			if allPointsOnTheRight:
				if pointI not in minimum_convex_hull:
					minimum_convex_hull.append(pointI)
				if pointJ not in minimum_convex_hull:
					minimum_convex_hull.append(pointJ)
			
	x = [p.x for p in minimum_convex_hull]
	y = [p.y for p in minimum_convex_hull]
	
	centroid = Coordinate(x=(sum(x) / len(minimum_convex_hull)), y=(sum(y) / len(minimum_convex_hull)))

	sorted_minimum_convex_hull = sorted(minimum_convex_hull, key=functools.cmp_to_key(counterclockwise_sorting))
				
	return sorted_minimum_convex_hull
	
def armar_caminos(s,t,convex_hull):
	idx_s = convex_hull.index(s)
	idx_t = convex_hull.index(t)
	
	weight_1 = 0
	weight_2 = 0
	
	if idx_t < idx_s:
		path1 = convex_hull[idx_s:]
		path1.extend(convex_hull[0:idx_t+1])
	else:
		path1 = convex_hull[idx_s:idx_t+1]
    
	path2 = []
	path2.append(s)
	
	if idx_t > idx_s:
		if idx_s != 0:
			path2.extend(convex_hull[:idx_s])
			
		if idx_t != len(convex_hull):
			for i in range(len(convex_hull)-1,idx_t,-1):
				path2.append(convex_hull[i])
			
	else:
		if idx_s != 0:
			for i in range(idx_s-1,idx_t,-1):
				path2.append(convex_hull[i])
	path2.append(t)
	
	for i in range(1,len(path1)):
		weight_1 += distance(path1[i-1],path1[i])	
	for i in range(1,len(path2)):
		weight_2 += distance(path2[i-1],path2[i])
	
	return (WeightedPath(path=path1,weight=weight_1), WeightedPath(path=path2,weight=weight_2))

def division_conquista(s, t, safe_points):
	#ordenar los puntos por su componente x
	sorted_points = sorted(safe_points, key=get_key)
	
	result = divide(s,t,sorted_points)
		
	return result
	
if len(sys.argv) != 3 :
	print("Invalid input.\nUsage: \n\t safepath inputFilepath F|G|D")
	sys.exit(1)
	
filename = sys.argv[1]
mode=sys.argv[2]

#
#
convex_hull = []
path1 = None
path2 = None
s = ()
t = ()
safe_points = []

input = open(filename, "r")

for line in input:
	line = line.rstrip('\n')
	coordinates = line.split(" ")
	safe_points.append(Coordinate(x=int(coordinates[0]), y=int(coordinates[1])))

s = safe_points[0]
t = safe_points[1]

if mode == 'F':
	convex_hull = fuerza_bruta(s, t, safe_points)
		
	if s not in convex_hull or t not in convex_hull:
		print("ERROR: Convex Hull does not contain source or tail.")
		sys.exit(500)
	
	path1,path2=armar_caminos(s,t,convex_hull)
	
elif mode == 'G':
	convex_hull=grahamScan.convex_hull(safe_points)
	
	if s not in convex_hull or t not in convex_hull:
		print("ERROR: Convex Hull does not contain source or tail.")
		sys.exit(500)
		
	path1,path2=armar_caminos(s,t,convex_hull)
elif mode == 'D':
	convex_hull=division_conquista(s, t, safe_points)
	
	if s not in convex_hull or t not in convex_hull:
		print("ERROR: Convex Hull does not contain source or tail.")
		sys.exit(500)	
	path1,path2=armar_caminos(s,t,convex_hull)
else:
	print("Method [%s] is not valid." % mode)
	os._exit(-1)
	
print("Camino 1: Longitud [%s]" % path1.weight)
print("Recorrido: " + str(path1.path))

print("Camino 2: Longitud [%s]" % path2.weight)
print("Recorrido: " + str(path2.path))

print("Camino seleccionado: [%s]" % (1 if path1.weight < path2.weight else 2))
