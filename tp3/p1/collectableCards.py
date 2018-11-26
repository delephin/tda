#!/usr/bin/env python
import sys
from utils import analisys_greedy, greedy, dynamic

if len(sys.argv) < 3 :
  print("Error: faltan argumentos.\n(Ej. 'python collectableCards.py test3.txt 14 G' o 'python collectableCards.py test3.txt A')")
  sys.exit(1)

filename = sys.argv[1]
mode = sys.argv[2]
cards = int(sys.argv[3])
packets = []

for line in open(filename, 'r'):
  packets.append(int(line.rstrip('\n')))

if(mode not in ['A','G','D']):
  print("Error: modo incorrecto")
  sys.exit(1)

if cards <= 0:
    print(f'Error: número de cartas incorrecto ({cards})')
    sys.exit(1)

if mode == 'A':
  S, c = analisys_greedy(packets)
  if(not S):
    print('No es factible resolver el problema mediante un algoritmo greedy')
    print(f'para sobres de {packets} y {cards} cartas')
    print(f'algoritmo greedy:      {c[1]}')
    print(f'programación dinámica: {c[2]}')
  else:
    print(S, c)

print(f'sobres: {packets}, cartas: {cards}')
if mode == 'G':
  S, q = greedy(cards,packets)
if mode == 'D':
  S, q = dynamic(cards, packets)
print(f'configuración: {S}')
print(f'cantidad de sobres: {q}')
