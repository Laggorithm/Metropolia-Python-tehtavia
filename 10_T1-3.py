ElevList =[]
class Building:
    MaxFloor = 9
    MinFloor = 0
    ElevAmount = 0
    def __init__(self, maxFloor, minFloor, elevAmount):
        self.MaxFloor = maxFloor
        self.MinFloor = minFloor
        self.ElevAmount = elevAmount
def Fire():
    print(len(ElevList))
    for i in range(len(ElevList)):
        Elevator(i + 1).CurrentFloor = 0
        print(f"Elevator {Elevator (i + 1).Index} in safe zone at floor {Elevator(i + 1).CurrentFloor}")
class Elevator:
    CurrentFloor = 0
    Index = 0
    def __init__(self, index):
        self.Index = index
    def FloorUp(self, amount):
        for i in range(amount):
            if self.CurrentFloor != Building.MaxFloor:
                self.CurrentFloor += 1
                print (f"floor: {self.CurrentFloor}, elevator: {self.Index}")
    def FloorDown(self, amount):
        for i in range(amount):
            if self.CurrentFloor != Building.MinFloor:
                self.CurrentFloor -= 1
                print (f"floor: {self.CurrentFloor}, elevator: {self.Index}")
def createElevator(amount):
    for i in range(amount):
        elevator = Elevator(i)
        ElevList.append(elevator)
createElevator(2)
Elevator(1).FloorUp(10)
Elevator(1).FloorDown(1)
Elevator(2).FloorUp(11)
Elevator(2).FloorDown(1)
Fire()