"""Escribir un programa que pregunte al usuario por el número de 
horas trabajadas y el costo por hora. Después debe mostrar por
pantalla la paga que le corresponde"""

horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = round(horas * coste, 3)
print("Tu paga es " +str(paga))