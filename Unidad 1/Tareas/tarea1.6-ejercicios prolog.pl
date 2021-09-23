/*
  Tarea 1.6 ejercicios prolog

  Equipo: 3
  
  Nombre: Cristian Gabriel Pi�a Rosales
  N�mero de control: 18130588
  
  Nombre: Jos� Misael Adame Sandoval
  N�mero de control: 18131209

  Nombre: Jose Luis Flores Ramos
  N�mero de control: 18131237
  
  Nombre: Ricardo Ra�l Castro Luna
  N�mero de control: 18131227
  
  Nombre: Kevin Alejandro Ruiz Mart�nez
  N�mero de control: 18131280


1. Defina los hechos en prolog para representar lo siguiente:

- Juan tiene 28 a�os.
- Mar�a tiene 14 a�os.
- Sara tiene 25 a�os.
- Manuel tiene 20 a�os.
- Yolanda tiene 16 a�os.

*/

persona_edad(juan,28).
persona_edad(maria,14).
persona_edad(sara,25).
persona_edad(manuel,20).
persona_edad(yolanda,16).

gusta(juan,almendras).

esPadre(juan,pedro)
esPadre(pedro, maria)
esPadre(jose, luis)

/*
 Defina una regla para que liste las personas mayores de 15 a�os.
*/

es_mayor(X) :- persona_edad(X, Y), Y > 15.

/*
 Modifique la regla para que la edad sea una variable.
*/

es_mayor_var(X, Y) :- persona_edad(X, Z), Z > Y.

/*
   Defina las metas para contestar las siguientes preguntas:
   - �Hay alguien llamado Yolanda?
 */
 
 llamado_yolanda() :- persona_edad(X, Y), X == yolanda, Y > 0.
 
 /*
   - �Hay alguien mayor de 20 a�os?
 */
 
 mayor_que_20(X):- persona_edad(X, Y), Y > 20.

/*
   - �Qui�nes tienen menos de 20 a�os
*/
 
 menores_que_20(X):- persona_edad(X, Y), Y < 20.
 
 /*

2. Suponiendo que el predicado gusta(X,Y) indica que a X le gusta Y, escriba los
objetivos que habr�a que definir en Prolog para contestar las siguientes preguntas:

- �Le gusta algo a Juan?
 */
 
 le_gusta_algo_juan(juan,_) :- gusta(juan,_).

 /*
 - �Le gustan a Juan las almendras?
 */

 gusta(juan, almendras).

/*
   - �Qu� es lo que le gusta a Juan?
*/

gusta(juan, X).

/*

A continuaci�n, suponiendo que esPadre(X,Y) indica que X es el padre de Y, exprese en
lenguaje natural lo que significan las preguntas:
?- esPadre(X,pedro).
�Quien es padre de pedro?


?- esPadre(_,pedro).
?- esPadre(X,_).
?- esPadre(_,_).
?- esPadre(_,X).
?- esPadre(X,Y).

?- esPadre(personaQueNoExiste,pedro).

*/

 /*
 
3.- Represente en Prolog, los siguientes hechos:
- Pedro quiere a Mar�a.
- Pedro quiere a Bel�n.
- Manuel quiere a Bel�n.
- Mar�a quiere a Pedro.
- Todos quieren a Juan y a Mar�a.
- Todo el mundo se quiere a s� mismo.
- Alguien quiere a Juan y a Pedro.
- Alguien quiere a Mar�a.
- Alguien quiere a todos los dem�s.
 
 */
 
 
 /*
 
4.- A continuaci�n, escriba los objetivos en Prolog necesarios para responder a las
preguntas indicadas a continuaci�n:
- �Quiere Manuel a Mar�a?
- �Quiere Manuel a Mar�a y a Pedro?
- �Quiere Manuel a alguien?
- �Qui�nes son los que quieren a Mar�a?
- �Qui�nes son los que quieren a Pedro?
- �Qui�nes son los que se quieren mutuamente?
- �Qui�nes son los que se quieren a s� mismos?
- �Se quiere Manuel a s� mismo?
- �Hay alguien que quiera a Mar�a?
- �Hay alguien que quiera a alguien?
- �Hay alguien que quiera a todo el mundo?
 
 */

/*

5. Defina la relaci�n m�ximo(Lista_enteros) para calcular el mayor elemento de una lista
de enteros.

*/

maximo(M, [X|Xs]):-
          maximo2(M, X, Xs).

maximo2(M, M, []):- !.

maximo2(X, Y, [Z|Zs]):-
          Z >= Y,
          !,
          maximo2(X, Z, Zs).

maximo2(X, Y, [Z|Zs]):-
          Z =< Y,
          maximo2(X, Y, Zs).
          
/*

6. Defina la relaci�n cuenta(Elemento, Lista, Cantidad) que cuente el n�mero de veces que
un elemento se encuentra en una lista.

*/

cuenta(_,0,[]).
cuenta(N,L,[N|XS]):-L>0,NL is L-1,cuenta(N,NL,XS).
cuenta(N,L):-cuenta(N,N,L).
listar([],[]).
listar([X|XS],NL):-cuenta(X,L),listar(XS,NX),append(L,NX,NL).


/*

7. Defina la relaci�n elimina(Elemento, Lista_ori, Lista_res) para que elimine un elemento
de una lista. El resultado se guardar� en otra lista nueva. Por ejemplo, el resultado de
borrar el valor a de la lista [b,a,g,a,h,b], ser�a la nueva lista formada por [b,g,h,b].

*/

elimina(_, [], []).

elimina(Y, [Y|Xs], Zs):-
          elimina(Y, Xs, Zs), !.

elimina(X, [Y|Xs], [Y|Zs]):-
          elimina(X, Xs, Zs).
          
/*

8. Escriba la(s) regla(s) necesaria(s) para agregar un elemento al principio de una lista.
?- agregar(gato,[zorro, zopilote, puerco],L), write(L), nl.
L = [gato, zorro, zopilote, puerco]
yes.

*/

agregar(E,L,[E|L]).
agregar(E,[X|Y],[X|Z]):-agregar(E,Y,Z).

/*

9. Escriba la(s) regla(s) necesaria(s) para agregar un elemento al final de una lista.
?- agregar_final([agua, tierra, viento], fuego, L), write(L), nl.
L = [agua, tierra, viento, fuego]
yes.

*/

agregar_final([],X,[X|[]]).
agregar_final([H1|T1],x,[H1|T]):-agregar_final(T1,X,T).

/*

10. Escriba la(s) regla(s) necesaria(s) para agregar un elemento en su lugar correspondiente
en una lista ordenada.
?- agregar_ordenada(7,[0,2,5,6,9,10,],L), write(L), nl.
L = [0,2,5,6,7,9,10]
yes.

*/

