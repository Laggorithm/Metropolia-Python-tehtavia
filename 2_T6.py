import random
Code1Length = 3
Code2Length = 4
Code1 = []
Code2 = []
while Code1Length > 0:
    Random1 = random.randint(0, 9)
    Code1.append(Random1)
    Code1Length -= 1
if Code1Length == 0:
    print("Code1 generated")
    while Code2Length > 0:
        Random2 = random.randint(6, 6)
        Code2.append(Random2)
        Code2Length -= 1
    if Code2Length == 0:
        print("Code2 generated")
if Code2Length == 0 and Code1Length == 0:
    print("All codes generated")
    print(f"Code 1: {Code1}, Code 2: {Code2}")