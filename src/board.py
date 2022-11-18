import numpy as np
from copy import deepcopy


class Board:
    def __init__(self, string=None, fuel=[]):
        self.cost = 0
        self.fuel = {}
        self.vehicles = {}
        self.previous_move = None

        if string is None:
            self.state = np.array(list("....................................")).reshape((6, 6))
        else:
            self.state = np.array(string).reshape((6, 6))
            for col in self.state:
                for el in col:
                    if el != ".":
                        self.fuel[el] = 100
                        self.vehicles[el] = self.vehicle_location(el)
            for el in fuel:
                vehicle, fuel_count = el
                self.fuel[vehicle] = fuel_count

    def __copy__(self, vehicle=0, movement=0, distance=0):
        copy = Board()
        copy.state = np.array(self.state, copy=True)
        copy.fuel = self.fuel.copy()
        copy.vehicles = self.vehicles.copy()
        copy.previous_move = (vehicle, movement, distance)
        copy.cost = self.cost + 1

        return copy

    def is_winning_board(self):
        return self.state[2][4] == 'A' and self.state[2][5] == 'A'

    def vehicle_location(self, vehicle):
        if vehicle in self.vehicles:
            return self.vehicles[vehicle]
        coords = []
        for x, y in np.argwhere(self.state == vehicle):
            coords.append((x, y))
        return coords

    def vehicle_length(self, vehicle):
        return len(self.vehicle_location(vehicle))

    def is_horizontal(self, vehicle):
        coords = self.vehicle_location(vehicle)
        horizontal = coords[0][0]
        for x, y in coords:
            if x != horizontal:
                return False
        return True

    def is_vertical(self, vehicle):
        coords = self.vehicle_location(vehicle)
        vertical = coords[0][1]
        for x, y in coords:
            if y != vertical:
                return False
        return True

    def can_move_left(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        for i in range(distance):
            for x, y in coords:
                if y < i + 1 or (self.state[x][y - (i + 1)] != '.' and self.state[x][y - (i + 1)] != vehicle):
                    return False
        return self.fuel[vehicle] >= distance and self.is_horizontal(vehicle)

    def move_left(self, vehicle, distance, ):
        coords = self.vehicle_location(vehicle)
        self.vehicles[vehicle] = []
        for x, y in coords:
            self.state[x][y - distance] = vehicle
            self.state[x][y] = '.'
            self.vehicles[vehicle].append((x, y - distance))
        self.fuel[vehicle] = self.fuel[vehicle] - distance

    def can_move_right(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        for x, y in coords:
            if y > 5 - distance or (self.state[x][y + distance] != '.' and self.state[x][y + distance] != vehicle):
                return False
        return self.fuel[vehicle] >= distance and self.is_horizontal(vehicle)

    def move_right(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        self.vehicles[vehicle] = []
        for x, y in reversed(coords):
            self.state[x][y + distance] = vehicle
            self.state[x][y] = '.'
            self.vehicles[vehicle].append((x, y + distance))
        self.fuel[vehicle] = self.fuel[vehicle] - distance

    def can_move_up(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        for x, y in coords:
            if x < distance or (self.state[x - distance][y] != '.' and self.state[x - distance][y] != vehicle):
                return False
        return self.fuel[vehicle] >= distance and self.is_vertical(vehicle)

    def move_up(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        self.vehicles[vehicle] = []
        for x, y in coords:
            self.state[x - distance][y] = vehicle
            self.state[x][y] = '.'
            self.vehicles[vehicle].append((x - distance, y))
        self.fuel[vehicle] = self.fuel[vehicle] - distance

    def can_move_down(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        for x, y in coords:
            if x > 5 - distance or (self.state[x + distance][y] != '.' and self.state[x + distance][y] != vehicle):
                return False
        return self.fuel[vehicle] >= distance and self.is_vertical(vehicle)

    def move_down(self, vehicle, distance):
        coords = self.vehicle_location(vehicle)
        self.vehicles[vehicle] = []
        for x, y in reversed(coords):
            self.state[x + distance][y] = vehicle
            self.state[x][y] = '.'
            self.vehicles[vehicle].append((x + distance, y))
        self.fuel[vehicle] = self.fuel[vehicle] - distance

    def can_remove_vehicle(self, vehicle):
        coords = self.vehicle_location(vehicle)
        valid_y = [3, 4, 5]
        for x, y in coords:
            if x != 2 or y not in valid_y:
                return False
        return True

    def remove_vehicle(self, vehicle):
        coords = self.vehicle_location(vehicle)
        for x, y in coords:
            self.state[x][y] = '.'
        self.vehicles.pop(vehicle)
        self.fuel.pop(vehicle)

    def __eq__(self, board):
        for i, col in enumerate(self.state):
            for j, el in enumerate(col):
                if board.state[i][j] != el:
                    return False
        return True

    def h1(self):
        a_coords = self.vehicle_location('A')
        right_position = a_coords[1][1] + 1
        blocking_vehicles = set()

        while right_position < 6:
            if self.state[2][right_position] != '.':
                blocking_vehicles.add(self.state[2][right_position])
            right_position = right_position + 1
        return len(blocking_vehicles)

    def h2(self):
        a_coords = self.vehicle_location('A')
        right_position = a_coords[1][1] + 1
        blocked_position = 0

        while right_position < 6:
            if self.state[2][right_position] != '.':
                blocked_position = blocked_position + 1
            right_position = right_position + 1

        return blocked_position

    def h3(self, constant):
        return constant * self.h1()

    def h4(self):
        heuristic = 0
        a_coords = self.vehicle_location('A')
        right_position = a_coords[1][1] + 1
        while right_position < 6:
            current_cell = self.state[2][right_position]
            if current_cell == '.':
                right_position = right_position + 1
                continue
            is_vertical = self.is_vertical(current_cell)
            if is_vertical:
                can_move = self.can_move_up(current_cell, 1) or self.can_move_down(current_cell, 1)
                heuristic = heuristic + (1 if can_move else 2)
                right_position = right_position + 1
            elif not is_vertical:
                can_move = self.can_move_right(current_cell, 1) or self.can_remove_vehicle(current_cell)
                heuristic = heuristic + (1 if can_move else 2)
                right_position = right_position + self.vehicle_length(current_cell)
        return heuristic
