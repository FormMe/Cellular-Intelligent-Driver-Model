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
        head = self.coords[-1]
        dist = -1
        front_id = -1
        for i in range(1, road.length + 1):
            pos = (head + i) % road.length
            carFound = road.map[self.lane][pos] != 0
            if carFound:
                front_id = road.map[self.lane][pos]
                dist = pos - head if pos > head else road.length - head + pos
                break

        # print(dist, front_id, self.__dict__)
        if dist >= 0 and front_id != self.v_id:
            if dist - self.velocity <= self.distance:
                self.velocity = 0
            elif self.velocity <= self.maxVelocity:
                self.velocity = max(self.velocity + self.acceleration, self.maxVelocity)

        for i, pos in enumerate(self.coords):
            self.coords[i] = (pos + self.velocity) % road.length
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