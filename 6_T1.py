import random
def rolld6():
    a = random.randint(1, 6)
    print(a)
    return a

while rolld6() != 6:
    rolld6()