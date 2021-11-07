"""
Tarea 2.7 El problema de la mochila (knapsack problem).

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
Programar en Python o Swi-Prolog (a su elección) el algoritmo de búsqueda Hill Climbing
(escalado en la colina) y el algoritmo Beam Search (búsqueda en haz), para dar solución al
problema de la Mochila, como se describe en los apuntes (Busqueda local).

Noten que se deben programar los dos algoritmos (preferentemente como funciones (python)
o Hechos-reglas (prolog) dentro de un solo programa fuente, y poder decidir qué algoritmo
utilizar.

El planteamiento de este problema es simple, disponemos de un contenedor de una
capacidad limitada (habitualmente el peso, pero puede ser cualquier medida de capacidad) y
debemos llenarlo eligiendo de entre conjunto limitado de objetos que ocupan un espacio
específico en el contenedor y llevan un valor asociado. El objetivo es llenar el contenedor
con un subconjunto de los objetos de manera que no se sobrepase su capacidad, y que estos
objetos sumen el mayor valor posible (ver apuntes).
"""
#coding: utf-8
 
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
 
    def __str__(self):
        return "Value: %d - Weight: %d" % (self.value, self.weight)
    
    def __repr__(self):
        return self.__str__()
 
items = [Item(4, 12),
         Item(2, 2),
         Item(2, 1),
         Item(1, 1),
         Item(10, 4),
        ]
c = 0
def ks(index, weight):
    global items
    global c
    c += 1
 
    if index >= len(items):
        return 0
 
    item = items[index]
 
    if item.weight > weight:
        return ks(index + 1, weight)
    else:
        return max(ks(index + 1, weight),
                   ks(index + 1, weight - item.weight) + item.value)
 
print("Max sum: %d" % (ks(0, 20),))
print("Iterations %d" % (c,))
print()
 
c = 0
mem = {}
def ks(index, weight):
    global items
    global c
    global mem
    c += 1
 
    case = (index, weight)
    if case in mem:
        return mem[case]
 
 
    if index >= len(items):
        mem[case] = 0
        return mem[case]
 
    item = items[index]
    grab_case = (index + 1, weight - item.weight)
    no_grab_case = (index + 1, weight)
 
    if item.weight > weight:
        mem[case] = ks(*no_grab_case)
        return mem[case]
    else:
        if no_grab_case not in mem:
            mem[no_grab_case] = ks(index + 1, weight)
        if grab_case not in mem:
            mem[grab_case] = ks(index + 1, weight - item.weight) + item.value
        mem[case] = max(mem[grab_case], mem[no_grab_case])
        return mem[case]
 
print ("Max sum: %d" % (ks(0, 20),))
print ("Iterations %d" % (c,))
print ()
 
def ks(items, weight):
    mem = [[0 for j in range(weight + 1)]
           for i in range(len(items) + 1)]
    
    grab = [[0 for j in range(weight + 1)]
           for i in range(len(items) + 1)]
    
    
    for i, item in enumerate(items, start=1):
        for j in range(1, weight + 1):
            if item.weight <= j:
                if item.value + mem[i][j - item.weight] >= mem[i - 1][j]:
                    mem[i][j] = item.value + mem[i][j - item.weight]
                    grab[i][j] = 1
                else:
                    mem[i][j] = mem[i - 1][j]
            else:
                mem[i][j] = mem[i - 1][j]
                
    itemList = []
    n = len(items)
    while n > 0 and weight >= 0:
        if grab[n][weight]:
            itemList.append(items[n-1])
            weight -= items[n-1].weight
        n -= 1
    return itemList
                
print (ks(items, 15))