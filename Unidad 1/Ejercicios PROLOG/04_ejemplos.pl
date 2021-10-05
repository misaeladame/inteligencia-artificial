% Ejemplo de Hecho
edad(juan, 27).

% Ejemplo de regla
mayor_de_edad(X) :- edad(X, E), E > 18.