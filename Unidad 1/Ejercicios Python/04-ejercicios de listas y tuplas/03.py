"""Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura, y después las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura> es
cada una des las asignaturas de la lista y <nota> cada una de
las correspondientes notas introducidas por el usuario."""

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nota = []

for asignatura in asignaturas:
    nota.append(int(input("¿Cuál fue la nota que saco en la asignatura de " +asignatura +"? ")))

i = 0;
for asignatura in asignaturas:
    print("En " +asignatura +" has sacado " +str(nota[i]))
    i += 1