#Autot
class Auto:
    speed = 0
    distance = 0
    MaxSpeed = 0
    def __init__(self, RegNumber, speed, MaxSpeed, distance):
        self.number = RegNumber
        self.speed = speed
        self.distance = distance
        self.MaxSpeed = MaxSpeed
    def kiihdyta(Auto):
        Auto.speed += random.randint(-10, +15)
        if Auto.speed > Auto.MaxSpeed:
            Auto.speed = Auto.MaxSpeed
    def kulje(Auto, TravelTime):
        Auto.distance += Auto.speed * TravelTime

#Auto-tehdäs
def CreateCars(amountOfCars):
    for i in range(amountOfCars):
        randomSpeed = random.randint(100, 200)
        car = Auto(f"ABC-{i}", 0, randomSpeed, 0)
        Cars.append(car)
    return

#Ohjelma
import random
Cars=[]
CreateCars(10)
RaceOn = True
while RaceOn:
    for car in Cars:
        Auto.kiihdyta(car)
        Auto.kulje(car, 130)
        print(car.number, car.speed, car.MaxSpeed, car.distance, )
        if car.distance >= 10000:
            RaceOn = False
            break

