import sys
import array
import math
import time

BRUTE_FORCE_METHOD = "F"
EFFICIENT_METHOD = "E"

if len(sys.argv) < 2 :
	print("Error: Faltan argumentos de entrada. \n\t eratostenes E/F N")
	sys.exit(1)

METHOD = str(sys.argv[1])
N = int(sys.argv[2])

if METHOD not in [BRUTE_FORCE_METHOD, EFFICIENT_METHOD]:
    print("Error: modo de trabajo no reconocido")
    sys.exit(1)

if N <= 1:
    print("Error: N no es un entero mayor igual a 2")
    sys.exit(1)

def efficient_primes(n):
    startTime = time.time()
    X = array.array('b', [True] * n)
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(i**2, n, i):
            X[j] = False
    return [[m for m in range(2,n) if X[m] == True], "Elapsed time: "+	str(time.time() - startTime)]

def brute_force_primes(n):
    startTime = time.time()
    L = []
    for i in range(2,n):
        es_primo = True
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo is True:
            L.append(i)
    return [L, "Elapsed time: "+	str(time.time() - startTime)]

if __name__ == '__main__':
    if METHOD == EFFICIENT_METHOD:
        print(efficient_primes(N))
    elif METHOD == BRUTE_FORCE_METHOD:
        print(brute_force_primes(N))
    else:
        raise ValueError()
