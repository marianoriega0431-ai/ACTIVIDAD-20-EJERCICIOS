print("=== CAFETERIA EL FILO ===")
total_dia = 0
continuar = ""

while continuar != "salir":
    producto = input("¿que desea comprar? (cafe, capuchino, pastel): ").lower()
    
    if producto == "cafe":
        precio = 4000
    elif producto == "capuchino":
        precio = 7000
    elif producto == "pastel":
        precio = 6000
    else:
        precio = 0
        print("Ese producto no existe")

    if precio > 0:
        if total_dia > 20000:
            descuento = precio * 0.10
            final = precio - descuento
            print("Se aplicó descuento del 10%")
        else:
            final = precio
            print("Cobro normal")
        
        print("Total de este pedido:", final)
        total_dia = total_dia + final
        
    continuar = input("Escriba 'salir' para cerrar o cualquier tecla para seguir: ").lower()

print("Dinero total acumulado hoy:", total_dia)