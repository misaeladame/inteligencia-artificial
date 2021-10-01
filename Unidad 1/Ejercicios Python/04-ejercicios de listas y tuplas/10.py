"""Escribir un programa que pregunte por una muestra de números,
separados por comas, los guarde en una tupla y muestre por pantalla
su media y desviación típica."""

muestra = input("Introduce una muestra de números separados por comas: ")
# La cadena introducida se convierte a lista
muestra = muestra.split(',')
n = len(muestra)
# La lista de caracteres se convierte a lista de enteros
for i in range(n):
    muestra[i] = int(muestra[i])
muestra = tuple(muestra)

suma = 0
suma_al_cuadrado = 0
# Se calcula la suma de los elementos y la suma de sus cuadrados
for i in muestra:
    suma += i
    suma_al_cuadrado += i**2
# Se calcula la media
media = suma/n
# Se calcula la desviación estandar
desviacion_estandar = (suma_al_cuadrado/n-media**2)**(1/2)
print('La media es', media, ', y la desviación típica es', desviacion_estandar)