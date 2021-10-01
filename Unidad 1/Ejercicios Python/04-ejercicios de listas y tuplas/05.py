"""Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura y elimine de la lista las asignaturas aprobadas. Al final
el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir."""

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
asignaturas_reprobadas = []

for asignatura in asignaturas:
    nota = int(input("Ingresa tu nota en la asignatura de " +asignatura +": "))
    notas.append(nota)

i = 0
for asignatura in asignaturas:
    if notas[i] <= 5:
        asignaturas_reprobadas.append(asignatura)
    i += 1

print("Las materias que tienes que repetir son: " +str(asignaturas_reprobadas))
