print("=== CINE EL HUESO ===")
capacidad = int(input("¿Cuántas personas caben en la sala? "))
ingresados = 0
niños = 0
adultos = 0
mayores = 0

while ingresados < capacidad:
    edad = int(input("Edad de la persona: "))
    
    if edad < 13:
        niños = niños + 1
    elif edad < 60:
        adultos = adultos + 1
    else:
        mayores = mayores + 1
        
    ingresados = ingresados + 1
    print("Van", ingresados, "personas dentro.")
    
    if ingresados < capacidad:
        seguir = input("¿Entra alguien más? (si/no): ")
        if seguir == "no":
            break

print("--- REPORTE ---")
print("Niños:", niños)
print("Adultos:", adultos)
print("Adultos mayores:", mayores)
print("Total en sala:", ingresados)

if ingresados == capacidad:
    print("La sala se llenó")
else:
    print("Todavía sobró espacio")
