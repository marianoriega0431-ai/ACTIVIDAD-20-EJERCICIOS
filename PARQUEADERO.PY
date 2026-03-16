print("=== PARQUEADERO EL CARERO ===")

horas = int(input("¿cuantas horas duro su vehiculo en el parqueadero?:"))

if horas== 1:
    total= 5000
else:
    total= 5000 + (horas - 1) * 3000
    
    print("total a pagar:", total)
    