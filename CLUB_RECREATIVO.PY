print("=== CLUB RECREATIVO EL SOL ===")
plata_club = 0
basico = 0
premium = 0
familiar = 0

persona = "si"

while persona == "si":
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    plan = input("Plan (basico, premium, familiar): ").lower()
    
    if edad < 18:
        print("REGISTRO JUVENIL")
    elif edad >= 60:
        print("BENEFICIO SENIOR")
        
    if plan == "basico":
        plata_club = plata_club + 50000
        basico = basico + 1
    elif plan == "premium":
        plata_club = plata_club + 90000
        premium = premium + 1
    elif plan == "familiar":
        plata_club = plata_club + 130000
        familiar = familiar + 1
        
    persona = input("¿Hay otra persona? (si/no): ").lower()

print("--- CIERRE DEL CLUB ---")
print("Total recaudado: $", plata_club)
print("Personas por plan -> Basico:", basico, "Premium:", premium, "Familiar:", familiar)

if basico > premium and basico > familiar:
    print("El plan más vendido fue el Básico")
elif premium > familiar:
    print("El plan más vendido fue el Premium")
else:
    print("El plan más vendido fue el Familiar")