Count = 0
while Count < 1000:
    currentNumber = Count / 3
    RcurrendNumber = currentNumber // 1
    CurrentNumber = currentNumber - RcurrendNumber
    if CurrentNumber == 0:
        print(Count)
    Count += 1
