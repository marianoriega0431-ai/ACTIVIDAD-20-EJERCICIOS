print("=== HELADERIA DULCE TENTACION ===")
plata_total = 0
clientes_atendidos = 0

conos_vendidos = 0
vasos_vendidos = 0
bananas_vendidas = 0

quiere_seguir = "si"


while quiere_seguir == "si":
    print("=== NUEVA VENTA ===")
    print("opciones: cono (3000), vaso (4000), banana split (9000)")
    pedido = input("¿que va a llevar? ").lower()
    cuantos = int(input("¿cuantos quiere? "))
    
    if pedido == "cono":
        precio = 3000
        conos_vendidos += cuantos
    elif pedido == "vaso":
        precio = 4000
        vasos_vendidos += cuantos
    elif pedido == "banana split":
        precio = 9000
        bananas_vendidas += cuantos
    else:
        print("ese producto no lo tenemos.")
        precio = 0
        cuantos = 0

    pago_cliente = precio * cuantos
    plata_total += pago_cliente
    
    if pago_cliente > 0:
        clientes_atendidos += 1
        print("el cliente debe pagar:", pago_cliente)

    quiere_seguir = input("¿atender a otro? (si/no): ").lower()


print("=== RESUMEN DEL DÍA ===")
print("dinero total:", plata_total)
print("clientes totales:", clientes_atendidos)

if conos_vendidos > vasos_vendidos and conos_vendidos > bananas_vendidas:
    print("lo que más se vendió fue: cono")
elif vasos_vendidos > bananas_vendidas:
    print("lo que más se vendió fue: vaso")
else:
    print("lo que más se vendió fue: banana split")