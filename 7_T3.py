FlightIndexes = {}
def IndexAdd():
    try:
        UserInputIndex = input("Enter index of airport:")
        UserInputName = input("Enter name of airport:")
        if UserInputIndex not in FlightIndexes:
            FlightIndexes[UserInputIndex] = UserInputName
            print(FlightIndexes)
        else:
            print("Already exists")
    except ValueError:
        print("Something went wrong")
        return FlightIndexes
################################################
def IndexCheck():
    try:
        UserInputIndex = input("Enter index of airport:")
        if UserInputIndex in FlightIndexes:
            print(f"Name of airport: {FlightIndexes[UserInputIndex]}")
        elif len(FlightIndexes) == 0:
            print("No airports found, add one")
        else:
            print("Not found")
    except ValueError:
        print("Something went wrong")
    return
##################################################
while True:
    try:
        question = input("New airport, or searching an existing one? (1/2): ")
        if question == "1":
            IndexAdd()
        elif question == "2":
            IndexCheck()
        elif question == "":
            break
    except ValueError:
        ("something went wrong")
