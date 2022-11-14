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
            coords.append((x, y))
        return coords

    def can_move_left(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        horizontal = coords[0][0]
        for x, y in coords:
            if y < distance or (self.state[x][y - distance] != '.' and self.state[x][y - distance] != vehicle) or x != horizontal:
                return False
        return self.fuel[vehicle] >= distance

    def move_left(self, vehicle, distance):
        if self.can_move_left(vehicle, distance):
            coords = self.vehicle_location(vehicle)
            for x, y in coords:
                self.state[x][y - distance] = vehicle
                self.state[x][y] = '.'
            self.fuel[vehicle] = self.fuel[vehicle] - distance

    def can_move_right(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        horizontal = coords[0][0]
        for x, y in coords:
            if y > 5 - distance or (self.state[x][y + distance] != '.' and self.state[x][y + distance] != vehicle) or x != horizontal:
                return False
        return self.fuel[vehicle] >= distance

    def move_right(self, vehicle, distance):
        if self.can_move_right(vehicle, distance):
            coords = self.vehicle_location(vehicle)
            for x, y in reversed(coords):
                self.state[x][y + distance] = vehicle
                self.state[x][y] = '.'
            self.fuel[vehicle] = self.fuel[vehicle] - distance

    def can_move_up(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        vertical = coords[0][1]
        for x, y in coords:
            if x < distance or (self.state[x - distance][y] != '.' and self.state[x - distance][y] != vehicle) or y != vertical:
                return False
        return self.fuel[vehicle] >= distance

    def move_up(self, vehicle, distance):
        if self.can_move_up(vehicle, distance):
            coords = self.vehicle_location(vehicle)
            for x, y in coords:
                self.state[x - distance][y] = vehicle
                self.state[x][y] = '.'
            self.fuel[vehicle] = self.fuel[vehicle] - distance

    def can_move_down(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        vertical = coords[0][1]
        for x, y in coords:
            if x > 5 - distance or (self.state[x + distance][y] != '.' and self.state[x + distance][y] != vehicle) or y != vertical:
                return False
        return self.fuel[vehicle] >= distance

    def move_down(self, vehicle, distance):
        if self.can_move_down(vehicle, distance):
            coords = self.vehicle_location(vehicle)
            for x, y in reversed(coords):
                self.state[x + distance][y] = vehicle
                self.state[x][y] = '.'
            self.fuel[vehicle] = self.fuel[vehicle] - distance

    def can_remove_vehicle(self, vehicle):
        coords = self.vehicle_location(vehicle)
        valid_y = [3, 4, 5]
        for x, y in coords:
            if x != 2 and y not in valid_y:
                return False
        return True

    def remove_vehicle(self, vehicle):
        if self.can_remove_vehicle(vehicle):
            coords = self.vehicle_location(vehicle)
            for x, y in coords:
                self.state[x][y] = '.'


