"""Ejericio 1"""
print("Ejericio 1")

n1 = int(input("Ingresa el número 1: "))
n2 = int(input("Ingresa el número 2: "))

if n1 > n2:
    print(n1, "es mayor que", n2)
elif n2 == n1:
    print("Ambos números son iguales")
else:
    print(n2, "es mayor que", n1)

"""Ejercicio 2"""
print("\n\nEjercicio 2")

def max_de_tres(n1, n2, n3):
    if n1 > (n2 and n3):
        print(n1, "es mayor que", n2, "y", n3)
    elif n2 > (n1 and n3):
        print(n2, "es mayor que", n1, "y", n3)
    elif n3 > (n2 and n1):
        print(n3, "es mayor que", n2, "y", n1)
    elif n1 == n2 == n3:
        print("Los tres números son iguales")

max_de_tres(1, 2, 3)
max_de_tres(2, 1, 0)
max_de_tres(3, 8, 6)
max_de_tres(3, 3, 3)
