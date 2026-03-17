print("=== GYM BAJA SI PUEDES ===")
compromiso_bajo = 0
compromiso_medio = 0
compromiso_alto = 0

for i in range(5):
    nombre = input("Nombre del usuario: ")
    dias = int(input("¿Cuántos días vino a la semana? "))
    minutos = int(input("¿Cuántos minutos entrena por día? "))
    
    if dias < 3:
        print("Bajo compromiso")
        compromiso_bajo = compromiso_bajo + 1
    elif dias <= 4:
        print("Compromiso medio")
        compromiso_medio = compromiso_medio + 1
    else:
        print("Compromiso alto")
        compromiso_alto = compromiso_alto + 1

print("--- RESULTADOS ---")
print("Bajo compromiso:", compromiso_bajo)
print("Compromiso medio:", compromiso_medio)
print("Compromiso alto:", compromiso_alto)