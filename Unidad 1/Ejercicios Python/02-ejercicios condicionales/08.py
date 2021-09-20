"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a
sus clientes. Los ingredientes para cada tipo de pizza aparecen a
continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza
vegetariana o no, y en función de su respuesta le muestre un menú con
los ingredientes disponibles para que elija. Solo se puede eligir un
ingrediente además de la mozzarella y el tomate que están en todas la
pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva."""

pizza_vegetariana = input("¿Desea que su pizza sea vegetariana (Contestar: Si o No): ")

ingredientes_basico = "mozzarella, tomate"

if pizza_vegetariana.lower() == "si":
    print("Menú de los ingredientes: Pimiento y tofu")
    print("Escoger solo uno")
    ingrediente = input()
    if ingrediente.lower() in ("pimiento", "tofu"):
        print("Su pizza es vegetariana y los ingredientes que lleva son la " +ingredientes_basico +" y " +ingrediente.lower())
    else:
        print("Error, Ingrediente no válido")
elif pizza_vegetariana.lower() == "no":
    print("Menú de los ingredientes: Peperoni, Jamon y Salmon")
    print("Escoger solo uno")
    ingrediente = input()
    if ingrediente.lower() in ("peperoni, jamon, salmon"):
        print("Su pizza no es vegetariana y los ingredientes que lleva son la " +ingredientes_basico +" y " +ingrediente.lower())
    else:
        print("Error, ingrediente no válido")
else:
    print("Error, selección no válida")