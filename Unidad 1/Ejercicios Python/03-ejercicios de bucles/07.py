"""Escribir un programa que muestre por pantalla los
resultados de las tablas de multiplicar del 1 al 10."""

for i in range(10):
    for j in range(10):
        print(str(i + 1) +" * " +str(j + 1) +" = " +str((i + 1) * (j + 1)))