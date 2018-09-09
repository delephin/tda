#!/usr/bin/env python
import sys
from collections import deque

if len(sys.argv) < 4 :
	print("Error: Faltan argumentos de entrada. \n\t gale_shapley N M X Y")
	sys.exit(1)
	
N=int(sys.argv[1])
M=int(sys.argv[2])
X=int(sys.argv[3])
Y=int(sys.argv[4])

print("Gale Shapley \n Cantidad de Recitales: " + str(N) + " \n Cantidad de Bandas: " + str(M) + " \n Bandas por Recital: " + str(X) + "\n Recitales por banda: " + str(Y) )

if X > M :
	print("Error: No hay " + X + " bandas configuradas.")
	sys.exit(2)
	
if Y > N :
	print("Error: No hay " + Y + " recitales configuradas.")
	sys.exit(3)

recitales_restantes = deque()	
	
recitales=[[0 for x in range(M)] for y in range(N)] 
bandas=[[0 for x in range(N)] for y in range(M)] 

# proxima_banda[i]=j -> j es el n° de la proxima banda preferida del recital i
proxima_banda=[0 for x in range(N)]
# recital_x_banda[i]=j -> j es el n° del recital aceptado por la banda i
recital_x_banda=[-1 for x in range(M)]

# carga de recitales y sus preferencias
for x in range(1,N+1):
	filename = 'dataset_1/recital_'+str(x)
	recital = open(filename)
	
	recitales_restantes.append(x)
	
	y = 0
	for line in recital:
		recitales[x-1][y]=int(line)
		y+=1
	
# carga de bandas y sus preferencias
for x in range(1,M+1):
	filename = 'dataset_1/banda_'+str(x)
	banda = open(filename)
	y = 0
	for line in banda:
		bandas[x-1][y]=int(line)
		y+=1
	
counter = 0	

#while len(recitales_restantes) > 0 and counter < 50:
while len(recitales_restantes) > 0 :
	nuevo_recital = recitales_restantes.popleft()

	posicion_banda_actual = proxima_banda[nuevo_recital-1]
	
	proxima_banda[nuevo_recital-1] = posicion_banda_actual+1
	
	banda = recitales[nuevo_recital-1][posicion_banda_actual]

	recital_actual = recital_x_banda[banda-1]
	
	proxima_banda[nuevo_recital-1]
	
	print("procesando recital ["+str(nuevo_recital)+"]")
	
	if recital_actual == -1: 
		print("primera asignacion b["+str(banda)+"] r["+str(nuevo_recital)+"]")
		recital_x_banda[banda-1] = nuevo_recital
	else: 
		print(" b["+str(banda)+"] tiene r["+str(recital_actual)+"]")
		pref_banda = bandas[banda-1]
		if pref_banda.index(nuevo_recital) > pref_banda.index(recital_actual):
			print(" b["+str(banda)+"] prefiere su actual ["+str(recital_actual)+"] a ["+str(nuevo_recital)+"]")
			recitales_restantes.append(nuevo_recital)
		else:
			print(" b["+str(banda)+"] prefiere el nuevo ["+str(nuevo_recital)+"] al actual ["+str(recital_actual)+"]")
			recital_x_banda[banda-1] = nuevo_recital
			recitales_restantes.append(recital_actual)
	
	counter+=1
	
print("\nRecitales: " + str(recital_x_banda))