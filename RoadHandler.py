import numpy as np

from Vehicle import Vehicle, Car, Truck


class Road:
    def __init__(self, lanesCount, length):
        self.lanesCount = lanesCount
        self.length = length
        self.map = np.zeros((lanesCount, length))


class RoadHandler:
    def __init__(self, road, vehicles):
        self.road = road
        self.vehicles = vehicles
        self.lastId = len(vehicles)

    def step(self):
        for v in self.vehicles:
            old_coord = list(v.coords)
            old_lane = int(v.lane)
            new_coord, new_lane = v.calc_coord(self.road, self.vehicles)

            for pos in old_coord:
                self.road.map[old_lane][pos] = 0
            for pos in new_coord:
                self.road.map[new_lane][pos] = v.v_id
