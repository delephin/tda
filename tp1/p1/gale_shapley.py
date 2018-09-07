#!/usr/bin/env python
import sys

N=sys.argv[1]
M=sys.argv[2]
X=sys.argv[3]
Y=sys.argv[4]

print("Gale Shapley \n Cantidad de Recitales: " + N + " \n Cantidad de Bandas: " + M + " \n Bandas por Recital: " + X + "\n Recitales por banda: " + Y )

if X > M :
	print("Error: No hay " + X + " bandas configuradas.")
	exit
	
if Y > N :
	print("Error: No hay " + Y + " recitales configuradas.")
	exit

