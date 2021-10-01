"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si
es un palíndromo."""

palabra_lista = []
palabra_lista_contrario = []

palabra = input("Introduzca una palabra: ")

for letra in palabra:
    palabra_lista.append(letra)
    palabra_lista_contrario.insert(0, letra)

if palabra_lista == palabra_lista_contrario:
    print("La palabra " +palabra +" SI es un palíndromo")
else:
    print("La palabra " +palabra +" NO es un palíndromo")


