import numpy as np

class Vehicle:
    def __init__(self, v_id, size, distance, acceleration, startVelocity, maxVelocity, reaction, type):
        self.v_id = v_id
        self.velocity = startVelocity
        self.distance = distance
        self.maxVelocity = maxVelocity
        self.acceleration = acceleration
        self.size = size
        self.reaction = reaction
        self.collision = -1
        self.lane = None
        self.coords = []
        self.type = type

    def calc_coord(self, road, vehicles):

        #если машина в столкновении она стоит на месте определенное время, потом исчезает
        if self.collision > 0:
            self.collision -= 1
            self.velocity = 0
            if self.collision == 0:
                self.coords = []
            return self.coords, self.lane

        head = self.coords[-1]
        tail = self.coords[0]
        dist = 0
        front_id = -1
        for i in range(1, road.length + 1):
            pos = (head + i) % road.length
            carFound = road.map[self.lane][pos] != 0
            if carFound:
                front_id = road.map[self.lane][pos]
                dist = pos - head - 1 if pos > head else road.length - 1 - head + pos
                break

        # если расстояние с передней машиной стало маленьким
        # в зависимости от того среагировали или нет
        # определяем возможность перестроиться или тормозить
        if dist - self.velocity - self.acceleration < self.distance \
                and np.random.uniform(0, 1) < self.reaction:

            def check_lane(l):
                # нет ли кого то слева прямо сейчас и впереди
                for pos in range(tail, head + self.distance + self.acceleration + 1):
                    near = road.map[l][pos % road.length] == 0
                    if near:
                        return False

                # предсказываем где будет едущая на соседней полосе сздади машина
                # на следующем шаге. если дальше или вблизи, то не перестраиваемся
                for i in range(1, road.length + 1):
                    dist_l = i - 1
                    back_id = road.map[l][head - i]
                    if back_id != 0 and back_id != self.v_id:
                        print(self.v_id, back_id)
                        back_v = [v for v in vehicles if v.v_id == back_id][0]
                        return dist_l - back_v.velocity - back_v.acceleration >= back_v.distance

                return True

            self.velocity = 0
            overtake = False
            # проверяем полосу справа
            if self.lane != road.lanesCount - 1:
                overtake = check_lane(self.lane + 1)

            if overtake:
                self.lane = self.lane + 1
                self.velocity = self.acceleration
            # проверяем полосу слева
            elif self.lane != 0:
                overtake = check_lane(self.lane - 1)
                if overtake:
                    self.lane = self.lane - 1
                    self.velocity = self.acceleration

        #если расстояния достаточно и оно будет не минимальным, ускоряемся
        elif dist - self.velocity != self.distance:
            self.velocity = min(self.velocity + self.acceleration, self.maxVelocity)

        # print(dist, front_id, self.__dict__)
        for i, pos in enumerate(self.coords):
            self.coords[i] = (pos + self.velocity) % road.length

        return self.coords, self.lane
