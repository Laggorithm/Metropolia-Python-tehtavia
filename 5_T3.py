
AnswerIndexes = []
amountOfTrues = 0
while True:
    number = int(input("Anna luku: "))
    for i in range(number +1):
        if i != 0:
            Equation = float(number) / float(i)
            print(i)
            if Equation == 1.0 or Equation == float(number):
                print(i)
                AnswerIndexes.append(1)
            elif Equation - int(Equation) == 0.0:
                AnswerIndexes.append(0)
            else:
                AnswerIndexes.append(3)

    print(AnswerIndexes)
    for indexes in AnswerIndexes:
        if indexes == 0:
            amountOfTrues += 1
    if amountOfTrues == 0:
        print("Luku on alkuluku")
    else:
        print("Ei ole alkuluku")
