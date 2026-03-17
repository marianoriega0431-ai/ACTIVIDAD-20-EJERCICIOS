print("=== PELUQUERIA LA CALVA ===")
plata_dia = 0
corte = 0
cepillado = 0
tintura = 0

for i in range(7):
    nombre = input("Nombre del cliente: ")
    print("Servicios: corte, cepillado, tintura")
    servicio = input("¿Qué servicio se hizo? ").lower()
    pago = int(input("¿Cuánto pagó? "))
    
    plata_dia = plata_dia + pago
    
    if servicio == "corte":
        corte = corte + 1
    elif servicio == "cepillado":
        cepillado = cepillado + 1
    elif servicio == "tintura":
        tintura = tintura + 1

print("--- REPORTE PELUQUERÍA ---")
print("Total de dinero hoy: $", plata_dia)
print("Cortes:", corte, "| Cepillados:", cepillado, "| Tinturas:", tintura)

if corte > cepillado and corte > tintura:
    print("El servicio más pedido fue el Corte")
elif cepillado > tintura:
    print("El servicio más pedido fue el Cepillado")
else:
    print("El servicio más pedido fue la Tintura")