class IVehicle:
    def __init__(self, v_id, startVelocity, maxVelocity, acceleration, length, reaction):
        self.v_id = v_id
        self.velocity = startVelocity
        self.maxVelocity = maxVelocity
        self.acceleration = acceleration
        self.length = length
        self.reaction = reaction

    def calc_coord(self):
        pass

    def ident_collision(self):
        pass

    def step(self):
        self.calc_coord()
        self.ident_collision()
        pass


class Car(IVehicle):
    def calc_coord(self):
        print('Car calc')

    def ident_collision(self):
        print('Car coll')


class Bus(IVehicle):
    def calc_coord(self):
        print('Bus calc')

    def ident_collision(self):
        print('Bus coll')


class Truck(IVehicle):
    def calc_coord(self):
        print('Truck calc')

    def ident_collision(self):
        print('Truck coll')