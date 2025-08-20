from tokenize import endpats

uLeiviska = float(input("Leiviskä: "))
uNaula = float(input("Naula: "))
uLuoti = float(input("Luoti: "))
summa = (13.3 * 20 * 32 * uLeiviska) + (13.3 * 32 * uNaula) + (13.3 * uLuoti)
print(summa)
kysymys = input("Muunetaanko kg:ksi? Y/N ")
if kysymys == "Y" or kysymys == "y":
    summa2 = summa/1000
    kg = int(summa2)
    print(f"{kg} kg")
    g = summa2 - kg
    gram = g * 1000
    grammaa = round(gram, 1)
    print(f"{grammaa} grammaa")

elif kysymys == "N" or kysymys == "n":
    print("Bye")
else:
    print("Fooling around? Bye")




