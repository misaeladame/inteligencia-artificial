"""Escribir un programa que pida al usuario un número entero
y muestre por pantalla un triángulo rectángulo como el de
más abajo.
1
3 1
5 3 1
7 5 3 1"""

n = int(input("Introduce un numero entero: "))

for i in range(n):
    k = i + (i + 1)
    for j in range(i + 1):
        print(k, end=" ")
        k -= 2
    print()

