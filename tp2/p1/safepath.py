#!/usr/bin/env python

import sys
import time
import math
import os
import numpy as np
from collections import deque, namedtuple

Edge = namedtuple('Edge', 'start, end, distance')
Coordinate = namedtuple('Coordinate', 'x,y')

def make_edge(start, end, distance=1):
  return Edge(start, end, distance)
  
class Graph():

	def __init__(self, edges):
		self.edges = edges
		
	def add_edge(self, n1, n2, distance=1):
		#print("add_edge [%s] [%s] [%s]" % (n1,n2,distance))
		self.edges.append(Edge(start=n1, end=n2, distance=distance))

	def add_edge2(self, edge):
		#print("add_edge [%s] [%s] [%s]" % (edge))
		self.edges.append(edge)
			
	def remove_edge(self, edge):
		self.edges.remove(edge)
	
	@property
	def adjacents(self):
		adjacents = {vertex: set() for vertex in self.vertices}
		for edge in self.edges:
			adjacents[edge.start].add((edge.end, edge.distance))
			adjacents[edge.end].add((edge.start, edge.distance))
		return adjacents

	@property
	def vertices(self):
		return set(
			sum(
				([edge.start, edge.end] for edge in self.edges), []
			)
		)

	def dijkstra (self, s, t):
		distances = {vertex: np.inf for vertex in self.vertices}
		
		previous_vertices = {
			vertex: None for vertex in self.vertices
        }		
		
		distances[s] = 0
		
		vertices = self.vertices.copy()
		
		while vertices:
			current_vertex = min(vertices, key=lambda vertex: distances[vertex])
			
			if distances[current_vertex] == np.inf:
				break
		
			for adjacent, distance in self.adjacents[current_vertex]:
				alternative_route = distances[current_vertex] + distance
				
				if alternative_route < distances[adjacent]:
					distances[adjacent] = alternative_route
					previous_vertices[adjacent] = current_vertex
					
			vertices.remove(current_vertex)
			
		path, current_vertex = deque(), t
		
		while previous_vertices[current_vertex] is not None:
			path.appendleft(current_vertex)
			current_vertex = previous_vertices[current_vertex]
		if path:
			path.appendleft(current_vertex)
		return path
		
		print("dijkstra %s" % distances)
		
def which_side_of_line (lineEndptA, lineEndptB, ptSubject):
    return (ptSubject.x - lineEndptA.x) * (lineEndptB.y - lineEndptA.y) - (ptSubject.y - lineEndptA.y) * (lineEndptB.x - lineEndptA.x)

def distance(p1, p2):
	return math.sqrt(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2))
	
def fuerza_bruta(s, t, safe_points):
	print("fuerzabruta [%s] [%s] [%s]" % (s, t, safe_points))
	
	minimum_convex_hull = []
	s_present = False
	t_present = False
		
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
				
				d = which_side_of_line(pointI, pointJ, safe_points[k])
				if d < 0:
					allPointsOnTheRight = False
					break
			
			if allPointsOnTheRight:
				e = Edge(start=pointI, end=pointJ, distance=distance(pointI, pointJ))
				
				if pointI == s or pointJ == s:
					s_present = True
					
				if pointI == t or pointJ == t:
					t_present = True
								
				if e not in minimum_convex_hull:
					minimum_convex_hull.append(e)
	
	if not t_present or not s_present:
		print("ERROR: Convex Hull does not contain source or tail.")
		sys.exit(500)	
	
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
convex_hull = []
path1 = []
path2 = []
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
		
	g = Graph([])
    
	for edge in convex_hull:
		g.add_edge2(edge)
				
	path1=g.dijkstra(s, t)

elif mode == 'G':
	graham()
elif mode == 'D':
	division()
else:
	print("Method [%s] is not valid." % mode)
	os._exit(-1)

#print("###################")	
#print("Initial Point [%s], Final Point [%s]" % (s,t))
#print("Safe Points %s" % safe_points)
	
print("###################\n\n")
print("Camino 1: Longitud [%s]" % len(path1))
print("Recorrido: " + str(path1))

print("Camino 2: Longitud [%s]" % len(path2))
print("Recorrido: " + str(path2))

print("Camino seleccionado: [%s]" % min(len(path1), len(path2)) )