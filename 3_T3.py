Nmin = 117
Nmax = 175
Mmin = 134
Mmax = 195

ProgramToken = 0

while ProgramToken == 0:
    sukupuoli = input("Sukupuoli M/N: ")
    if sukupuoli == "N" or sukupuoli == "n" or sukupuoli == "nainen" or sukupuoli == "Nainen" or sukupuoli == "NAINEN":
        hemoglob = int(input("Hemoglobiini: "))
        if hemoglob < Nmin:
            print("alle")
            ProgramToken = 1
        elif hemoglob > Nmax:
            print("yli")
            ProgramToken = 1
        elif hemoglob > Mmin and hemoglob < Mmax:
            print("normaali")
            ProgramToken = 1
        else:
            print("wrong input")

    elif sukupuoli == "M" or sukupuoli == "m" or sukupuoli == "mies" or sukupuoli == "Mies" or sukupuoli == "MIES":
        hemoglob = int(input("Hemoglobiini: "))
        if hemoglob < Nmin:
            print("alle")
            ProgramToken = 1
        elif hemoglob > Nmax:
            print("yli")
            ProgramToken = 1
        elif hemoglob > Mmin and hemoglob < Mmax:
            print("normaali")
            ProgramToken = 1
        else :
            print("wrong input")