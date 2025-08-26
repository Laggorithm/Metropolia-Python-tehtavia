ActivityState = True
def galToLitr():
    liters = Gallons * 3.785
    print(f"In liters: {liters}")
    return liters
while ActivityState:
    try:
        Gallons = float(input("Gallons: "))
        floatGallons = float(Gallons)
        galToLitr()
        ActivityState = False
    except ValueError:
        print("Enter a number. Please.")
        ActivityState = True