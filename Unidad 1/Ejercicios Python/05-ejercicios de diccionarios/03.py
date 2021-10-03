"""Escribir un programa que guarde en un diccionario los precios de las
frutas de la tabla, pregunte al usuario por una fruta, un número de kilos
y muestre por pantalla el precio de ese número de kilos de fruta. Si la
fruta no está en el diccionario debe mostrar un mensaje informando de
ello."""

precios_frutas = {"platano" : 1.35, "manzana" : 0.80, "pera" : 0.85, "naranja" : 0.70 }

try:
    fruta = input("¿Qué fruta desea? ")
    kilos = int(input("Ingrese los kilos de esa fruta: "))

    precio_total = precios_frutas[fruta.lower()] * kilos

    print("El precio total de " +str(kilos) +" kilos de " +fruta +" es de " +str(round(precio_total,2)))
except KeyError:
    print("AVISO: Esa fruta no está disponible")