print("=== CAFETERIA DONDE MAJO===")

cafe = 4000
te = 3000
jugo = 5000

bebida= input ("¿que bebida deseas ordenar? (cafe, te, jugo):")
cantidad= int (input("¿cuantas deseas?"))

if bebida == "cafe":
    total = cafe * cantidad
elif bebida == "te":
    total = te * cantidad
elif bebida == "jugo":
    total = jugo * cantidad     
    
if total > 0:
    print("total a pagar:" , total)
    