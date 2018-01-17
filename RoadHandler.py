import numpy as np

from Vehicle import IVehicle, Car, Bus, Truck

class Road:
    def __init__(self, lanesCount, length):
        self.map = np.zeros((lanesCount, length))


class RoadHandler:
    def __init__(self, road, vehicles):
        self.road = road
        self.vehicles = vehicles

    def update_road(self):
        pass

    def step(self):
        for v in self.vehicles:
            v.step()
        self.update_road()
