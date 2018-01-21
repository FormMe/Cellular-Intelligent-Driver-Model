import copy

from RoadHandler import Road, RoadHandler
from StochasticTrafficCreator import StochasticTrafficCreator

road = Road(4, 1000)
creator = StochasticTrafficCreator(car_count=30,
                                   truck_count=int(30*0.2),
                                   car_size=30,
                                   truck_size=100,
                                   acceleration_mean=10, acceleration_sigma=1.5,
                                   car_velocity_mean=190, car_velocity_sigma=30,
                                   truck_velocity_mean=140, truck_velocity_sigma=20,
                                   distance_mean=20, distance_sigma=6,
                                   probability_of_right_driver_reaction_mean=0.95, probability_of_right_driver_reaction_sigma=0.01)
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
                print("_")
            else:
                print(int(pos))
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

print(sum(throughputVals) / float(len(throughputVals)))
print(throughputVals, collisionVals)
