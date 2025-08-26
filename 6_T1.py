import random
def rolld6():
    a = random.randint(1, 6)
    print(a)
    return

while rolld6() != 6:
    rolld6()