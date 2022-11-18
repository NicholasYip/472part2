import numpy as np
from collections import deque


def uniform_cost_search(initial_board):
    print('=*=*=*=*=*=*=*=*=*Uniform Cost Search=*=*=*=*=*=*=*=*=*=*=*')
    visited_boards = set()

    to_visit_boards = deque(np.array([initial_board]))
    possible_distances = [1, 2, 3, 4]
    winning_board = None

    while not len(to_visit_boards) == 0:
        board = to_visit_boards.popleft()
        visited_boards.add(board)
        vehicle_list = sorted(list(board.vehicles.keys()))
        if board.is_winning_board():
            print(board.state)
            print("Cost: ", board.cost)
            print("States: ", len(visited_boards))

            winning_board = board
            break

        for vehicle in vehicle_list:
            for distance in possible_distances:
                if not board.can_move_down(vehicle, distance):
                    break
                board1 = board.__copy__(vehicle, "down", distance)
                board1.move_down(vehicle, distance)

                found = False
                for i, el in enumerate(to_visit_boards):
                    if board1.__eq__(el) and el.cost > board1.cost:
                        to_visit_boards[i] = el
                        found = True
                        break
                if not found:
                    to_visit_boards.append(board1)

            for distance in possible_distances:
                if not board.can_move_up(vehicle, distance):
                    break
                board2 = board.__copy__(vehicle, "up", distance)
                board2.move_up(vehicle, distance)

                found = False
                for i, el in enumerate(to_visit_boards):
                    if board2.__eq__(el) and el.cost > board2.cost:
                        to_visit_boards[i] = el
                        found = True
                        break
                if not found:
                    to_visit_boards.append(board2)

            for distance in possible_distances:
                if not board.can_move_left(vehicle, distance):
                    break
                board3 = board.__copy__(vehicle, "left", distance)
                board3.move_left(vehicle, distance)

                found = False
                for i, el in enumerate(to_visit_boards):
                    if board3.__eq__(el) and el.cost > board3.cost:
                        to_visit_boards[i] = el
                        found = True
                        break
                if not found:
                    to_visit_boards.append(board3)

            for distance in possible_distances:
                if not board.can_move_right(vehicle, distance):
                    break
                board4 = board.__copy__(vehicle, 'right', distance)
                board4.move_right(vehicle, distance)

                found = False
                for i, el in enumerate(to_visit_boards):
                    if board4.__eq__(el) and el.cost > board4.cost:
                        to_visit_boards[i] = el
                        found = True
                        break
                if not found:
                    to_visit_boards.append(board4)

            if board.can_remove_vehicle(vehicle):
                board5 = board.__copy__(vehicle, "add")
                board5.cost = board5.cost - 1
                board5.remove_vehicle(vehicle)

                found = False
                for i, el in enumerate(to_visit_boards):
                    if board5.__eq__(el) and el.cost > board5.cost:
                        to_visit_boards[i] = el
                        found = True
                        break
                if not found:
                    to_visit_boards.append(board5)

    # path = np.empty(len(winning_board))
    #
    # i = len(winning_board) - 1
    # current_board = winning_board
    # while current_board.previous_move is not None:
    #     path[i] = current_board
    #     copy = current_board.__copy__
    #     # if current_board.previous_move[1] == "down":
