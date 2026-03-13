print("=== BIENVENIDOS A HELADERIA, DULCE SABOR ===")
print("ELIJA EL SABOR DE SU HELADO:")

vainilla = 0
chocolate = 0
fresa = 0

cantidad = int(input("Ingresa la cantidad de helados que deseas (máximo 5): "))

if cantidad > 5:
    print("No puedes pedir más de 5 helados")
else:
    for i in range(cantidad):

        sabor = input("Ingrese el sabor (vainilla, chocolate, fresa): ").lower()

        if sabor == "vainilla":
            vainilla += 1
        elif sabor == "chocolate":
            chocolate += 1
        elif sabor == "fresa":
            fresa += 1
        else:
            print("Sabor no válido")

    print("Resultados finales:")
    print("Vainilla:", vainilla)
    print("Chocolate:", chocolate)
    print("Fresa:", fresa)