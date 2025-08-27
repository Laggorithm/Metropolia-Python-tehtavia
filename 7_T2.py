nimet = set()
while True:
    try:
        nimi = input("Anna nimi: ")
        if nimi != "":
            if nimi not in nimet:
                nimet.add(nimi)
                print("Uusi nimi")
            else:
                print("Aiemmin syötetty nimi")
        else:
            print(nimet)
            break
    except ValueError:
        print("Something went wrong")