"""Escribir un programa que muestre el eco de todo lo que el
usuario introduzca hasta que el usuario escriba “salir” que
terminará."""

eco = input("Ingrese algún texto: ")

while eco.lower() != "salir":
    print(eco) 
    eco = input("Ingrese algún texto: ")