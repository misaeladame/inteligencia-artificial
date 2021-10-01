"""Escribir un programa que pregunte al usuario los números ganadores de la
lotería, los almacene en una lista y los muestre por pantalla ordenados de
menor a mayor."""

eco = ""
numeros_ganadores = []

while eco.lower() != "no":
    n = int(input("Ingrese un número ganador de loteria: "))
    numeros_ganadores.append(n)

    eco = input("¿Desea almacenar más numeros (Escriba no cuando ya no quiera)? ")

numeros_ganadores.sort()
print(numeros_ganadores)