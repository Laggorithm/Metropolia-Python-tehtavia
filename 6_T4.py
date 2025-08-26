intList = []
number = 0
fails = 0

def sum():
    summa = 0
    for i in intList:
        summa += i
    return summa
ActivityBool = True
while ActivityBool:
    try:
        number = int(input("Enter a number(press enter 3 time to end the program): "))
        intList.append(number)
    except ValueError:
        fails += 1
        if fails == 3:
            print("Enter an integer. Please. (1; 2; 3; BUT not 1.3 11243,2332; 12332.21313 or such!)")
            print(f"sum of: {intList}")
            sum()
            ActivityBool = False
print(f"sum: {sum()}")
