from numpy import random

from Vehicle import Vehicle, Car, Truck
from RoadHandler import Road


class StochasticTrafficCreator:
    def __init__(self):
        self.carCount = 8
        self.truckCount = 4

        self.sizeVelCarDist = random.randint(low=1, high=3, size=self.carCount)
        self.sizeVelTruckDist = random.randint(low=3, high=5, size=self.truckCount)

        self.accCarDist = random.uniform(3, 2, self.carCount)
        self.accTruckDist = random.uniform(3, 2, self.truckCount)

        self.startVelCarDist = random.uniform(3, 2, self.carCount)
        self.startVelTruckDist = random.uniform(3, 2, self.truckCount)

        self.maxVelCarDist = random.uniform(3, 2, self.carCount)
        self.maxVelTruckDist = random.uniform(3, 2, self.truckCount)

        self.reactCarDist = random.uniform(3, 2, self.carCount)
        self.reactTruckDist = random.uniform(3, 2, self.truckCount)

    def create_vehicles(self):
        vehicles = []
        for size, acc, startVel, \
            maxVel, react in zip(self.sizeVelCarDist, self.accCarDist,
                                 self.startVelCarDist, self.maxVelCarDist, self.reactCarDist):
            v = Vehicle(v_id=len(vehicles),
                        size=size,
                        acceleration=acc,
                        startVelocity=startVel,
                        maxVelocity=maxVel,
                        reaction=react)
            v.__class__ = Car
            vehicles.append(v)

        for size, acc, startVel, \
            maxVel, react in zip(self.sizeVelTruckDist, self.accTruckDist,
                                 self.startVelTruckDist, self.maxVelTruckDist, self.reactTruckDist):
            v = Vehicle(v_id=len(vehicles),
                        size=size,
                        acceleration=acc,
                        startVelocity=startVel,
                        maxVelocity=maxVel,
                        reaction=react)
            v.__class__ = Truck
            vehicles.append(v)

        return vehicles


    def dist_vehicles(self, vehicles, road):
        for v in vehicles:
            while True:
                lane = random.randint(road.lanesCount)
                pos = random.randint(road.length)
                freeSpace = True
                for i in range(v.size):
                    freeSpace = road.map[lane][(pos + i) % road.length] == 0
                    if not freeSpace:
                        break

                if freeSpace:
                    for i in range(v.size):
                        road.map[lane][(pos + i) % road.length] = v.v_id
                    break


road = Road(5, 14)
creator = StochasticTrafficCreator()
vehicles = creator.create_vehicles()
creator.dist_vehicles(vehicles, road)
print(road.map)