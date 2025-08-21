Name = ["aboba", "Hello13223", "MrNobody", "python"]
import sys

print(Name)
Password = ["1234", "2442", "12452", "rules"]
#Tein semmosen systeemin koska halusin kokeila miten se voisi toimia jos siinä olisi enemmäin kuin 1 user
RegState = False
LoginState = False
TryCount = 5
while True:
    while RegState == False and LoginState == False:
        startQuestion = input("Wish to log in or registrate? (L/R): ")
        if startQuestion in ["r", "R"]:
            RegState = True
        elif startQuestion in ["l", "L"]:
            LoginState = True

    if RegState == True:
        while True:
            nameVar = input("Enter your name: ")
            Name.append(nameVar)
            Password.append(1234)
            question = input("Do you want to set password?? Basic one is 1234 (y/n): ")
            if question in ["y", "Y", "Yes", "YES"]:
                currentNameIndex = Name.index(nameVar)
                print(currentNameIndex)
                PasswordVar = input("Enter your password: ")
                Password[currentNameIndex] = (PasswordVar)
                print(Password)
                RegState = False
                break
            else:
                RegState = False
                break
    elif LoginState == True:
        while True:
            nameVar = input("Enter your name: ")
            while nameVar in Name:
                currentNameIndex = Name.index(nameVar)
                print(currentNameIndex)
                PasswordCheck = Password[currentNameIndex]
                print(PasswordCheck)
                PasswordVar = input("Enter your password: ")
                if PasswordVar == PasswordCheck:
                    print(f"Right password, welcome in, {nameVar}!")
                    LoginState = False
                    break
                else:
                    print(f"Wrong password, {nameVar}!")
                    TryCount -= 1
                    print(TryCount)
                    if TryCount == 0:
                        print("Too many tries!!!!")
                        sys.exit()
            else:
                print(f"Wrong name, please try again.")


