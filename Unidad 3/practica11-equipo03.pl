/*
Practica 11 - Lógica y reglas de producción.

Objetivo: El alumno comprenderá cómo representar y codificar el conocimiento con reglas de producción.
Se corresponde con el Tema 3 “Representación del conocimiento y razonamiento.” del programa de la 
materia.

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
Ejercicio 1- Implemente el siguiente problema en prolog.
Dado un conjunto de personas, hombres y mujeres, que tienen ciertos hobbies, se trata de
establecer cuáles pueden conformar una pareja ideal, suponiendo que para ello deben
compartir al menos uno de los hobbies declarados. 

En primer lugar, se definen como axiomas al grupo de personas, donde cada una está
representada por un nombre, su género y una lista de hobbies. A continuación, se codifica la
regla de inferencia: Se puede decir que es una pareja ideal si existe un hombre y una mujer que
comparten al menos uno de sus hobbies (interés común). Para determinar si el hombre y la
mujer tienen algún interés común, se analiza el contenido de las dos listas de hobbies,
buscando alguno que sea miembro tanto de la lista del hombre, como de la lista de la mujer.
Finalmente, se imprime en la salida los resultados de las parejas que se consideran ideales.
*/

% Axiomas
persona('Daniel',hombre,[viajar,libros,computadores,futbol]).
persona('Juan',hombre,[estampillas,futbol,nadar,viajar]).
persona('Anna',mujer,[vinos,libros,computadores,modas]).
persona('Georgina',mujer,[estampillas,tejer,nadar,viajar]).

% Reglas
pareja_ideal:-persona(H,hombre,Lh),persona(M,mujer,Lm),interes_comun(Lh,Lm),
write(H),write(' podria hacer pareja con '), write(M), nl,fail.
miembro(X,[X|_]).
miembro(X,[_|Cola]):-
miembro(X,Cola).
interes_comun(L1,L2):-
miembro(I, L1),
miembro(I, L2), !.

/*
Si al consultar no da mensajes de error, se pueden plantear preguntas al intérprete y el sistema
contestará, según corresponda:
*/

% Pregunta: ¿Cuáles personas pueden ser una pareja ideal?
% ?- pareja_ideal.

% Pregunta: ¿Cuáles son las personas y sus datos registrados?
% ?- persona(N,G,H).

%Pregunta: ¿Hay mujeres registradas en el sistema?
% ?- persona(_,'mujer',_).

%Pregunta: ¿Nombres de los hombres registrados en el sistema?
% ?- persona(N,'hombre',_).