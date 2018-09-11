# TP 1

## Integrantes del grupo

* Errázquin Martín, padrón 98017
* **hola1**
* **hola2**
* **hola3**

## Parte 1: Variante de Gale Shapley

### 1. Pseudocódigo

**hola4**

### 2. Análisis de complejidad

**hola5**

### 3. Condiciones para solución estable y/o perfecta

**hola6**

### 4. Rankings no estrictos

**hola7**

### 5. Simulaciones

**hola8**

### 6. Comparación complejidad teoría vs implementación

**hola9**

## Parte 2: Criba de Eratóstenes

### 1. Pseudocódigo solución eficiente

Sea N un natural > 1, X un arreglo de tamaño N con todos valores True.

~~~
para i = 2, 3, 4, ... no más de N^1/2:
  si X[i] es True:
    para j = i^2, i^2+i, i^2+2i,... no más de N:
      A[j] <- False
devolver lista de todos los X[i] que son True
~~~

### 2. Análisis de complejidad

Siendo que modificar A[j] es O(1), notamos que dado un i primo, la cantidad de valores que toma
j está acotada por N/i. Del [*segundo teorema de Merthens*](https://en.wikipedia.org/wiki/Mertens%27_theorems#Mertens'_second_theorem_and_the_prime_number_theorem) se observa que la sumatoria de 1/p para todos los primos p está acotada por log log n, luego para un primo i setear todos sus múltiplos como no-primos es O(log log N), y como el primer loop está acotado por N^1/2^ **este algoritmo es O(N^1/2^ log log N)**.

### 3. Pseudocódigo solución fuerza bruta y análisis de complejidad

**hola10**

### 4. Programar puntos 1 y 3

**placeholder, acá no va nada solo hay que codear**

### 5. Gráfico tiempos de ejecución

**hola11**

### 6. Análisis de resultados

**hola12**
