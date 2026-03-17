print("=== PARQUEADERO SAL SI PUEDES ===")
recaudado = 0
cant_carros = 0
cant_motos = 0
pago_maximo = 0

for i in range(8):
    print("Vehículo número:", i + 1)
    placa = input("Ingrese la placa: ")
    tipo = input("¿Es carro o moto? ").lower()
    horas = int(input("¿Cuántas horas se quedó? "))
    
    if tipo == "carro":
        total_pago = horas * 4000
        cant_carros = cant_carros + 1
    elif tipo == "moto":
        total_pago = horas * 2000
        cant_motos = cant_motos + 1
    else:
        print("Tipo no válido")
        total_pago = 0

    print("Este vehículo paga:", total_pago)
    recaudado = recaudado + total_pago
    
    if total_pago > pago_maximo:
        pago_maximo = total_pago

print("--- REPORTE FINAL ---")
print("Total de dinero:", recaudado)
print("Carros que entraron:", cant_carros)
print("Motos que entraron:", cant_motos)
print("El pago más alto fue de:", pago_maximo)