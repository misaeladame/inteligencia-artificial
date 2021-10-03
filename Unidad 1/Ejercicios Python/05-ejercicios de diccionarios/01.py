"""Escribir un programa que guarde en una variable el
diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al
usuario por una divisa y muestre su símbolo o un mensaje
de aviso si la divisa no está en el diccionario."""

diccionario = { "Euro" : "€", "Dollar" : "$", "Yen" : "¥"}


try:
    divisa = input("Ingrese una divisa: ")
    print(diccionario[divisa])
except KeyError:
    print("AVISO: Esa divisa no está en el diccionario")