"""Escribir un programa que almacene las matrices
en una tupla y muestre por pantalla su producto.
Nota: Para representar matrices mediante tuplas usar tuplas
anidadas, representando cada vector fila en una tupla."""

A = ((1, 2, 3), 
     (4, 5, 6))
B = ((-1, 0),(0, 1), (1, 1))
producto = [[0, 0],
            [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            producto[i][j] += A[i][k] * B[k][j]

for i in range(len(producto)):
    producto[i] = tuple(producto[i])
producto = tuple(producto)
for i in range(len(producto)):
    print(producto[i])

    