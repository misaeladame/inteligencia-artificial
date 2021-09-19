renta = int(input("Ingresa tu renta anual: "))

if renta >= 0 and renta < 10000:
    print("Su tipo impositivo es del 5%")
elif renta >= 10000 and renta < 20000:
    print("Su tipo impositivo es del 15%")
elif renta >= 20000 and renta < 35000:
    print("Su tipo impositivo es del 20%")
elif renta >= 35000 and renta < 60000:
    print("Su tipo impositivo es del 30%")
elif renta >= 60000:
    print("Su tipo impositivo es del 45%")
else:
    print("Error, cantidad no valida") 