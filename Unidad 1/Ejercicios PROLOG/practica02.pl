/* Práctica 2. Estructura y componentes de los programas para IA en el lenguaje seleccionado.
José Misael Adame Sandoval 
En este Programa definiremos las funciones (relaciones) para dar solución a los reactivos de la Práctica 2.
*/

/*1.- Elabore un programa para determinar el mayor de dos números o indicar que son iguales si es el
caso. Teclee y pruebe los programas en lso respectivos entornos.
Nota: Prolog y Python tienen una funcion max() incorporada, pero hacerla nosotros mismos es buen 
ejercicio ilustrativo. */

max2(X,Y,Z) :- (X =< Y -> Z = Y ; Z = X).

/* 2.- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de
ellos. */

max3(N1,N2,N3,Mayor) :- max2(N1,N2,M1), max2(M1, N3, Mayor).