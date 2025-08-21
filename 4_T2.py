MadeupBool = 0
while MadeupBool == 0:
    tuuma = float(input("Tuuma: "))
    if tuuma > 0:
        cm = tuuma * 2.54
        print(f"cm: {cm:.2f}")
    else:
        print("ei miinuksia sallittuna, bye")
        MadeupBool = 1