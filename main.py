import copy

from RoadHandler import Road, RoadHandler
from StochasticTrafficCreator import StochasticTrafficCreator

road_length = 2000
lanes_number = 4
road = Road(lanes_number, road_length)
# 1 for normal 4-lane traffic
risk_coefficient = 0.6
creator = StochasticTrafficCreator(car_count=20,
                                   truck_count=int(30*0.2),
                                   car_size=30,
                                   truck_size=100,
                                   acceleration_mean=10 * risk_coefficient, acceleration_sigma=1.5,
                                   car_velocity_mean=190 * risk_coefficient, car_velocity_sigma=30,
                                   truck_velocity_mean=140 * risk_coefficient, truck_velocity_sigma=20,
                                   distance_mean=20 * (2 - risk_coefficient), distance_sigma=6,
                                   probability_of_right_driver_reaction_mean=0.99, probability_of_right_driver_reaction_sigma=0.001)
vehicles = creator.create_vehicles()
creator.dist_vehicles(vehicles, road)
handler = RoadHandler(road, vehicles)
steps_for_statistics = 100
throughputVals = []
throughput = 0
collisionVals = []
collision = 0

number_of_steps = 4000
for s in range(1, number_of_steps + 1):
    for lane in handler.road.map:
        for pos in lane[::10]:
            if pos == 0:
                print("_"),
            else:
                print(int(pos)),
        print("")
    print("step", s)

    prevVehicles = copy.deepcopy(vehicles)
    coll, vehicles = handler.step(s)
    collision += coll
    find_v = lambda pv: len([v for v in vehicles if v.v_id == pv.v_id]) != 0
    prevVehicles = [v for v in prevVehicles if find_v(v)]
    for v, prevV in zip(vehicles, prevVehicles):
        if prevV.coords[-1] > v.coords[-1]:
            throughput += 1

    if s % steps_for_statistics == 0:
        throughputVals.append(throughput)
        throughput = 0
        collisionVals.append(collision)
        collision = 0

print("avg throughput in cars/100 conventional time units", sum(throughputVals) / float(len(throughputVals)))
print("avg collisions in times/100 conventional time units", sum(collisionVals) / float(len(collisionVals)))
print(throughputVals, collisionVals)
