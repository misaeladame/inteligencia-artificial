"""
Practica 5 - Búsqueda en anchura y búsqueda en profundidad.

Objetivo: Comprender la resolución de problemas mediante búsqueda ciega. Se corresponde con el
Tema 2 “Técnicas de búsqueda” del programa de la materia.

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
Nodos de búsqueda.
Según lo visto en clase, la generación de los aŕboles de búsqueda en espacios de estado se
hace a través de lo que llamamos nodo de búsqueda.

Ejercicio 1. Elabore dos funciones en python para implementar la búsqueda en anchura
(bfs) y la búsqueda en profundidad (dfs) para el siguiente grafo.


Este grafo tiene como nodo inicial el 1 y como nodo final el 8, todos los caminos son dirigidos y
tienen el mismo coste. Utilizaremos los algoritmos de búsqueda ciega para encontrar un camino
entre estos dos nodos.

Supondremos que hacemos un tratamiento de los nodos repetidos durante la ejecución del
algoritmo. Hay que tener en cuenta también que para poder recuperar el camino, los nodos
deben tener un enlace al padre que los ha generado.

Compruebe su funcionamiento con diferentes metas.
"""

#nodos
graph ={'1':['2','3'],
        '2':['4','6'],
        '4':['5'],
        '6':['7','8'],
        '3':['4','5','7'],
        '5':['6','7'],
        '7':['8']}


#funcion busqueda en anchura bfs
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

#funcion busqueda en profundidad dfs
print("Funcion bfs:" )
print(bfs(graph, '1', '8'))

def dfs(graph, Estado_inicial, Estado_final):
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
        hijos.reverse()
        for hijo in hijos:
            # tratar repetidos
            if hijo not in Est_cerrados and hijo not in Est_abiertos:
                 Est_abiertos.append(hijo)     
    # hay solucion?
    if Actual == Estado_final:
        return Est_cerrados
    else:
        return "No hay solucion"

print("\nFuncion dfs:" )
print(dfs(graph, '1', '8'))

