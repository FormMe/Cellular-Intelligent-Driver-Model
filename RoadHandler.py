import numpy as np

from Vehicle import Vehicle


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
        self.collision_time = 10

    def step(self, s):
        collisions = 0
        for v in self.vehicles:
            old_coord = list(v.coords)
            old_lane = int(v.lane)
            new_coord, new_lane = v.calc_coord(self.road, self.vehicles)

            for pos in old_coord:
                self.road.map[old_lane][pos] = 0
            for pos in new_coord:
                self.road.map[new_lane][pos] = v.v_id

        self.vehicles = [v for v in self.vehicles if v.coords != []]
        for l in range(self.road.lanesCount):
            for i, v1 in enumerate(self.vehicles):
                # только те машины на линии что еще не в аварии
                if v1.collision == -1 and v1.lane == l:
                    for j, v2 in enumerate(self.vehicles):
                        if v1.v_id != v2.v_id and v2.lane == l:
                            v1_head = v1.coords[-1]
                            v2_head = v2.coords[-1]

                            # если координаты головы машины пересекаются или сзади перередней машины
                            # то значит столкновение произошло
                            if (v1_head + 1) % self.road.length in v2.coords \
                                    or (v2_head + 1) % self.road.length in v1.coords:

                                self.vehicles[i].collision = self.collision_time
                                self.vehicles[j].collision = self.collision_time
                                collisions += 1
                                # print(s, self.vehicles[i].v_id, self.vehicles[i].coords,
                                #       self.vehicles[j].v_id, self.vehicles[j].coords)

        return collisions, self.vehicles