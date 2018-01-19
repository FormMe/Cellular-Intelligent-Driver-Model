import os

from Vehicle import Vehicle, Car, Truck
from RoadHandler import Road, RoadHandler
from StochasticTrafficCreator import StochasticTrafficCreator

road = Road(5, 28)
creator = StochasticTrafficCreator()
vehicles = creator.create_vehicles()
creator.dist_vehicles(vehicles, road)
handler = RoadHandler(road, vehicles)

while True:
    for lane in handler.road.map:
        for pos in lane:
            print(int(pos), end=" ")
        print("")

    handler.step()
    # for v in handler.vehicles:
    #     print(v.lane, v.coords, v.v_id, v.velocity, v.maxVelocity)
