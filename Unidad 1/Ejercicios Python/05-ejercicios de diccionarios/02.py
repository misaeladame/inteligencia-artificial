"""Escribir un programa que pregunte al usuario su nombre,
edad, dirección y teléfono y lo guarde en un diccionario.
Despúes debe mostrar por pantalla el mensaje <nombre>
tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>."""

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
direccion = input("Ingresa tu dirección: ")
telefono = input("Ingresa tu telefono: ")

diccionario = {"Nombre" : nombre, "Edad" : edad, "Direccion" : direccion, "Telefono" : telefono}

print(diccionario["Nombre"], "tiene", diccionario["Edad"], "años, vive en", 
diccionario["Direccion"], "y su número de teléfono es", diccionario["Telefono"])