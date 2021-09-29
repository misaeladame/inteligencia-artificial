"""Escribir un programa que pregunte al usuario una cantidad
a invertir, el interés anual y el número de años, y muestre
por pantalla el capital obtenido en la inversión cada año
que dura la inversión."""

inversion = float(input("Ingresa la cantidad a invertir: "))
interes_anual = float(input("Ingresa el interés anual: "))
anios = int(input("Introduce los años: "))

interes_anual *= 0.01 

for i in range(anios):
    inversion = inversion + ( inversion * interes_anual )
    print("El capital obtenido en el año " +str(i+1) + " es de " +str(round(inversion, 2))) 