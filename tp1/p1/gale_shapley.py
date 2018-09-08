#!/usr/bin/env python
import sys

if len(sys.argv) < 4 :
	print("Error: Faltan argumentos de entrada. \n\t gale_shapley N M X Y")
	sys.exit(1)
	
N=sys.argv[1]
M=sys.argv[2]
X=sys.argv[3]
Y=sys.argv[4]

print("Gale Shapley \n Cantidad de Recitales: " + N + " \n Cantidad de Bandas: " + M + " \n Bandas por Recital: " + X + "\n Recitales por banda: " + Y )

if X > M :
	print("Error: No hay " + X + " bandas configuradas.")
	sys.exit(2)
	
if Y > N :
	print("Error: No hay " + Y + " recitales configuradas.")
	sys.exit(3)

	
