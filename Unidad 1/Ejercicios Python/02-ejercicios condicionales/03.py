"""Programa que pida al usuario dos números y
muestre por pantalla su división. Si el divisor es cero el
programa debe mostrar un error."""

dividendo = int(input("Ingresa el dividendo: "))
divisor = int(input("Ingresa el divisor: "))

if divisor == 0:
    print("Error, número indeterminado")
else:
    division = dividendo / divisor
    print(division)