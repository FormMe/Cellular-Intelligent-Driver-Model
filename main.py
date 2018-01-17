import os

from Vehicle import Vehicle, Car, Truck
from RoadHandler import Road, RoadHandler
from StochasticTrafficCreator import StochasticTrafficCreator

road = Road(5, 14)
creator = StochasticTrafficCreator()
vehicles = creator.create_vehicles()
creator.dist_vehicles(vehicles, road)
handler = RoadHandler(road, vehicles)

for v in handler.vehicles:
    print(v.lane, v.coords, v.v_id)
while True:
    handler.step()
    print(handler.road.map, flush=True)
