print("=== TIENDA DEPORTIVA DONDE MAJO ===")

contador= 0 
for i in range(6):
    precio= float(input("INGRESE EL PRECIO DEL PRODUCTO:"))
    if precio > 100000:
        contador += 1
    
print("CANTIDAD DE PRODUCTOS MAYORES A 100000:", contador)
