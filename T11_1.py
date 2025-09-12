class Julkaisu:
    def __init__(self, name):
        self.name = name
class Kirja(Julkaisu):
    def __init__(self,name , writer, pages):
        self.writer = writer
        self.pages = pages
        super().__init__(name)
class Lehti(Julkaisu):
    def __init__(self, name, toimit):
        self.toimit = toimit
        super().__init__(name)
JulkaisuList = [Lehti("Aku Ankka", "Aki Hyppä"), Kirja("Hytti n:o 6","Rosa Liksom",200)]
def PrintJulkaisu(julkaisuNimi):
        for julkaisu in JulkaisuList:
            if isinstance(julkaisu, Kirja) and julkaisu.name == julkaisuNimi:
                print(f"{julkaisu.name} is been written by {julkaisu.writer}, and has {julkaisu.pages} pages.")
            elif isinstance(julkaisu, Lehti)and julkaisu.name == julkaisuNimi:
                print(f"{julkaisu.name} is been published by {julkaisu.toimit}.")
while True:
    try:
        question = int(input("Uuusi julkaisu vai tarkistetaan? 1/2/3 (lopetetaan): "))
        if question == 1:
            question2 = int(input("Kirja tai lehti? 1/2: "))
            if question2 == 1:
                one = input("Enter julkaisun nimi: ")
                two = input("Enter julkaisun kirjoittaja: ")
                three = input("Enter julkaisun sivumäärä: ")
                uusiJulkaisu = Kirja(one, two, three)
                print(uusiJulkaisu.name, uusiJulkaisu.writer, uusiJulkaisu.pages)
                JulkaisuList.append(uusiJulkaisu)
            elif question2 == 2:
                one = input("Enter julkaisun nimi: ")
                two = input("Enter julkaisun toimittaja: ")
                uusiJulkaisu = Lehti(one, two)
                JulkaisuList.append(uusiJulkaisu)
                print(uusiJulkaisu.name, uusiJulkaisu.toimit)
        elif question == 2:
            name = input("Enter julkaisun nimi: ")
            PrintJulkaisu(name)
        elif question == 3:
            break
    except ValueError:
        print("wrong input")


