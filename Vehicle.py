class Vehicle:
    def __init__(self, v_id, size, acceleration, startVelocity, maxVelocity, reaction):
        self.v_id = v_id
        self.velocity = startVelocity
        self.maxVelocity = maxVelocity
        self.acceleration = acceleration
        self.size = size
        self.reaction = reaction

    def calc_coord(self):
        pass

    def ident_collision(self):
        pass

    def step(self):
        self.calc_coord()
        self.ident_collision()


class Car(Vehicle):
    def calc_coord(self):
        print('Car calc')

    def ident_collision(self):
        print('Car coll')


class Bus(Vehicle):
    def calc_coord(self):
        print('Bus calc')

    def ident_collision(self):
        print('Bus coll')


class Truck(Vehicle):
    def calc_coord(self):
        print('Truck calc')

    def ident_collision(self):
        print('Truck coll')