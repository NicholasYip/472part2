import numpy as np


class Board:
    def __init__(self, string, fuel=[]):
        self.state = np.array(string).reshape((6, 6))
        self.fuel = {}
        for row in self.state:
            for el in row:
                if el != ".":
                    self.fuel[el] = 100
        for el in fuel:
            vehicle, fuel_count = list(el)
            self.fuel[vehicle] = fuel_count

    def is_winning_board(self):
        return self.state[2][4] == 'A' and self.state[2][5] == 'A'

    def vehicle_location(self, vehicle):
        coords = []
        for x, y in np.argwhere(self.state == vehicle):
            coords.append((y, x))
        return coords

    def move_left(self, vehicle):

    def move_up(self, vehicle):

    def move_down(self, vehicle):

    def move_right(self, vehicle):

    def remove_vehicle(self, vehicle):
