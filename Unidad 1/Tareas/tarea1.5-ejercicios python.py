"""
Tarea 1.5 ejercicios python

Equipo: 3

Nombre: Piña Rosales Cristian Gabriel 
Número de Control: 18130588

Nombre: Adame Sandoval José Misael
Número de Control: 18131209

Nombre: Castro Luna Ricardo Raúl
Número de Control: 18131227

Nombre: Flores Ramos José Luis
Número de Control: 18131237

Nombre: Ruiz Martínez Kevin Alejandro
Número de Control: 18131280
"""

""" Ejercicio 1
Elabore un programa que pida un número (entero) y muestre por pantalla
a. “Es par” en caso de serlo y
b. “Es impar” en caso de ser impar."""

print("Ejercicio 1")
numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("El número " +str(numero) + " es par")
else:
    print("El número " +str(numero) + " es impar")

""" Ejercicio 2
Elabore un programa que pida un año y muestre por pantalla
a. “Es bisiesto”, en el caso de ser año bisiesto,
b. “No es bisiesto”, en el caso de que el año no sea bisiesto. Considere que son bisiestos 
   todos los años múltiplos de 4, excepto aquellos que son múltiplos de 100 pero no de 400. 
   Por ejemplo: años múltiplos de 4 son 4, 8, 20, 100, 400, 1000, 2000, 2100, 2800… De ellos, 
   años múltiplos de 100 pero no de 400 son: 100, 200, 1000, 2100 … Así que años bisiestos 
   son 4, 8, 20, 400, 2000, 2800 …"""

print("")
print("Ejercicio 2")

anio = int(input("Introduzca un año: "))

if anio % 4 == 0 and not ( anio % 100 == 0 and not anio % 400 == 0 ):
    print("El año " +str(anio) + " es bisiesto")
else:
    print("El año " +str(anio) + " no es bisiesto")

"""Ejercicio 3
Escriba un programa usando listas, que pida una letra de abecedario y muestre por pantalla:
a. “Es una vocal”, cuando la letra dada lo sea y
b. “No es una vocal”, cuando la letra dada no lo sea."""

print("")
print("Ejercicio 3")

letra = input("Introduce una letra del abecedario: ")

vocales = ["a", "e", "i", "o", "u"]
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

if letra.lower() in vocales:
    print("La letra " +letra + " es una vocal")
elif letra.lower() in consonantes:
    print("La letra " +letra +" no es una vocal")
else:
    print("Error, se ingresó un valor no válido")

"""Ejercicio 4
Escriba un programa usando “if-else” que pida una hora en tres variables: horas, minutos y segundos 
y muestre por pantalla “Hora correcta” u “Hora incorrecta” según el caso. Las horas deben ser mayor 
o igual a cero y menor o igual a 23, los minutos y los segundos deben estar entre 0 y 59 incluyendo 
0 y 59"""

print()
print("Ejercicio 4")
horas = int(input("Ingresa las horas: "))
minutos = int(input("Ingresa los minutos: "))
segundos = int(input("Ingresa los segundos: "))

if (0 <= horas <= 23) and (0 <= minutos <= 59) and (0 <= segundos <= 59):
    print(str(horas) +":" +str(minutos) +":" +str(segundos) + " es una Hora correcta")
else:
    print(str(horas) +":" +str(minutos) +":" +str(segundos) + " es una Hora incorrecta")

"""Ejercicio 5
Elabore un programa usando diccionarios que pida un numero de 1 al 7 y diga el dia de 
la semana correspondiente."""

print("")
print("Ejercicio 5")

dias_de_la_semana = {1 : "Lunes", 2 : "Martes", 3 : "Miercoles", 4 : "Jueves", 5 : "Viernes", 
                     6 : "Sabado", 7 : "Domingo"}

dia = int(input("Ingresa el día de la semana en número: "))

if 0 < dia <= 7:
    print(dias_de_la_semana[dia])
else:
    print("Error, se ingresó un valor no válido")