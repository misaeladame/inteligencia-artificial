"""
Practica 6 - Búsqueda en profundidad limitada y profundidad iterativa.

Objetivo: Comprender la resolución de problemas mediante la búsqueda en profundidad. Se corresponde
con el Tema 2 “Técnicas de búsqueda” del programa de la materia.

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
Ejercicio 1. Elabore dos funciones en python para implementar la búsqueda en
profindidad limitada y la búsqueda en profundidad iterativa.


Este grafo tiene como nodo inicial el 1 y como nodo final el 8, todos los caminos son dirigidos y
tienen el mismo coste. Utilizaremos los algoritmos de búsqueda ciega para encontrar un camino
entre estos dos nodos.

Supondremos que hacemos un tratamiento de los nodos repetidos durante la ejecución del
algoritmo. Hay que tener en cuenta también que para poder recuperar el camino, los nodos
deben tener un enlace al padre que los ha generado.

Compruebe su funcionamiento con diferentes metas.
"""

class Node(object):
    def __init__(self, label: str=None):
        self.label = label
        self.children = []
        
    def __lt__(self,other):
        return (self.label < other.label)
    
    def __gt__(self,other):
        return (self.label > other.label)
    
    def __repr__(self):
        return '{} -> {}'.format(self.label, self.children)
    
    def add_child(self, node, cost=1):
        if type(node) is list:
            [self.add_child(sub_node) for sub_node in node]
            return
        edge = Edge(self, node, cost)
        self.children.append(edge)
    
    
class Edge(object):
    
    def __init__(self, source: Node, destination: Node, cost: int=1, bidirectional: bool=False):
        self.source = source
        self.destination = destination
        self.cost = cost
        self.bidirectional = bidirectional
    
    def __repr__(self):
        return '{}: {}'.format(self.cost, self.destination.label)

def iddfs(root: Node, goal: str, maximum_depth: int=10):
    for depth in range(0, maximum_depth):
        result = _dls([root], goal, depth)
        if result is None:
            continue
        return result
    
    raise ValueError('goal not in graph with depth {}'.format(maximum_depth))

def _dls(path: list, goal: str, depth: int):
    current = path[-1]
    if current.label == goal:
        return path
    if depth <= 0:
        return None
    for edge in current.children:
        new_path = list(path)
        new_path.append(edge.destination)
        result = _dls(new_path, goal, depth - 1)
        if result is not None:
            return result
    
N1 = Node('1')
N2 = Node('2')
N3 = Node('3')
N4 = Node('4')
N5 = Node('5')
N6 = Node('6')
N7 = Node('7')
N8 = Node('8')


N1.add_child([N2, N3])
N2.add_child([N4, N6])
N3.add_child([N4, N5, N7])
N4.add_child(N5)
N5.add_child([N6, N7])
N6.add_child([N7, N8])
N7.add_child(N8)

print(iddfs(N1, '8'))