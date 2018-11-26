#!/usr/bin/env python
#
import sys
import time
import math
import os
from collections import deque, namedtuple

Demanda = namedtuple('Demanda', 'in_,out')

A=['Plaza de Mayo','Perú','Piedras','Lima','Sáenz Peña','Congreso','Pasco','Alberti','Plaza Miserere','Loria','Castro Barros','Río de Janeiro','Acoyte','Primera Junta','Puan','Carabobo','San José de Flores','San Pedrito']
B=['Alem','Florida','Pellegrini','Uruguay','CallaoB','Pasteur','PueyrredónB','Gardel','Medrano','Gallardo','Malabia','Dorrego','Lacroze','Tronador','Los Incas','Echeverría','Rosas']
C=['Retiro','San Martín','Lavalle','Diagonal Norte','Avenida de Mayo','Moreno','Independencia','San Juan','Constitución']
D=['Catedral','9 de Julio','Tribunales','CallaoD','Facultad de Medicina','PueyrredónD','Agüero','Bulnes','Scalabrini Ortiz','Plaza Italia','Palermo','Carranza','Olleros','Hernández','Juramento','Congreso de Tucumán']
E=['Bolívar','Belgrano','Independencia','San José','Entre Ríos','Pichincha','Jujuy','Urquiza','Boedo','Avenida La Plata','Moreno','Emilio Mitre','Medalla Milagrosa','Varela','Plaza de los Virreyes']
H=['Facultad de Derecho','Las Heras','Santa Fe','Corrientes','Once','Venezuela','Humberto I','Inclán','Caseros','Parque Patricios','Hospitales']

class Vertex(object):
	def __init__(self, name):
		self.name = name
		self.in_ = 0
		self.out = 0
		
	def __repr__(self):
		return "%s->%s->%s" % (self.in_,self.name,self.out)

class Edge(object):
	def __init__(self, u, v, w):
		self.source = u
		self.sink = v
		self.capacity = w
		
	def __repr__(self):
		return "%s->%s:%s" % (self.source, self.sink, self.capacity)
		
class FlowNetwork(object):
	def __init__(self):
		self.adj = {}
		self.flow = {}
		
	def add_vertex(self, vertex):
		self.adj[vertex] = []
		
	def get_edges_(self):
		return self.adj
		
	def get_edges(self, v):
		return self.adj[v]
		
	def add_edge(self, u, v, w=0):
		if u == v:
			raise ValueError("u == v")
			
		edge = Edge(u,v,w)
		redge = Edge(v,u,0)
		edge.redge = redge #redge is not defined in Edge class
		redge.redge = edge
		self.adj[u].append(edge)
		self.adj[v].append(redge)
		self.flow[edge] = 0
		self.flow[redge] = 0
		
	def find_path(self, source, sink, path, path_set):
		if source == sink:
			return path
		
		#for edge in self.get_edges(source):
		for edge in self.get_edges(source):
			residual = edge.capacity - self.flow[edge]
			
			if residual > 0 and not (edge,residual) in path_set:
				path_set.add((edge, residual))
				result = self.find_path( edge.sink, sink, path +
				[(edge,residual)], path_set)
				
				if result != None:
					return result
				
	def max_flow(self, source, sink):
		global vertices
		
		path = self.find_path(source, sink, [], set())
		
		while path != None:
			flow = min(res for edge,res in path)
			
			for edge,res in path:
				self.flow[edge] += flow
				self.flow[edge.redge] -= flow
				
				if edge.source in vertices:
					vertices[edge.source].out += flow
				if edge.sink in vertices:
					vertices[edge.sink].in_ += flow
			
			path = self.find_path(source, sink, [], set())
			
		return self.flow,sum(self.flow[edge] for edge in self.get_edges(source))

