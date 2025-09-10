import random
#Autot
class Race:
    RaceOn = True
    RaceLength = 0
    def __init__(self, raceLength):
        self.RaceLength = raceLength
    def RaceOver(self):
        for car in Cars:
            if car.distance >= self.RaceLength and car not in Winners and len(Winners) < 1:
                Winners.append(car)
                self.RaceOn = False
                self.RaceSituation()
    def HourPass(self, hours):
        self.Hours = hours
        for i in range(hours):
            for car in Cars:
                Auto.kiihdyta(car)
                Auto.kulje(car, self.Hours)
    def RaceSituation(self):
        try:
            if newRace.RaceOn:
                for car in Cars:
                    print(f"Auton id: {car.RegNumber}, distance: {car.distance}")
            else:
                for car in Winners:
                    print(f"Auton id: {car.RegNumber} is winner")
        except ValueError:
            print("Something went wrong in RaceSituation")
class Auto:
    speed = 0
    distance = 0
    MaxSpeed = 0
    RegNumber = ""
    def __init__(self, RegNumber, speed, MaxSpeed, distance):
        self.RegNumber = RegNumber
        self.speed = speed
        self.distance = distance
        self.MaxSpeed = MaxSpeed
    def kiihdyta(Auto):
        Auto.speed += random.randint(-10, +35)
        if Auto.speed > Auto.MaxSpeed:
            Auto.speed = Auto.MaxSpeed
    def kulje(Auto, TravelTime):
        if Auto.distance < newRace.RaceLength:
            Auto.distance += Auto.speed * TravelTime
            newRace.RaceOver()


#Auto-tehdäs
def CreateCars(amountOfCars):
    for i in range(amountOfCars):
        randomSpeed = random.randint(100, 200)
        car = Auto(f"ABC-{i}", 0, randomSpeed, 0)
        Cars.append(car)
    return

#Ohjelma

Cars=[]
Winners = []
CreateCars(10)
newRace = Race(random.randint(8000, 10000))
while newRace.RaceOn:
    try:
        print(newRace.RaceLength)
        choice = int(input("Skip time or check how's the race? (1/2): "))
        if choice == 1:
            hours = int(input("How many hours?: "))
            newRace.HourPass(hours)
        elif choice == 2:
            newRace.RaceSituation()
    except ValueError:
        print("Wrong input, try number instead")

