import random
dotAmount = int(input("Miten paljon pisteitä? "))
hits = 0
while dotAmount > 0:
    x = round(random.uniform(-1, 1), 3)
    y = round(random.uniform(-1, 1), 3)
    if x**2 + y**2 < 1:
        dotAmount -= 1
        hits += 1
    else:
        dotAmount -= 1
print(hits)


