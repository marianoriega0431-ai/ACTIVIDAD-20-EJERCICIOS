print("=== PETS SHOP MI AMIGO FIEL ===")
suma_alimento = 0
suma_juguete = 0
suma_accesorio = 0

for i in range(10):
    print("Venta número:", i + 1)
    categoria = input("Categoría (alimento, juguete, accesorio): ").lower()
    valor = float(input("Valor de la compra: "))
    
    if categoria == "alimento":
        suma_alimento = suma_alimento + valor
    elif categoria == "juguete":
        suma_juguete = suma_juguete + valor
    elif categoria == "accesorio":
        suma_accesorio = suma_accesorio + valor
    else:
        print("Esa categoría no existe")

print("--- TOTALES POR CATEGORÍA ---")
print("Alimento: $", suma_alimento)
print("Juguete: $", suma_juguete)
print("Accesorio: $", suma_accesorio)

# Para saber cuál generó más dinero:
if suma_alimento > suma_juguete and suma_alimento > suma_accesorio:
    print("La categoría que más dinero dio fue: Alimento")
elif suma_juguete > suma_accesorio:
    print("La categoría que más dinero dio fue: Juguete")
else:
    print("La categoría que más dinero dio fue: Accesorio")