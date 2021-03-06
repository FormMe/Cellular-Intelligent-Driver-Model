from numpy import random
import matplotlib.pyplot as plt

from Vehicle import Vehicle
from RoadHandler import Road


def normal_integers(mu, sigma, size):
    return [int(x) if x > 0 else int(-x) for x in random.normal(mu, sigma, size)]


class StochasticTrafficCreator:
    def __init__(self,
                 car_count, truck_count,
                 car_size, truck_size,
                 acceleration_mean, acceleration_sigma,
                 car_velocity_mean, car_velocity_sigma,
                 truck_velocity_mean, truck_velocity_sigma,
                 distance_mean, distance_sigma,
                 probability_of_right_driver_reaction_mean, probability_of_right_driver_reaction_sigma):

        self.carCount = car_count
        self.truckCount = truck_count

        self.sizeVelCarDist = [car_size] * self.carCount
        self.sizeVelTruckDist = [truck_size] * self.truckCount

        # acceleration in meters per conventional time unit (cars/trucks) (x: acceleration,
        # y: probability density)
        self.accCarDist = normal_integers(acceleration_mean, acceleration_sigma, self.carCount)
        self.accTruckDist = normal_integers(acceleration_mean, acceleration_sigma, self.truckCount)

        # max velocity meters on conventional time unit
        self.maxVelCarDist = normal_integers(car_velocity_mean, car_velocity_sigma, self.carCount)
        self.maxVelTruckDist = normal_integers(truck_velocity_mean, truck_velocity_sigma, self.truckCount)

        self.startVelCarDist = self.maxVelCarDist
        self.startVelTruckDist = self.maxVelTruckDist

        # min distance (meters)
        self.distanceVelCarDist = normal_integers(distance_mean, distance_sigma, self.carCount)
        self.distanceVelTruckDist = normal_integers(distance_mean, distance_sigma, self.truckCount)

        # probability of correct driver reaction
        self.reactCarDist = random.normal(probability_of_right_driver_reaction_mean, probability_of_right_driver_reaction_sigma, self.carCount)
        self.reactTruckDist = random.normal(probability_of_right_driver_reaction_mean, probability_of_right_driver_reaction_sigma, self.truckCount)

    def create_vehicles(self):
        vehicles = []
        for size, acc, distance, \
            startVel, maxVel, react in zip(self.sizeVelCarDist, self.accCarDist, self.distanceVelCarDist,
                                           self.startVelCarDist, self.maxVelCarDist, self.reactCarDist):
            v = Vehicle(v_id=len(vehicles)+1,
                        size=size,
                        acceleration=acc,
                        distance=distance,
                        startVelocity=startVel,
                        maxVelocity=maxVel,
                        reaction=react,
                        type="Car")
            # v.__class__ = Car
            vehicles.append(v)

        for size, acc, distance, \
            startVel, maxVel, react in zip(self.sizeVelTruckDist, self.accTruckDist, self.distanceVelTruckDist,
                                           self.startVelTruckDist, self.maxVelTruckDist, self.reactTruckDist):
            v = Vehicle(v_id=len(vehicles)+1,
                        size=size,
                        acceleration=acc,
                        distance=distance,
                        startVelocity=startVel,
                        maxVelocity=maxVel,
                        reaction=react,
                        type="Truck")
            # v.__class__ = Truck
            vehicles.append(v)

        return vehicles

    def dist_vehicles(self, vehicles, road):
        for v in vehicles:
            while True:
                lane = random.randint(road.lanesCount if v.type == "Car"
                                      else int(road.lanesCount*0.2)+1)
                pos = random.randint(road.length)
                freeSpace = True
                for i in range(v.size + 1):
                    freeSpace = road.map[lane][(pos + i) % road.length] == 0
                    if not freeSpace:
                        break

                if freeSpace:
                    v.lane = lane
                    for i in range(v.size):
                        road.map[lane][(pos + i) % road.length] = v.v_id
                        v.coords.append((pos + i) % road.length)
                    break

