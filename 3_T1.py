length = int(input("Mitä pituus?(cm) "))

if int(length) < 37:
    verdictB = 37 - length
    print(f"on {verdictB} alle sallitua! ")
else:
    verdictA = length - 37
    print(f"pidenmpi {verdictA} cm kuin minimi, nice! ")