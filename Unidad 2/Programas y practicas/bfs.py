#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Representacion del grafo
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12'],
        '8': ['13']
        }

def bfs(graph, Estado_inicial, Estado_final):
    # creamos las estructuras necesarias para el algoritmo
    Est_abiertos = []
    Est_cerrados = []
    hijos = []
    # Se mete a los abiertos el nodo inicial
    Est_abiertos.append(Estado_inicial)
    # El nodo actual es el primero enla estructura de los abiertos
    Actual = Est_abiertos[-1]
    # Mientras no sea estado final y haya nodos abiertos
    while (Actual != Estado_final and Est_abiertos):
        # Borrar el primero en la estructura de los nodos abiertos
        Actual = Est_abiertos.pop()
        # Se inserta en los cerraos
        Est_cerrados.append(Actual)
        # obtiene los nodos hijo
        hijos = graph.get(Actual, [])
        for hijo in hijos:
            # tratar repetidos
            if hijo not in Est_cerrados and hijo not in Est_abiertos:
                 Est_abiertos.insert(0, hijo)
    # hay solucion?
    if Actual == Estado_final:
        return Est_cerrados
    else:
        return "No hay solucion"


print(bfs(graph, '1', '7'))
print(bfs(graph, '1', '11'))
print(bfs(graph, '1', '14'))