"""Programa que almacene la cadena de
caracteres contraseña en una variable, pregunte al usuario
por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la
variable sin tener en cuenta mayúsculas y minúsculas."""

contrasenia = "contraseña"

verificacion_contrasenia = input("Ingresa la contraseña: ")

if verificacion_contrasenia.lower() in contrasenia:
    print("Las contraseñas SI coinciden")
else:
    print("Las contraseñas NO coinciden")