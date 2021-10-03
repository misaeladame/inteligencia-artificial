"""Escribir una función que calcule el área de un círculo y otra que calcule el
volumen de un cilindro usando la primera función."""

import math

def area_circulo(radio):
    return math.pi * math.pow(radio, 2)
     
def volumen_cilindro(altura, radio):
    return area_circulo(radio) * altura

radio = float(input("Ingrese el radio: "))
altura = float(input("Ingrese la altura: "))

print("El área del círculo es = " +str(round(area_circulo(radio), 4)))
print("El área del cilindro es = " +str(round(volumen_cilindro(altura, radio), 4)))