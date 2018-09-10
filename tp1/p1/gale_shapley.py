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
# bandas restantes
bandas_restantes=[X for x in range(N)]

# recitales_x_banda[x][y]=j -> j es el n° del recital aceptado por la banda x
recitales_x_banda=[[-1 for x in range(Y)] for y in range(M)]

# carga de recitales y sus preferencias
for x in range(1,N+1):
	filename = 'dataset_2/recital_'+str(x)
	recital = open(filename)
	
	recitales_restantes.append(x)
	
	y = 0
	for line in recital:
		recitales[x-1][y]=int(line)
		y+=1
	
# carga de bandas y sus preferencias
for x in range(1,M+1):
	filename = 'dataset_2/banda_'+str(x)
	banda = open(filename)
	y = 0
	for line in banda:
		bandas[x-1][y]=int(line)
		y+=1
	
while len(recitales_restantes) > 0 :
	nuevo_recital = recitales_restantes.popleft()
	
	#print("#------------------------------------------------------------#")
	
	#print("procesando recital ["+str(nuevo_recital)+"] con ["+str(bandas_restantes[nuevo_recital-1])+"] bandas disponibles, de cola ["+str(recitales_restantes)+"]")
	
	while bandas_restantes[nuevo_recital-1] >= 1:
		bandas_restantes[nuevo_recital-1]-=1
		posicion_banda_actual = proxima_banda[nuevo_recital-1]
		
		if posicion_banda_actual < M: 
			proxima_banda[nuevo_recital-1] = posicion_banda_actual+1
		else: 
			break
		
		#print("------>>>>>>>>>> nuevo_recital ["+str(nuevo_recital-1)+"] posicion banda actual ["+str(posicion_banda_actual)+"]")
		
		banda = recitales[nuevo_recital-1][posicion_banda_actual]
		
		menos_favorito = -1
		chequear_menos_favorito = True
		
		for x in range(Y):
			#print("\tanalizando banda ["+str(banda)+"]["+str(x)+"]")
			recital_actual = recitales_x_banda[banda-1][x]
						
			if recital_actual == -1: 
			#	print("\tse asigna b["+str(banda)+"]["+str(x)+"] -> r["+str(nuevo_recital)+"]")
				recitales_x_banda[banda-1][x] = nuevo_recital
			#	print("\t.. ["+str(recitales_x_banda[banda-1])+"]")
				chequear_menos_favorito = False
				break
			else: 
			#	print(" b["+str(banda)+"] tiene r["+str(recital_actual)+"]")
				pref_banda = bandas[banda-1]
				if pref_banda.index(nuevo_recital) > pref_banda.index(recital_actual):
			#		print(" b["+str(banda)+"] prefiere su actual ["+str(recital_actual)+"] a ["+str(nuevo_recital)+"]")
					bandas_restantes[nuevo_recital-1]+=1
					chequear_menos_favorito = False
					continue
				else: 
					if menos_favorito == -1:
			#			print(" b["+str(banda)+"] prefiere el nuevo ["+str(nuevo_recital)+"] al actual ["+str(recital_actual)+"] menos favorito -> " + str(x))
						menos_favorito = x
						chequear_menos_favorito = True
					else: 
						recital_menos_favorito = recitales_x_banda[banda-1][menos_favorito]
						
						if pref_banda.index(recital_actual) > pref_banda.index(recital_menos_favorito):
			#				print(" b["+str(banda)+"] menos favorito anterio ["+str(menos_favorito)+"] nuevo menos favorito -> " + str(x) )
							menos_favorito = x
							chequear_menos_favorito = True
							
		if chequear_menos_favorito:
			## asigno menos favorito
			recital_menos_favorito = recitales_x_banda[banda-1][menos_favorito]
			recitales_x_banda[banda-1][menos_favorito] = nuevo_recital
			#print(".. ["+str(recitales_x_banda[banda-1])+"]")
			bandas_restantes[recital_menos_favorito-1]+=1
			#print("se encola ["+str(recital_menos_favorito)+"] con ["+str(bandas_restantes[recital_menos_favorito-1])+"] bandas disponibles")
			if recital_menos_favorito not in recitales_restantes:
				recitales_restantes.append(recital_menos_favorito)
	
print("\nRecitales por banda: ")
for x in range(M):
	print("\nBanda ["+str(x)+"]: " + str(recitales_x_banda[x]))
