/* Hechos */
padrede(juan, maria).     % juan es padre de maria (juan y maria son átomos).
padrede(pablo, juan).     % pablo es padre de juan
padrede(pablo, marcela).  % pablo es padre de marcela
padrede(carlos, debora).  % carlos es padre de debora

% Reglas con variables
% A es hijo de B si B es padre A
hijode(A, B) :- padrede(B, A).

% A es abuelo de B si A es padre de C y C es padre B
abuelode(A, B) :-
    padrede(A, C),
    padrede(C, B).

% A y B son hermanos si el padre de A es también el padre de B y si A y B no son lo mismo.
hermanode(A, B) :-
    padrede(C, A),
    padrede(C, B),
    A \== B.

% consultas
% juan es hermano de marcela?
/*
?- hermanode('juan', 'marcela').
Yes
*/

% carlos es hermano de juan?
/*
?- hermanode('carlos', 'juan').
no
*/

% pablo es abuelo de maria?
/*
?- abuelode('pablo', 'maria').
yes
*/