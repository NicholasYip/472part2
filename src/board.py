import numpy as np
from copy import deepcopy


class Board:
    def __hash__(self):
        return hash(str(self.state))

    def __init__(self, string=None, fuel=[]):
        self.cost = 0
        self.fuel = {}
        self.vehicles = {}

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

        # TODO: OPTIMIZE THIS CODE

    def __copy__(self):
        copy = Board()
        np.copyto(copy.state, self.state)
        copy.fuel = self.fuel.copy()
        copy.vehicles = {key: [x[:] for x in value] for key, value in self.vehicles.items()}
        copy.cost = self.cost
        return copy

    def is_winning_board(self):
        return self.state[2][4] == 'A' and self.state[2][5] == 'A'

    def vehicle_location(self, vehicle):
        coords = []
        for x, y in np.argwhere(self.state == vehicle):
            coords.append([x, y])
        return coords

    def vehicle_length(self, vehicle):
        return len(self.vehicles[vehicle])

    def can_move_left(self, vehicle):
        coords = self.vehicles[vehicle]
        return self.fuel[vehicle] > 0 and coords[0][0] == coords[1][0] and coords[0][1] != 0 and self.state[coords[0][0]][coords[0][1] - 1] == "."

    def move_left(self, vehicle):
        coords = self.vehicles[vehicle]
        self.state[coords[-1][0]][coords[-1][1]] = "."
        self.state[coords[-1][0]][coords[-1][1] - len(coords)] = vehicle
        self.vehicles[vehicle][-1][1] = self.vehicles[vehicle][-1][1] - len(coords)
        self.vehicles[vehicle] = [self.vehicles[vehicle][-1]] + self.vehicles[vehicle][0:-1]
        self.fuel[vehicle] = self.fuel[vehicle] - 1

    def can_move_right(self, vehicle):
        coords = self.vehicles[vehicle]
        return self.fuel[vehicle] > 0 and coords[0][0] == coords[1][0] and coords[-1][1] != 5 and self.state[coords[-1][0]][coords[-1][1] + 1] == "."

    def move_right(self, vehicle):
        coords = self.vehicles[vehicle]
        self.state[coords[0][0]][coords[0][1]] = "."
        self.state[coords[0][0]][coords[0][1] + len(coords)] = vehicle
        self.vehicles[vehicle][0][1] = self.vehicles[vehicle][0][1] + len(coords)
        self.vehicles[vehicle] = self.vehicles[vehicle][1:] + [self.vehicles[vehicle][0]]
        self.fuel[vehicle] = self.fuel[vehicle] - 1

    def can_move_up(self, vehicle):
        coords = self.vehicles[vehicle]
        return self.fuel[vehicle] > 0 and coords[0][1] == coords[1][1] and coords[0][0] != 0 and self.state[coords[0][0] - 1][coords[0][1]] == "."

    def move_up(self, vehicle):
        coords = self.vehicles[vehicle]
        self.state[coords[-1][0]][coords[-1][1]] = "."
        self.state[coords[-1][0] - len(coords)][coords[-1][1]] = vehicle
        self.vehicles[vehicle][-1][0] = self.vehicles[vehicle][-1][0] - len(coords)
        self.vehicles[vehicle] = [self.vehicles[vehicle][-1]] + self.vehicles[vehicle][0:-1]
        self.fuel[vehicle] = self.fuel[vehicle] - 1

    def can_move_down(self, vehicle):
        coords = self.vehicles[vehicle]
        return self.fuel[vehicle] > 0 and coords[0][1] == coords[1][1] and coords[-1][0] != 5 and self.state[coords[-1][0] + 1][coords[-1][1]] == "."

    def move_down(self, vehicle):
        coords = self.vehicles[vehicle]
        self.state[coords[0][0]][coords[0][1]] = "."
        self.state[coords[0][0] + len(coords)][coords[0][1]] = vehicle
        self.vehicles[vehicle][0][0] = self.vehicles[vehicle][0][0] + len(coords)
        self.vehicles[vehicle] = self.vehicles[vehicle][1:] + [self.vehicles[vehicle][0]]
        self.fuel[vehicle] = self.fuel[vehicle] - 1

    def can_remove(self, vehicle):
        coords = self.vehicles[vehicle]
        return coords[-1][0] == 2 and coords[-1][1] == 5 and coords[-2][0] == 2 and coords[-2][1] == 4

    def remove(self, vehicle):
        coords = self.vehicles[vehicle]
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
        a_coords = self.vehicles['A']
        right_position = a_coords[1][1] + 1
        blocking_vehicles = set()

        while right_position < 6:
            if self.state[2][right_position] != '.':
                blocking_vehicles.add(self.state[2][right_position])
            right_position = right_position + 1
        return len(blocking_vehicles)

    def h2(self):
        a_coords = self.vehicles['A']
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
        a_coords = self.vehicles['A']
        right_position = a_coords[1][1] + 1
        while right_position < 6:
            current_cell = self.state[2][right_position]
            if current_cell == '.':
                right_position = right_position + 1
                continue
            is_vertical = a_coords[0][1] == a_coords[1][1]
            if is_vertical:
                can_move = self.can_move_up(current_cell, 1) or self.can_move_down(current_cell, 1)
                heuristic = heuristic + (1 if can_move else 2)
                right_position = right_position + 1
            elif not is_vertical:
                can_move = self.can_move_right(current_cell, 1) or self.can_remove_vehicle(current_cell)
                heuristic = heuristic + (1 if can_move else 2)
                right_position = right_position + self.vehicle_length(current_cell)
        return heuristic
