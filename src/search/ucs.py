import numpy as np
from collections import deque


def queue_contains(board, q):
    if q.empty():
        return False
    return any(board.__eq__(item) for item in q.queue)


def uniform_cost_search(initial_board):
    print('=*=*=*=*=*=*=*=*=*Uniform Cost Search=*=*=*=*=*=*=*=*=*=*=*')
    visited_boards = deque(np.array([]))
    to_visit_boards = deque(np.array([initial_board]))
    possible_distances = np.array([1, 2, 3, 4])

    while not len(to_visit_boards) == 0:
        board = to_visit_boards.popleft()
        visited_boards.append(board)
        vehicle_list = np.sort(np.array(list(board.vehicles.keys())))
        if board.is_winning_board():
            print(board.state)
            print(board.cost)
            return board

        for vehicle in vehicle_list:
            for distance in possible_distances:
                if not board.can_move_down(vehicle, distance):
                    break
                board1 = board.__copy__()
                board1.move_down(vehicle, distance)
                if board1 in visited_boards:
                    continue
                else:
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
                board2 = board.__copy__()
                board2.move_up(vehicle, distance)
                if board2 in visited_boards:
                    continue
                else:
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
                board3 = board.__copy__()
                board3.move_left(vehicle, distance)
                if board3 in visited_boards:
                    continue
                else:
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
                board4 = board.__copy__()
                board4.move_right(vehicle, distance)
                if board4 in visited_boards:
                    continue
                else:
                    found = False
                    for i, el in enumerate(to_visit_boards):
                        if board4.__eq__(el) and el.cost > board4.cost:
                            to_visit_boards[i] = el
                            found = True
                            break
                    if not found:
                        to_visit_boards.append(board4)

            if board.can_remove_vehicle(vehicle):
                board5 = board.__copy__()
                board5.cost = board5.cost - 1
                board5.remove_vehicle(vehicle)
                if board5 in visited_boards:
                    continue
                else:
                    found = False
                    for i, el in enumerate(to_visit_boards):
                        if board5.__eq__(el) and el.cost > board5.cost:
                            to_visit_boards[i] = el
                            found = True
                            break
                    if not found:
                        to_visit_boards.append(board5)

