"""programa que pregunte al usuario su edad y
muestre por pantalla si es mayor de edad o no."""

edad = int(input("Ingresa tu edad: "))
if edad < 18 and edad >= 0:
    print("Eres menor de edad")
elif edad >= 18 and edad <= 120:
    print("Eres mayor de edad")
else:
    print("Edad incorrecta")