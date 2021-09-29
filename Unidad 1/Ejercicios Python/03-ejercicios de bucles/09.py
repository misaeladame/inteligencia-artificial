"""Escribir un programa que pida al usuario un número entero y
muestre por pantalla si es un número primo o no."""

numero = int(input("Ingrese un número entero: "))
primo = True

if numero <= 1:
    print(f"El número {numero} NO es primo")
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(f"El número {numero} SI es primo")
    else:
        print(f"El número {numero} NO es primo")
    



    
    