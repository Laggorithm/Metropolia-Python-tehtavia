
numbers = []
while True:
    number = input("enter number: ")
    if number == "" or not number.isdigit():
        print(numbers)
        print(f"Min number {min(numbers)}")
        print(f"Max number {max(numbers)}")
        break
    else:
        numbers.append(number)