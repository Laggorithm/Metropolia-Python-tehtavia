MadeupBool = 0
numbers = []
while MadeupBool == 0:
    number = input("enter number: ")
    if number == "" or not number.isdigit():
        MadeupBool = 1
        numbers.sort()
        numbers.sort(reverse=True)
        print(numbers[0:5])
    else:
        numbers.append(int(number))
