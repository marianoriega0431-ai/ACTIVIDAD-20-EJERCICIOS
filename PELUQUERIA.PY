print("=== PELUQUERIA DONDE MAJO ===")

hora= int(input("INGRESE HORA DE LLEGADA (6 A 22):"))

if hora >= 6 and hora <=11:
    print("turno mañana")
if hora >= 12 and hora <= 17:
    print("turno tarde")
elif hora >= 12 and hora <22:
    print("turno noche")
else:
    print("fuera de horario")