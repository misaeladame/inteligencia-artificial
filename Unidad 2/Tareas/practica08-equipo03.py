"""
Practica 8 - Búsqueda local, Recocido Simulado.

Objetivo: Comprender la resolución de problemas mediante técnicas de búsqueda local, búsqueda con
recocido simulado (simulated annealing). Se corresponde con el Tema 2 “Técnicas de búsqueda” del 
programa de la materia.

Equipo: 3

Nombre: Piña Rosales Cristian Gabriel 
Número de Control: 18130588

Nombre: Adame Sandoval José Misael
Número de Control: 18131209

Nombre: Castro Luna Ricardo Raúl
Número de Control: 18131227

Nombre: Flores Ramos José Luis
Número de Control: 18131237

Nombre: Ruiz Martínez Kevin Alejandro
Número de Control: 18131280
"""

"""
El viajante de comercio.

El problema del viajante de comercio (travel salesman problem) es también un problema bastante
conocido y con bastantes aplicaciones prácticas que van desde el diseño de rutas de distribución hasta la
optimización del diseño de chips.

El planteamiento es muy sencillo, disponemos de un conjunto de N ciudades que debemos recorrer y
conocemos las distancias que conectan cada pareja de ciudades, debemos encontrar un camino que recorra
todas las ciudades una sola vez, comenzando y finalizando el recorrido en la misma ciudad. El objetivo es
encontrar el recorrido más corto posible.

El espacio de búsqueda esta formado por todos los posibles caminos que se pueden formar con las N
ciudades (N!), por lo que es impracticable encontrar la solución óptima.
Para solucionar ese problema primero nos hemos de plantear el espacio de búsqueda. En este caso
podemos considerar que esta formado por todos los caminos posibles que se pueden formar con las N
ciudades.

Como solución inicial podemos partir desde cualquier camino al azar o plantearnos encontrar una buena
solución inicial que nos reduzca el camino a recorrer en el espacio de búsqueda antes de encontrar un
óptimo local. Una heurística utilizada para encontrar una buena solución inicial en este problema consiste
en usar una estrategia avariciosa, comenzando en la primera ciudad vamos eligiendo la ciudad que no
hayamos visitado que se encuentre más cerca.

Como operadores de búsqueda tenemos muchas opciones, cualquier transformación de un recorrido nos
permite movernos en el espacio de búsqueda. Es una elección habitual el escoger un operador que
intercambia dos ciudades en el recorrido, esto supondría tener un factor de ramificación cuadrático,
asegurándonos que todos las soluciones son alcanzables. También podemos elegir otros operadores como
por ejemplo, mover un trozo del recorrido a una posición cualquiera o invertir el recorrido entre dos
ciudades, … El tener más operadores nos aumenta la conectividad en el espacio de soluciones, acortando
los caminos hacia los óptimos, pero obviamente aumenta el factor de ramificación.

La función heurística en este problema es la obvia, hemos de minimizar la longitud del recorrido. No
obstante, podemos plantear variantes del problema cambiando la función heurística, añadiendootras
restricciones que sean optimizadas por el algoritmo de búsqueda, como, por ejemplo, imponer que se
recorran ciertas ciudades en un orden específico o en grupos establecido

Elabore un programa en python que dé solución a este problema con el uso del algoritmo Recocido
Simulado (simulated annealing).
"""


"""
NOTA: En caso de un error(es) como los siguiente(s):
    ModuleNotFoundError: No module named 'numpy' entonces instalar la librería numpy ejecutando el comando: 
        pip install numpy
    ModuleNotFoundError: No module named 'mathplotlib' entonces instalar la librería mathplotlib ejecutando el comando:
        pip install mathplotlib
'"""
import random, numpy, math, copy, matplotlib.pyplot as plt

ciudades = [random.sample(range(100), 2) for x in range(15)];
tramo = random.sample(range(15),15);

for temperature in numpy.logspace(0,5,num=100000)[::-1]:
	[i,j] = sorted(random.sample(range(15),2));
	nuevoTramo =  tramo[:i] + tramo[j:j+1] +  tramo[i+1:j] + tramo[i:i+1] + tramo[j+1:];
	if math.exp( ( sum([ math.sqrt(sum([(ciudades[tramo[(k+1) % 15]][d] - ciudades[tramo[k % 15]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]]) - sum([ math.sqrt(sum([(ciudades[nuevoTramo[(k+1) % 15]][d] - ciudades[nuevoTramo[k % 15]][d])**2 for d in [0,1] ])) for k in [j,j-1,i,i-1]])) / temperature) > random.random():
		tramo = copy.copy(nuevoTramo);
plt.plot([ciudades[tramo[i % 15]][0] for i in range(16)], [ciudades[tramo[i % 15]][1] for i in range(16)], 'xb-');

plt.show()