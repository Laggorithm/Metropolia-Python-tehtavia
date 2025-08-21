MadeupBool = 0
numbers = []
while MadeupBool == 0:
    number = input("enter number: ")
    if number == "" or not number.isdigit():
        MadeupBool = 1
        print(numbers)
        print(f"Min number {min(numbers)}")
        print(f"Max number {max(numbers)}")
    else:
        numbers.append(number)