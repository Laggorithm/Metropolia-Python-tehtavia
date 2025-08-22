import random
diceNum = []
ActivityState = True
while ActivityState == True:
    userDice = input("How many dices do we roll? ")
    if userDice.isdigit() == False:
        print("Not a number, 20 Tarrasques attack you, roll the initiative")
    else:
        for cycle in range(int(userDice)):
            rollD6 = random.randint(1, 6)
            diceNum.append(rollD6)
            if cycle == 0:
                ActivityState = False
if ActivityState == False:
    print(diceNum)