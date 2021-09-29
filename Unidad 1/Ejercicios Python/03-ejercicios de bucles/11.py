"""Escribir un programa en el que se pregunte al usuario por
una frase y una letra, y muestre por pantalla el número de
veces que aparece la letra en la frase."""

frase = input("Introduce una frase: ")
letra = input("Ingrese una letra: ")

if len(letra) > 1:
    print("Incorrecto, se ingresó más de 2 caracteres en la letra")
else:
    c = 0
    for i in frase:
        if letra.lower() == i.lower():
            c += 1
    print("La letra " +letra +" aparece " +str(c) + " veces en la frase que introdujo")

