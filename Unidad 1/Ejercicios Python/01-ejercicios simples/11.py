"""Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión"""

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años? "))
print("Capital final: " +str(round(amount * (interest / 100 + 1) ** years, 2)))