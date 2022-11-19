import numpy as np
from collections import deque


def uniform_cost_search(initial_board):
    print('=*=*=*=*=*=*=*=*=*Uniform Cost Search=*=*=*=*=*=*=*=*=*=*=*')
    visited_boards = set()
    to_visit_boards = deque([initial_board])

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
            if board.can_move_left(vehicle):
                board1 = board.__copy__()
                board1.cost = board.cost + 1
                while board1.can_move_left(vehicle):
                    board1.move_left(vehicle)
                    try:
                        i = to_visit_boards.index(board1)
                        if i and board1.cost < to_visit_boards[i].cost:
                            to_visit_boards[i] = board1.__copy__()
                    except ValueError:
                        to_visit_boards.append(board1.__copy__())

            if board.can_move_right(vehicle):
                board2 = board.__copy__()
                board2.cost = board.cost + 1
                while board2.can_move_right(vehicle):
                    board2.move_right(vehicle)
                    try:
                        i = to_visit_boards.index(board2)
                        if i and board2.cost < to_visit_boards[i].cost:
                            to_visit_boards[i] = board2.__copy__()
                    except ValueError:
                        to_visit_boards.append(board2.__copy__())

            if board.can_move_up(vehicle):
                board3 = board.__copy__()
                board3.cost = board.cost + 1
                while board3.can_move_up(vehicle):
                    board3.move_up(vehicle)
                    try:
                        i = to_visit_boards.index(board3)
                        if i and board3.cost < to_visit_boards[i].cost:
                            to_visit_boards[i] = board3.__copy__()
                    except ValueError:
                        to_visit_boards.append(board3.__copy__())

            if board.can_move_down(vehicle):
                board4 = board.__copy__()
                board4.cost = board.cost + 1
                while board4.can_move_down(vehicle):
                    board4.move_down(vehicle)
                    try:
                        i = to_visit_boards.index(board4)
                        if i and board4.cost < to_visit_boards[i].cost:
                            to_visit_boards[i] = board4.__copy__()
                    except ValueError:
                        to_visit_boards.append(board4.__copy__())

            if board.can_remove(vehicle):
                board5 = board.__copy__()
                board5.remove(vehicle)
                try:
                    i = to_visit_boards.index(board5)
                    if i and board5.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = board5
                except ValueError:
                    to_visit_boards.append(board5)