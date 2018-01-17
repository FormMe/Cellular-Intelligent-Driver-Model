class Vehicle:
    def __init__(self, v_id, size, distance, acceleration, startVelocity, maxVelocity, reaction):
        self.v_id = v_id
        self.velocity = startVelocity
        self.distance = distance
        self.maxVelocity = maxVelocity
        self.acceleration = acceleration
        self.size = size
        self.reaction = reaction
        self.collision = False
        self.lane = None
        self.coords = []

    def calc_coord(self, road):

        for i, pos in enumerate(self.coords):
            self.coords[i] = (pos + 1) % road.length
        return self.coords, self.lane



class Car(Vehicle):
    def calc_coord(self):
       pass

    def ident_collision(self):
       pass



class Truck(Vehicle):
    def calc_coord(self):
       pass

    def ident_collision(self):
       pass