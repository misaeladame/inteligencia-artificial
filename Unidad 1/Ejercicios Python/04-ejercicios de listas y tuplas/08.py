"""Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos tuplas y muestre por pantalla su producto escalar."""

producto_escalar = 0
vector1 = (1, 2, 3)
vector2 = (-1, 0, 2)

for i in range(len(vector1)):
    producto = vector1[i] * vector2[i]
    producto_escalar += producto

print("El producto escalar de los vectores " +str(vector1) +" y " +str(vector2) +" es " +str(producto_escalar))