print("=== CENTRO DE IDIOMAS EL SABER ===")
suma_notas_grupo = 0
total_estudiantes = 0
mejor_nota = 0
estudiante_estrella = ""

bajo = 0
medio = 0
alto = 0

quiere_registrar = "si"

while quiere_registrar == "si":
    nombre = input("Nombre del estudiante: ")
    n1 = float(input("Nota de Speaking: "))
    n2 = float(input("Nota de Listening: "))
    n3 = float(input("Nota de Reading: "))
    
    promedio = (n1 + n2 + n3) / 3
    print("Su promedio es:", promedio)
    
    if promedio < 60:
        print("Nivel: Bajo")
        bajo = bajo + 1
    elif promedio <= 79:
        print("Nivel: Medio")
        medio = medio + 1
    else:
        print("Nivel: Alto")
        alto = alto + 1
  
    suma_notas_grupo = suma_notas_grupo + promedio
    total_estudiantes = total_estudiantes + 1

    if promedio > mejor_nota:
        mejor_nota = promedio
        estudiante_estrella = nombre
        
    quiere_registrar = input("¿Registrar otro estudiante? (si/no): ").lower()

print("--- RESULTADOS DEL CURSO ---")
if total_estudiantes > 0:
    print("Promedio general del grupo:", suma_notas_grupo / total_estudiantes)
    print("El mejor estudiante fue:", estudiante_estrella, "con", mejor_nota)
print("Estudiantes por nivel - Bajo:", bajo, "Medio:", medio, "Alto:", alto)
