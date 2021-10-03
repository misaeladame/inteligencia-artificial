"""Escribir una función que reciba un número entero positivo y devuelva su
factorial."""

def factorial(numero): 
    factorial = 1    
    if numero < 0:
        print("No existe el factorial de números negativos")
    else:
        while numero > 0:
            numero -= 1
            factorial += factorial * numero
        return factorial

numero = int(input("Ingresa el número para calcular su factorial: "))
print("El factorial de {0:d} es = {1:d}".format(numero, factorial(numero)))