vertices={'Plaza de Mayo':Vertex('Plaza de Mayo'),'Perú':Vertex('Perú'),'Piedras':Vertex('Piedras'),'Lima':Vertex('Lima'),'Sáenz Peña':Vertex('Sáenz Peña'),'Congreso':Vertex('Congreso'),'Pasco':Vertex('Pasco'),'Alberti':Vertex('Alberti'),'Plaza Miserere':Vertex('Plaza Miserere'),'Loria':Vertex('Loria'),'Castro Barros':Vertex('Castro Barros'),'Río de Janeiro':Vertex('Río de Janeiro'),'Acoyte':Vertex('Acoyte'),'Primera Junta':Vertex('Primera Junta'),'Puan':Vertex('Puan'),'Carabobo':Vertex('Carabobo'),'San José de Flores':Vertex('San José de Flores'),'San Pedrito':Vertex('San Pedrito'),'Alem':Vertex('Alem'),'Florida':Vertex('Florida'),'Pellegrini':Vertex('Pellegrini'),'Uruguay':Vertex('Uruguay'),'CallaoB':Vertex('CallaoB'),'Pasteur':Vertex('Pasteur'),'PueyrredónB':Vertex('PueyrredónB'),'Gardel':Vertex('Gardel'),'Medrano':Vertex('Medrano'),'Gallardo':Vertex('Gallardo'),'Malabia':Vertex('Malabia'),'Dorrego':Vertex('Dorrego'),'Lacroze':Vertex('Lacroze'),'Tronador':Vertex('Tronador'),'Los Incas':Vertex('Los Incas'),'Echeverría':Vertex('Echeverría'),'Rosas':Vertex('Rosas'),'Retiro':Vertex('Retiro'),'San Martín':Vertex('San Martín'),'Lavalle':Vertex('Lavalle'),'Diagonal Norte':Vertex('Diagonal Norte'),'Avenida de Mayo':Vertex('Avenida de Mayo'),'Moreno':Vertex('Moreno'),'Independencia':Vertex('Independencia'),'San Juan':Vertex('San Juan'),'Constitución':Vertex('Constitución'),'Catedral':Vertex('Catedral'),'9 de Julio':Vertex('9 de Julio'),'Tribunales':Vertex('Tribunales'),'CallaoD':Vertex('CallaoD'),'Facultad de Medicina':Vertex('Facultad de Medicina'),'PueyrredónD':Vertex('PueyrredónD'),'Agüero':Vertex('Agüero'),'Bulnes':Vertex('Bulnes'),'Scalabrini Ortiz':Vertex('Scalabrini Ortiz'),'Plaza Italia':Vertex('Plaza Italia'),'Palermo':Vertex('Palermo'),'Carranza':Vertex('Carranza'),'Olleros':Vertex('Olleros'),'Hernández':Vertex('Hernández'),'Juramento':Vertex('Juramento'),'Congreso de Tucumán':Vertex('Congreso de Tucumán'),'Bolívar':Vertex('Bolívar'),'Belgrano':Vertex('Belgrano'),'Independencia':Vertex('Independencia'),'San José':Vertex('San José'),'Entre Ríos':Vertex('Entre Ríos'),'Pichincha':Vertex('Pichincha'),'Jujuy':Vertex('Jujuy'),'Urquiza':Vertex('Urquiza'),'Boedo':Vertex('Boedo'),'Avenida La Plata':Vertex('Avenida La Plata'),'Moreno':Vertex('Moreno'),'Emilio Mitre':Vertex('Emilio Mitre'),'Medalla Milagrosa':Vertex('Medalla Milagrosa'),'Varela':Vertex('Varela'),'Plaza de los Virreyes':Vertex('Plaza de los Virreyes'),'Facultad de Derecho':Vertex('Facultad de Derecho'),'Las Heras':Vertex('Las Heras'),'Santa Fe':Vertex('Santa Fe'),'Corrientes':Vertex('Corrientes'),'Once':Vertex('Once'),'Venezuela':Vertex('Venezuela'),'Humberto I':Vertex('Humberto I'),'Inclán':Vertex('Inclán'),'Caseros':Vertex('Caseros'),'Parque Patricios':Vertex('Parque Patricios'),'Hospitales':Vertex('Hospitales')}

		
# main
if len(sys.argv) != 4:
	print("Invalid input.\nUsage: \n\t subtes variablesFilepath demandasFilepath capacidadesFilePath")
	sys.exit(1)

filename_1 = sys.argv[1]
filename_2 = sys.argv[2]
filename_3 = sys.argv[3]

#
input_1 = open(filename_1, "r")
input_2 = open(filename_2, "r")
input_3 = open(filename_3, "r")

