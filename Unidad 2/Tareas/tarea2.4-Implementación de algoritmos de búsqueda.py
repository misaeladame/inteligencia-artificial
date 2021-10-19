"""
Tarea 2.4 Implementación de algoritmos de búsqueda

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
1. Modifique los programas vistos en clase para implementar en python la Búsqueda en
Profundidad Limitada para el siguiente grafo, compruebe su funcionamiento con diferentes
metas.

                  1
               /  |  \
              2   3   4
             / \     / \
            5   6   7   8
           / \     / \  |
          9  10   11 12 13

Cada elemento de este diccionario contiene una posicion y como valor tiene
el nombre de su elemento padre en el arbol

"""
print("1. Búsqueda en Profundidad Limitada")

valores={
    2:1,
    3:1,
    4:1,
    5:2,
    6:2,
    7:4,
    8:4,
    9:5,
    10:5,
    11:7,
    12:7,
    13:8
}
 
# variable que contiene el camino recorrido hasta llegar al estado a buscar
camino=[]
 
def buscar(inicio,valorBuscar):
    """
    Funcion recursiva para buscar en profundidad
    Tiene que recibir:
        - el valor inicial donde empezar a buscar
        - el valor a buscar en su estructura
    Devuelve el valor a buscar o 0 si no lo encuentra
    """
    camino.append(inicio)
 
    # si encontramos el elemento, lo devolvemos
    if inicio==valorBuscar:
        return valorBuscar
 
    # recorremos todos los elementos en busca del valor de inicio
    for k,v in valores.items():
 
        # si el valor del elemento tiene como padre al valor de inicio
        if v==inicio:
 
            # llamamos a la función recursivamente enviando el nuevo padre
            result=buscar(k,valorBuscar)
 
            # si hemos recibido algun resultado es que hemos encontrado el
            # elemento que buscamos
            if result:
                return result
 
    camino.pop()
 
    # si llegamos aqui, es que hemos llegado al final de una profundidad
    return 0

def mostrarResultado(inicio, fin):
    
    result=buscar(inicio,fin)
    if result:
        print("El camino que ha realizado ha sido: {}".format(camino))
    else:
        print("No encontrado")
    camino.clear()
    
mostrarResultado(1,10)
mostrarResultado(1,13)
mostrarResultado(1,12)
mostrarResultado(5,13)
mostrarResultado(4,12)
mostrarResultado(2,9)


"""
-----------------------------------------------------------------------------------------------------
2. Implemente en python la búsqueda en profundidad Iterativa para el siguiente grafo,
compruebe su funcionamiento con diferentes metas.

                  1
               /  |  \
              2   3   4
             / \     / \
            5   6   7   8
           / \     / \  |
          9  10   11 12 13
"""
print("\n\n2. Búsqueda en profundidad Iterativa")

graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12'],
        '8': ['13']
        }



def bfs(graph, est_inicio, est_final):
    
    est_abiertos = []
    est_cerrados = []
    hijos = []
    
    est_abiertos.append(est_inicio)
    est_actual = est_abiertos[-1]
    
    while(est_actual != est_final and est_abiertos):
        
        est_actual = est_abiertos.pop()
        est_cerrados.append(est_actual)
        hijos = graph.get(est_actual, [])
        
        for hijo in hijos:
            if hijo not in est_cerrados and hijo not in est_abiertos:
                est_abiertos.insert(0, hijo)
        
    if est_actual == est_final:
        return est_cerrados
    else:
        return "No hay solucion"
        
print(bfs(graph, '1', '10'))
print(bfs(graph, '4', '12'))
print(bfs(graph, '8', '9'))
print(bfs(graph, '2', '10')) 
print(bfs(graph, '1', '13')) 
            