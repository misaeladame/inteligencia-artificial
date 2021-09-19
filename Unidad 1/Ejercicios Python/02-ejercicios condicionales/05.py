"""Para tributar un determinado impuesto se debe ser mayor
de 16 años y tener unos ingresos iguales o superiores a
1000 € mensuales. Escribir un programa que pregunte al
usuario su edad y sus ingresos mensuales y muestre por
pantalla si el usuario tiene que tributar o no."""

edad = int(input("Ingresa tu edad: "))
ingreso_mensual = int(input("Introduce tu ingreso mensual: "))

if edad > 16 and ingreso_mensual >= 1000:
    print("Usted usuario SI tiene que tributar")
else:
    print("Usted usuario NO tiene que tributar")