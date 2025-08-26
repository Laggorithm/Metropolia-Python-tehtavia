import random
userInput = int(input("Enter a number: "))
def rolldice():
    a = random.randint(1, userInput)
    print(a)
    return a

while rolldice() != userInput:
    rolldice()