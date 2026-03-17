print("=== ROPA DEPORTIVA EL SUDOR ===")
agotados = 0
bajo = 0
normal = 0

for i in range(10):
    print("Producto número:", i + 1)
    nombre = input("Nombre del producto: ")
    cantidad = int(input("¿Cuánta cantidad hay disponible? "))
    
    if cantidad == 0:
        print("Estado: Agotado")
        agotados = agotados + 1
    elif cantidad >= 1 and cantidad <= 5:
        print("Estado: Stock bajo")
        bajo = bajo + 1
    else:
        print("Estado: Stock normal")
        normal = normal + 1

print("--- RESUMEN DE INVENTARIO ---")
print("Productos agotados:", agotados)
print("Productos con stock bajo:", bajo)
print("Productos con stock normal:", normal)
