from numpy import random

from Vehicle import IVehicle, Car, Bus, Truck
from RoadHandler import Road


class StochasticTrafficCreator:
    def __init__(self):
        self.carCount = 5
        self.truckCount = 1

        self.accCarDist = random.uniform(3, 2, self.carCount)
        self.accTruckDist = random.uniform(3, 2, self.truckCount)

        self.reactCarDist = random.uniform(3, 2, self.carCount)
        self.reactTruckDist = random.uniform(3, 2, self.truckCount)

        self.startVelCarDist = random.uniform(3, 2, self.carCount)
        self.startVelTruckDist = random.uniform(3, 2, self.truckCount)

        self.maxVelCarDist = random.uniform(3, 2, self.carCount)
        self.maxVelTruckDist = random.uniform(3, 2, self.truckCount)

    def create_vehicles(self):
        vehicles = []
        for _ in zip(self.accCarDist):
            pass
            # v = IVehicle(v_id=len(vehicles),
            #              velocity=0,
            #              acceleration=self.accelerationDist
            #     1, 1, 2)
            # v.__class__ = Car
