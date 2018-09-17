#!/usr/bin/env python
import sys
import random
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
# bandas restantes, bandas_restantes[i]=j -> j es la cantidad restantes de bandas que puede contratar el recital i
bandas_restantes=[X for x in range(N)]

# recitales_x_banda[x][y]=j -> j es el n° del recital aceptado por la banda x
recitales_x_banda=[[-1 for x in range(Y)] for y in range(M)]

# carga de recitales y sus preferencias
for x in range(1,N+1):
	recitales[x-1]=random.sample(range(1,M+1), M)

	filename = 'test/recital_'+str(x)
	recital = open(filename, "w")
	
	recitales_restantes.append(x)
	
	for y in range(M):
		recital.write(str(recitales[x-1][y])+'\n')
	
# carga de bandas y sus preferencias
for x in range(1,M+1):
	bandas[x-1]=random.sample(range(1,N+1), N)
	
	filename = 'test/banda_'+str(x)
	banda = open(filename, "w")
	
	for y in range(N):
		banda.write(str(bandas[x-1][y])+'\n')	
	
while len(recitales_restantes) > 0 :
	nuevo_recital = recitales_restantes.popleft()
	
	while bandas_restantes[nuevo_recital-1] >= 1:
		bandas_restantes[nuevo_recital-1]-=1
		posicion_banda_actual = proxima_banda[nuevo_recital-1]
		
		if posicion_banda_actual < M: 
			proxima_banda[nuevo_recital-1] = posicion_banda_actual+1
		else: 
			break
		
		banda = recitales[nuevo_recital-1][posicion_banda_actual]
		
		menos_favorito = -1
		chequear_menos_favorito = True
		
		for x in range(Y):
			recital_actual = recitales_x_banda[banda-1][x]
						
			if recital_actual == -1: 
				recitales_x_banda[banda-1][x] = nuevo_recital
				chequear_menos_favorito = False
				break
			else: 
				pref_banda = bandas[banda-1]
				if pref_banda.index(nuevo_recital) > pref_banda.index(recital_actual):
					bandas_restantes[nuevo_recital-1]+=1
					chequear_menos_favorito = False
					continue
				else: 
					if menos_favorito == -1:
						menos_favorito = x
						chequear_menos_favorito = True
					else: 
						recital_menos_favorito = recitales_x_banda[banda-1][menos_favorito]
						
						if pref_banda.index(recital_actual) > pref_banda.index(recital_menos_favorito):
							menos_favorito = x
							chequear_menos_favorito = True
							
		if chequear_menos_favorito:
			## asigno menos favorito
			recital_menos_favorito = recitales_x_banda[banda-1][menos_favorito]
			recitales_x_banda[banda-1][menos_favorito] = nuevo_recital
			bandas_restantes[recital_menos_favorito-1]+=1
			if recital_menos_favorito not in recitales_restantes:
				recitales_restantes.append(recital_menos_favorito)
	
print("\nRecitales por banda: ")
for x in range(M):
	print("\nBanda ["+str(x)+"]: " + str(recitales_x_banda[x]))
