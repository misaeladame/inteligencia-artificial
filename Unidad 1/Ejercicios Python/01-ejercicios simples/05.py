"""Escribir un programa que pregunte el nombre del usuario en 
la consola y después de que el usuario lo introduzca muestre
por pantalla el nombre en mayúsculas y el número de
caracteres que contiene en líneas distintas."""

name = input("¿Cómo te llamas? ")
print(name.upper() + " tiene " + str(len(name)) + " letras")