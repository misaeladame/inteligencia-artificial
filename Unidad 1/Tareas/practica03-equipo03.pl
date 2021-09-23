/*
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
*/


/*
Elabore el programa en Prolog y en Python para los siguientes ejercicios:
1. Defina la relación imprime_lista(L) que imprima el contenido de la lista L, por ejemplo:
?- imprime_lista([5,2,8,9,22]).
5 2 8 9 22
Yes.
*/

imprime_lista([]).
imprime_lista([H|T]) :- write(H), write(" "), imprime_lista(T).

/*
2. Definir la relación leer_lista(L) para leer los elentos de una lista.
*/

leer_lista([]).
leer_lista([_|_]).

/*    
3. Definir la relación miembro(X, L) la cual verifique si el primer argumento (X) pertenece a la
lista L. Por ejemplo:
?-miembro(2,[5,6,2,7,89,0]).
Yes.
*/

miembro(X,[X|_]).
miembro(X,[_|L]) :- miembro(X,L).

/*
4. Definir suma_lista(L, X) que efectúe en X la suma de los elementos de la lisa de números L.
Por ejemplo:
?- suma_lista([7, 5, 9 ], X).
X = 21
*/

suma_lista([], 0).
suma_lista([X|L], N) :- suma_lista(L, M), N is M + X.

/*
5. Definir append(L1, L2, L3) donde L3 es el resultado de añair la lista L1 al principio de la lista
L2, por ejemplo:
?- append([1,2,3],[4,5,6,7],L).
L = [1,2,3,4,5,6,7]
*/

append([], L, L).
append([X|L], M, [X|N]) :- append(L, M, N).

/*
6. Definir burbuja(L, O) donde la lista numérica L puede estar desordenada y por medio del
algoritmo de ordenaciónde burbuja se ordena de forma ascendente, por ejemplo:
?- burbuja([1,2,3,7,6,5,4,3,2,1],L)
L = [1,1,2,2,3,3,4,5,6,7]
*/

burbuja([], []).
burbuja([X], [X]).
burbuja([X|L], M) :- burbuja(L, N), [Y|O] = N, ((X =< Y, M = [X|N]) ; (X > Y,  burbuja([Y,X|O], M))).