maxPersonas = 0
minVagonesLineaA = 0
minVagonesLineaB = 0
minVagonesLineaC = 0
minVagonesLineaD = 0
minVagonesLineaE = 0
minVagonesLineaH = 0
vagonesFlota = 0

demandas = {}
S = []
T = []

g = FlowNetwork()

for line in input_1:
	line = line.rstrip('\n')
	if line.startswith('#') or not line:
		continue
	
	variables = line.split(",")
	
	maxPersonas = int(variables[0])
	minVagonesLineaA = int(variables[1])
	minVagonesLineaB = int(variables[2])
	minVagonesLineaC = int(variables[3])
	minVagonesLineaD = int(variables[4])
	minVagonesLineaE = int(variables[5])
	minVagonesLineaH = int(variables[6])
	vagonesFlota = int(variables[7])

for line in input_2:
	line = line.rstrip('\n')
	if line.startswith('#') or not line:
		continue
	
	datos_demanda = line.split(",")
	estacion = datos_demanda[0]
	f = Demanda(in_=int(datos_demanda[1]),out=int(datos_demanda[2]))
	
	demandas[estacion] = f
	
	if f.in_ - f.out < 0:
		S.append(estacion)
	elif f.in_ - f.out > 0:
		T.append(estacion)
		
	g.add_vertex(estacion)
	
#
for line in input_3:
	line = line.rstrip('\n')
	if line.startswith('#') or not line:
		continue
		
	info_tramo = line.split(",")
	# info_tramo = estacion i | estacion j | capacidad
	g.add_edge(info_tramo[0],info_tramo[1],int(info_tramo[2]) * maxPersonas)

g.add_vertex('s')
g.add_vertex('t')
	
for v in S:
	g.add_edge('s', v, -(demandas[v].in_ - demandas[v].out))

for u in T:
	g.add_edge(u, 't', demandas[u].in_ - demandas[u].out)
	
#edges = g.get_edges_()	
#for edge in edges.items():
#	print(edge)

paths, max_flow_value = g.max_flow('s','t')

demandA = sum(vertices[v].in_ for v in A) / maxPersonas
demandB = sum(vertices[v].in_ for v in B) / maxPersonas 
demandC = sum(vertices[v].in_ for v in C) / maxPersonas
demandD = sum(vertices[v].in_ for v in D) / maxPersonas
demandE = sum(vertices[v].in_ for v in E) / maxPersonas
demandH = sum(vertices[v].in_ for v in H) / maxPersonas

demandaSistema = demandA+demandB+demandC+demandD+demandE+demandH

if max_flow_value == 0:
	print("No es factible brindar un buen servicio ya que no se pueden respetar las demandas de flujo entrante y saliente de las estaciones.")
	exit(5)
else:
	print ("Flujo Maximo: %s personas/hora" % str(max_flow_value))

if demandA < minVagonesLineaA:
	print("Línea A tiene %s vagones/hora. No cumple contrato (min %s). No es factible brindar un buen servicio." % (demandA,minVagonesLineaA))
	sys.exit(2)

if demandB < minVagonesLineaB:
	print("Línea B tiene %s vagones/hora. No cumple contrato (min %s). No es factible brindar un buen servicio." % (demandB,minVagonesLineaB))
	sys.exit(2)

if demandC < minVagonesLineaC:
	print("Línea C tiene %s vagones/hora. No cumple contrato (min %s). No es factible brindar un buen servicio." % (demandC,minVagonesLineaC))
	sys.exit(2)

if demandD < minVagonesLineaD:
	print("Línea D tiene %s vagones/hora. No cumple contrato (min %s). No es factible brindar un buen servicio." % (demandD,minVagonesLineaD))
	sys.exit(2)

if demandE < minVagonesLineaE:
	print("Línea E tiene %s vagones/hora. No cumple contrato (min %s). No es factible brindar un buen servicio." % (demandE,minVagonesLineaE))
	sys.exit(2)

if demandH < minVagonesLineaH:
	print("Línea H tiene %s vagones/hora. No cumple contrato (min %s). No es factible brindar un buen servicio." % (demandH,minVagonesLineaH))
	sys.exit(2)

if demandaSistema > vagonesFlota:
	print("Se necesitan más vagones de los disponibles en la flota. No es factible brindar un buen servicio.")
	sys.exit(3)
