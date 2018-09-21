# TP 1

## Integrantes del grupo

* Bollero, Carlos  93542
* Czop, Guillermo 98059
* Errázquin, Martín 98017
* Escobar, Cynthia 85826

## Parte 1: Variante de Gale Shapley

### 1. Pseudocódigo

**S** = {}

Mientras haya recitales que todavía puedan contratar bandas y no se haya comunicado con todas las bandas:

	Seleccionar recital **r** de los que cumplen la condición anterior

​	Sea **b** la banda que mejor rankea en la lista de preferencias de **r**, y **b** no fue contactada previamente por **r**

​	Si **b** participa en  **k** recitales, con 0<**k** < **Y** entonces:

		se agrega **(b, r)**  a **S**

		se aumenta la cantidad de bandas que contrató el recital **r**

		se aumenta la cantidad de recitales que aceptó la banda **b**

	Si **b** ya participa en  **Y** recitales, entonces:

		Sea **~r** el recital menos preferido de **b**

​		Por cada recital **r'** previamente aceptado por **b**

​			Si **b** prefiere más al recital **r'** que al nuevo **r**, continúo

​			Si **b** prefiere más el nuevo recital **r** que al existente **r'**

				Si **~r** no está seteado o si **b** prefiere más a **~r** que a **r' **-> **~r** = **r'**

​		Si existe **~r** entonces:

​                        **b** rechaza a **~r** ->  quita  **(b,~r)**  de **S**

​			**~r** se encola para ser procesada posteriormente

​			se disminuye la cantidad de bandas que tiene contratadas **~r**

​			 **b** acepta a **r**  ->  se agrega **(b, r)**  a **S**

​			se aumenta la cantidad de bandas que contrató el recital **r**

retorna **S**		

### 2. Análisis de complejidad

Partiendo de que la complejidad de Gale-Shapley es O(n^2), podemos decir que para esta variante tenemos:

1. Inicialmente, una complejidad O(NxM) si cada recital pudiera contratar sólo 1 banda, y una banda sólo pudiera participar en 1 recital
2. Luego, si agregamos la variación de que un recital puede contratar X bandas, se iterará X veces por cada recital. Podemos decir entonces que la complejidad sería O(NxXxM)
3. Finalmente, si agregamos la variación de que cada banda puede participar de Y recitales, en el peor de los casos deberíamos validar contra cada uno de los Y recitales ya aceptados para comprobar que una propuesta nueva no es mejor. Con esto podemos decir que la complejidad final sería O(NxXxMxY)

### 3. Condiciones para solución estable y/o perfecta

Para esta versión de Gale-Shapley consideramos que una solución es perfecta si todo recital logra contratar alguna banda, y toda banda puede participar en algún recital.

En el único caso en el que habrá match perfecto es cuando N==M y X==Y.

Para N==M o N<>M:

- X < Y, no habrá match perfecto ya que algunas bandas podrían quedar sin participar en algún recital.
- X > Y, no habrá match perfecto ya que algunos recitales podrían quedarse sin bandas.

Independientemente del la cantidad de bandas y recitales y de las restricciones, la solución es estable ya que los pares banda-recital formados son inmejorables, incluso en los casos en los que quedan recitales o bandas libres. 

### 4. Rankings no estrictos

El algoritmo actual no soporta que un organizador tenga la misma preferencia para bandas diferentes (o visceversa) dado que nos basamos en el orden de inserción en las distintas estructuras de datos para determinar el orden de preferencia. Si se quisiera soportar este comportamiento, deberíamos cambiar las estructuras que estamos utilizando actualmente.

Suponiendo que el algoritmo soportara un mismo orden de preferencia para varias bandas/organizadores, y que el mecanismo de desempate sea arrojar una moneda entonces no alcanzaría con preguntar si se prefiere más a uno u a otro (recital/banda) ya que también podría preferirse a ambos en un mismo grado, y en ese caso se arrojaría la moneda para resolver la preferencia. Es decir:

**S** = {}

Mientras haya recitales que todavía puedan contratar bandas y no se haya comunicado con todas las bandas:

​	Seleccionar recital **r** de los que cumplen la condición anterior

​	Sea **b** la banda que mejor rankea en la lista de preferencias de **r**, y **b** no fue contactada previamente por **r**

​	Si **b** participa en  **k** recitales, con 0<**k** < **Y** entonces:

​		se agrega **(b, r)**  a **S**

		se aumenta la cantidad de bandas que contrató el recital **r**

​		se aumenta la cantidad de recitales que aceptó la banda **b**

​	Si **b** ya participa en  **Y** recitales, entonces:

​		Sea **~r** el recital menos preferido de **b**

​		Por cada recital **r'** previamente aceptado por **b**

==​			Si **b** prefiere a **r** y **r'** en un mismo grado:==

==​				Arrojo moneda, determino a quién a quién prefiere más y evalúo contra las condiciones ***(a)*** y ***(b)***==

​			Si **b** prefiere más al recital **r'** que al nuevo **r**, continúo ***(a)***

​			Si **b** prefiere más el nuevo recital **r** que al existente **r'** ***(b)***

​				Si **~r** no está seteado o si **b** prefiere más a **~r** que a **r' **-> **~r** = **r'**

​		Si existe **~r** entonces:

​                        **b** rechaza a **~r** ->  quita  **(b,~r)**  de **S**

			**~r** se encola para ser procesada posteriormente

			se disminuye la cantidad de bandas que tiene contratadas **~r**

			 **b** acepta a **r**  ->  se agrega **(b, r)**  a **S**

			se aumenta la cantidad de bandas que contrató el recital **r**

retorna **S**		

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
      X[j] <- False
devolver lista de todos los i desde 2 hasta N tal X[i] es True
~~~

### 2. Análisis de complejidad

Siendo que modificar A[j] es O(1), notamos que dado un i primo, la cantidad de valores que toma
j está acotada por N/i. Del [*segundo teorema de Merthens*](https://en.wikipedia.org/wiki/Mertens%27_theorems#Mertens'_second_theorem_and_the_prime_number_theorem) se observa que la sumatoria de 1/p para todos los primos p está acotada por log log n, luego para un primo i setear todos sus múltiplos como no-primos es O(log log N), y como el primer loop está acotado por N^1/2^ **este algoritmo es O(N^1/2^ log log N)**.

### 3. Pseudocódigo solución fuerza bruta y análisis de complejidad

Sea N un natural > 1, L una lista vacía:

~~~
para i = 2, 3, 4, ... N:
  es_primo <- True
  para j = 2, ... no más de i^1/2:
    si i % j es 0:
      es_primo <- False
      break
  si es_primo es True:
    agregar i a L
devolver L
~~~

Suponiendo que agregar un elemento a L y obtener el resto de una división son operaciones O(1), como cada loop de j se completa en O(N^1/2^) y se realizan N de los mismos, **este algoritmo es O(N^3/2^)**.

### 4. Programar puntos 1 y 3

**placeholder, acá no va nada solo hay que codear**

### 5. Gráfico tiempos de ejecución

**hola11**

### 6. Análisis de resultados

**hola12**
