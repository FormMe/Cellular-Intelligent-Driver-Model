import copy

from RoadHandler import Road, RoadHandler
from StochasticTrafficCreator import StochasticTrafficCreator

road = Road(5, 35)
creator = StochasticTrafficCreator()
vehicles = creator.create_vehicles()
creator.dist_vehicles(vehicles, road)
handler = RoadHandler(road, vehicles)
N = 50
throughputVals = []
throughput = 0
collisionVals = []
collision = 0

for s in range(1, 501):
    for lane in handler.road.map:
        for pos in lane:
            if pos == 0:
                print("_", end="\t")
            else:
                print(int(pos), end="\t")
        print("")
    # print("********************************************************************")

    prevVehicles = copy.deepcopy(vehicles)
    coll, vehicles = handler.step(s)
    collision += coll
    find_v = lambda pv: len([v for v in vehicles if v.v_id == pv.v_id]) != 0
    prevVehicles = [v for v in prevVehicles if find_v(v)]
    for v, prevV in zip(vehicles, prevVehicles):
        if prevV.coords[-1] > v.coords[-1]:
            throughput += 1

    if s % N == 0:
        throughputVals.append(throughput)
        throughput = 0
        collisionVals.append(collision)
        collision = 0

print(throughputVals, collisionVals)
