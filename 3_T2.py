
ClassStatus = 0
while ClassStatus == 0:
    Class = input("Enter a class LUX/A/B/C: ")
    if Class == "LUX" or Class == "lux":
        print("LUX on parvekkeellinen hytti yläkannella.")
        ClassStatus = 1
    elif Class == "A" or Class == "a":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
        ClassStatus = 1
    elif Class == "B" or Class == "b":
        print("B on ikkunaton hytti autokannen yläpuolella.")
        ClassStatus = 1
    elif Class == "C" or Class == "c":
        print("C on ikkunaton hytti autokannen alapuolella.")
        ClassStatus = 1
    else:
        print("Virheellinen hyttiluokka")


