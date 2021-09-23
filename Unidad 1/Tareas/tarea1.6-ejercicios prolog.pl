/*
  Tarea 1.6 ejercicios prolog

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


1. Defina los hechos en prolog para representar lo siguiente:

- Juan tiene 28 años.
- María tiene 14 años.
- Sara tiene 25 años.
- Manuel tiene 20 años.
- Yolanda tiene 16 años.

*/

persona_edad(juan,28).
persona_edad(maria,14).
persona_edad(sara,25).
persona_edad(manuel,20).
persona_edad(yolanda,16).

gusta(juan,almendras).

esPadre(juan,pedro).
esPadre(pedro, maria).
esPadre(jose, luis).

/*
 Defina una regla para que liste las personas mayores de 15 años.
*/

es_mayor(X) :- persona_edad(X, Y), Y > 15.

/*
 Modifique la regla para que la edad sea una variable.
*/

es_mayor_var(X, Y) :- persona_edad(X, Z), Z > Y.

/*
   Defina las metas para contestar las siguientes preguntas:
   - ¿Hay alguien llamado Yolanda?
 */
 
 llamado_yolanda() :- persona_edad(X, Y), X == yolanda, Y > 0.
 
 /*
   - ¿Hay alguien mayor de 20 años?
 */
 
 mayor_que_20(X):- persona_edad(X, Y), Y > 20.

/*
   - ¿Quiénes tienen menos de 20 años
*/
 
 menores_que_20(X):- persona_edad(X, Y), Y < 20.
 
/*
2. Suponiendo que el predicado gusta(X,Y) indica que a X le gusta Y, escriba los
objetivos que habrá que definir en Prolog para contestar las siguientes preguntas:

- ¿Le gusta algo a Juan?
*/
 
 le_gusta_algo_juan(juan,_) :- gusta(juan,_).

 /*
 - ¿Le gustan a Juan las almendras?
 */

 gusta(juan, almendras).

/*
   - ¿Qué es lo que le gusta a Juan?
*/

gusta(juan, X).

/*

A continuación, suponiendo que esPadre(X,Y) indica que X es el padre de Y, exprese en
lenguaje natural lo que significan las preguntas:
?- esPadre(X,pedro).
¿Quien es padre de pedro?


?- esPadre(_,pedro).
?- esPadre(X,_).
?- esPadre(_,_).
?- esPadre(_,X).
?- esPadre(X,Y).

?- esPadre(personaQueNoExiste,pedro).

*/

 /*
 
3.- Represente en Prolog, los siguientes hechos:
- Pedro quiere a María.
- Pedro quiere a Belén.
- Manuel quiere a Belén.
- María quiere a Pedro.
- Todos quieren a Juan y a María.
- Todo el mundo se quiere a sí mismo.
- Alguien quiere a Juan y a Pedro.
- Alguien quiere a María.
- Alguien quiere a todos los demás.
 
 */
 
quiere_a(pedro,maria).
quiere_a(pedro,belen).
quiere_a(manuel,belen).
quiere_a(maria,pedro).
quiere_a(_,juan). quiere_a(_,maria).
quiere_a(_,X).
quiere_a(X,juan). quiere_a(X,pedro).
quiere_a(X,maria).
quiere_a(X,_).
 
 /*
 
4.- A continuación, escriba los objetivos en Prolog necesarios para responder a las
preguntas indicadas a continuación:
- ¿Quiere Manuel a María?
- ¿Quiere Manuel a María y a Pedro?
- ¿Quiere Manuel a alguien?
- ¿Quiénes son los que quieren a María?
- ¿Quiénes son los que quieren a Pedro?
- ¿Quiénes son los que se quieren mutuamente?
- ¿Quiénes son los que se quieren a sí mismos?
- ¿Se quiere Manuel a sí mismo?
- ¿Hay alguien que quiera a María?
- ¿Hay alguien que quiera a alguien?
- ¿Hay alguien que quiera a todo el mundo?
 
*/

quieree_a(manuel,maria).
quieree_a(manuel,maria). quieree_a(manuel,pedro).
quieree_a(manuel,Y).
quieree_a(X,maria).
quieree_a(X,pedro).
quieree_a(manuel,manuel) | quieree_a(maria,maria).
quieree_a(manuel,manuel).
quieree_a(X,maria).
quieree_a(X,Y).
quieree_a(X,_).

/*

5. Defina la relación máximo(Lista_enteros) para calcular el mayor elemento de una lista
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

6. Defina la relación cuenta(Elemento, Lista, Cantidad) que cuente el número de veces que
un elemento se encuentra en una lista.

*/

cuenta(_,0,[]).
cuenta(N,L,[N|XS]):-L>0,NL is L-1,cuenta(N,NL,XS).
cuenta(N,L):-cuenta(N,N,L).
listar([],[]).
listar([X|XS],NL):-cuenta(X,L),listar(XS,NX),append(L,NX,NL).


/*

7. Defina la relación elimina(Elemento, Lista_ori, Lista_res) para que elimine un elemento
de una lista. El resultado se guardará en otra lista nueva. Por ejemplo, el resultado de
borrar el valor a de la lista [b,a,g,a,h,b], sería la nueva lista formada por [b,g,h,b].

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

agregar_ordenada([A | LA], B, [A,LC]):- agregar_ordenada(LA, B, LC).

