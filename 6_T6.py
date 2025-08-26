import math

def PizzaCalc():
    overallPriceA = priceA / (math.pi * (diameterA / 2) ** 2 / 10000)
    overallPriceB = priceB / (math.pi * (diameterB / 2) ** 2 / 10000)
    Checking = overallPriceA - overallPriceB
    if Checking < 0:
        BestChoice = "First Pizza better"
    elif Checking > 1:
        BestChoice = "Second Pizza better"
    return BestChoice
while True:
    try:
        diameterA = float(input("Diameter of the first pizza: "))
        priceA = float(input("Price of the first pizza: "))
        diameterB = float(input("Diameter of the second pizza: "))
        priceB = float(input("Price of the second pizza: "))
        PizzaCalc()
        print(PizzaCalc())
    except ValueError:
        print("Diameter must be a number.")