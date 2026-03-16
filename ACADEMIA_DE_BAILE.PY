print("=== ACADEMIA DE BAILE LA OXIDADA ===")

clases= int(input("ingrese la cantidad de clases que ha realizado:"))

if clases < 5:
    print("asistencia baja")
elif clases >= 5 and clases <= 8:
    print("asistencia media")
else:
    print("asistencia alta")
