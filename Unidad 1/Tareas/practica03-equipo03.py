"""
Practica 3 - Manejo de listas

Objetivo: Que el alumno reafirme el conocimiento sobre la representación y manipulación del
conocimiento con el uso de listas. Se corresponde con el Tema 1 “Fundamentos de la
Inteligencia Artificial” del programa de la materia.

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

Elabore el programa en Python para los siguientes ejercicios:

1. Defina la relación imprime_lista(L) que imprima el contenido de la lista L, por ejemplo:
"""
print("Ejercicio 1")
L = [1, 2, 3, 4, 5];
print(L[:])

"""
2. Definir la relación leer_lista(L) para leer los elementos de una lista.
"""
print("\nEjercicio 2")
print("L[0:4]: ", L[0:4])

"""
3. Definir la relación miembro(X, L) la cual verifique si el primer argumento (X) pertenece a la
lista L. 
"""
print("\nEjercicio 3")
print(5 in L)

"""
4. Definir suma_lista(L, X) que efectúe en X la suma de los elementos de la lisa de números L.
"""
print("\nEjercicio 4")
L1 = [1,2,3];
L2 = [4,5,6];
L3 = L1+L2
print("L1+L2: ", L3[0:5])

"""
5. Definir append(L1, L2, L3) donde L3 es el resultado de añair la lista L1 al principio de la lista
L2, por ejemplo:
?- append([1,2,3],[4,5,6,7],L).
L = [1,2,3,4,5,6,7]
"""
print("\nEjercicio 5")

def appendS(L1,L2,L3):
    L3 = L1+L2
    print(L3)

appendS([1,2,3],[4,5,6,7],L3=[])

"""
6. Definir burbuja(L, O) donde la lista numérica L puede estar desordenada y por medio del 
algoritmo de ordenaciónde burbuja se ordena de forma ascendente, por ejemplo:
?- burbuja([1,2,3,7,6,5,4,3,2,1],L)
L = [1,1,2,2,3,3,4,5,6,7]
"""
print("\nEjercicio 6")

def ordenamientoBurbuja(L,O):
    for numPasada in range(len(L)-1,0,-1):
        for i in range(numPasada):
            if L[i]>L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                O= L
    pass                
    print(O)
    
L = [1,2,3,7,6,5,4,3,2,1]
ordenamientoBurbuja(L,O=[])
 