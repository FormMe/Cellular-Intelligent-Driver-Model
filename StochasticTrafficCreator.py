from numpy import random

from Vehicle import Vehicle
from RoadHandler import Road


class StochasticTrafficCreator:
    def __init__(self):
        self.carCount = 8
        self.truckCount = 6

        self.sizeVelCarDist = random.randint(1, 3, self.carCount)
        self.sizeVelTruckDist = random.randint(3, 5, self.truckCount)

        self.distanceVelCarDist = random.randint(1, 3, self.carCount)
        self.distanceVelTruckDist = random.randint(2, 4, self.truckCount)

        self.accCarDist = random.randint(1, 4, self.carCount)
        self.accTruckDist = random.randint(1, 3, self.truckCount)

        self.startVelCarDist = random.randint(0, 2, self.carCount)
        self.startVelTruckDist = random.randint(0, 2, self.truckCount)

        self.maxVelCarDist = random.randint(1, 6, self.carCount)
        self.maxVelTruckDist = random.randint(1, 4, self.truckCount)

        self.reactCarDist = random.randint(2, 3, self.carCount)
        self.reactTruckDist = random.randint(2, 3, self.truckCount)

    def create_vehicles(self):
        vehicles = []
        for size, acc, distance, \
            startVel, maxVel, react in zip(self.sizeVelCarDist, self.accCarDist, self.distanceVelCarDist,
                                           self.startVelCarDist, self.maxVelCarDist, self.reactCarDist):
            v = Vehicle(v_id=len(vehicles)+1,
                        size=size,
                        acceleration=acc,
                        distance=distance,
                        startVelocity=startVel,
                        maxVelocity=maxVel,
                        reaction=1,
                        type="Car")
            # v.__class__ = Car
            vehicles.append(v)

        for size, acc, distance, \
            startVel, maxVel, react in zip(self.sizeVelTruckDist, self.accTruckDist, self.distanceVelTruckDist,
                                           self.startVelTruckDist, self.maxVelTruckDist, self.reactTruckDist):
            v = Vehicle(v_id=len(vehicles)+1,
                        size=size,
                        acceleration=acc,
                        distance=distance,
                        startVelocity=startVel,
                        maxVelocity=maxVel,
                        reaction=1,
                        type="Truck")
            # v.__class__ = Truck
            vehicles.append(v)

        return vehicles

    def dist_vehicles(self, vehicles, road):
        for v in vehicles:
            while True:
                lane = random.randint(road.lanesCount if v.type == "Car"
                                      else int(road.lanesCount*0.2)+1)
                pos = random.randint(road.length)
                freeSpace = True
                for i in range(v.size + 1):
                    freeSpace = road.map[lane][(pos + i) % road.length] == 0
                    if not freeSpace:
                        break

                if freeSpace:
                    v.lane = lane
                    for i in range(v.size):
                        road.map[lane][(pos + i) % road.length] = v.v_id
                        v.coords.append((pos + i) % road.length)
                    break

