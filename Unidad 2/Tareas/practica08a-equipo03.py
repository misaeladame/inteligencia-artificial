"""
Practica 8a - Búsqueda local, Algoritmos Genéticos.

Objetivo: Comprender la resolución de problemas mediante técnicas de búsqueda local, búsqueda 
con algoritmos genéticos. Se corresponde con el Tema 2 “Técnicas de búsqueda” del programa de 
la materia.

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
El problema de las N reinas.

El problema de las N reinas consiste en situar N reinas en un tablero de ajedrez de NxN sin que se
amenacen entre ellas. Una reina amenaza a otra si está en la misma fila, columna o diagonal.

Elabore un programa en python que dé solución a este problema con el uso de algoritmos genéticos.
"""

"""
NOTA: En caso de un error(es) como los siguiente(s):
    ModuleNotFoundError: No module named 'numpy' entonces instalar la librería numpy ejecutando el comando: 
        pip install numpy
    ModuleNotFoundError: No module named 'mathplotlib' entonces instalar la librería mathplotlib ejecutando el comando:
        pip install mathplotlib
    ModuleNotFoundError: No module named 'deap' entonces instalar el framework deap ejecutando el comando:
        pip install deap
'"""

import random
import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

import matplotlib.pyplot as plt

#Parámetros del problema 
NB_QUEENS = 50

# FUNCIÓN DE FITNESS
def evalNQueens(individual):
    size = len(individual)

    # Ataques sólo diagonales
    diagonal_izquierda_derecha = [0] * (2*size-1)
    diagonal_derecha_izquierda = [0] * (2*size-1)
    
    # Reinas en cada diagonal
    for i in range(size):
        diagonal_izquierda_derecha[i+individual[i]] += 1 # [columna + fila]
        diagonal_derecha_izquierda[size-1-i+individual[i]] += 1
    
    suma = 0
    for i in range(2*size-1): # recorremos las diagonales
        if diagonal_izquierda_derecha[i] > 1: 
            suma += diagonal_izquierda_derecha[i] - 1 
        if diagonal_derecha_izquierda[i] > 1:
            suma += diagonal_derecha_izquierda[i] - 1
    return suma,

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

# REGISTRO DE FUNCIONES QUE SON NECESARIAS -- CAJA DE HERRAMIENTAS
toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(NB_QUEENS), NB_QUEENS)

toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalNQueens)

# Operadores genéticos
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0/NB_QUEENS)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    seed=0
    random.seed(seed)

    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1) # objeto que almacena el mejor individuo
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=True) # algoritmo genético como "caja negra"

    return pop, stats, hof

if __name__ == "__main__":
    pop, stats, best = main()
    print(best)
    print(best[0].fitness.values)
    y = best[0]
    x= range(NB_QUEENS)
    x= numpy.array(x)
    print(x)
    y = numpy.array(y)
    print(y)    
    x = x + 0.5
    y = y + 0.5
    plt.figure()
    plt.scatter(x,y)
    plt.xlim(0,NB_QUEENS)
    plt.ylim(0,NB_QUEENS)
    plt.xticks(x-0.5)
    plt.yticks(x-0.5)
    plt.grid(True)
    plt.title(u"Mejor Individuo")
plt.show()