numbers = []
fails = 0
def CheckList():
    checkedList = []
    for i in numbers:
        if i % 2 == 0:
            checkedList.append(i)
    return checkedList
#Välillä kirjoitan enkulla ja valilla kirjoitan suomen kielellä. Älä ihmetellä jos tässä imeistyy jossain venäjä myös
#Puhun ne kaikki sama verran
ActivityBool = True
while ActivityBool:
    try:
        number = int(input("Enter a number(press enter 3 time to end the program): "))
        numbers.append(number)
    except ValueError:
        print("Enter a number, please")
        fails += 1
        if fails == 3:
            ActivityBool = False
            CheckList()
            print(f"List only with those who can be divided by 2 without leftovers{CheckList()}")
