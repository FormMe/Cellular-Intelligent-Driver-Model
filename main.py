import os

from Vehicle import Vehicle, Car, Truck
from RoadHandler import Road, RoadHandler
from StochasticTrafficCreator import StochasticTrafficCreator

road = Road(5, 14)
creator = StochasticTrafficCreator()
vehicles = creator.create_vehicles()
creator.dist_vehicles(vehicles, road)
handler = RoadHandler(road, vehicles)

while True:
    handler.step()
    print(handler.road.map, flush=True)
    # for v in handler.vehicles:
    #     print(v.lane, v.coords, v.v_id, v.velocity, v.maxVelocity)
