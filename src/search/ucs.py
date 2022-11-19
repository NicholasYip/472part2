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
            temp_board = board.__copy__()

            cost1 = board.cost + 1
            while temp_board.can_move_left(vehicle):
                temp_board.move_left(vehicle)

                board1 = temp_board.__copy__()
                board1.cost = cost1

                try:
                    i = to_visit_boards.index(board1)
                    if i and board1.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = board1
                except:
                    to_visit_boards.append(board1)

            temp_board = board.__copy__()
            cost2 = board.cost + 1
            while temp_board.can_move_right(vehicle):
                temp_board.move_right(vehicle)
                board2 = temp_board.__copy__()
                board2.cost = cost2

                try:
                    i = to_visit_boards.index(board2)
                    if i and board2.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = board2
                except:
                    to_visit_boards.append(board2)

            temp_board = board.__copy__()
            cost3 = board.cost + 1;
            while temp_board.can_move_up(vehicle):
                temp_board.move_up(vehicle)

                board3 = temp_board.__copy__()
                board3.cost = cost3

                try:
                    i = to_visit_boards.index(board3)
                    if i and board3.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = board3
                except:
                    to_visit_boards.append(board3)

            temp_board = board.__copy__()
            cost4 = board.cost + 1
            while temp_board.can_move_down(vehicle):
                temp_board.move_down(vehicle)

                board4 = temp_board.__copy__()
                board4.cost = cost4

                try:
                    i = to_visit_boards.index(board4)
                    if i and board4.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = board4
                except:
                    to_visit_boards.append(board4)

            if board.can_remove(vehicle):
                temp_board = board.__copy__()
                temp_board.remove(vehicle)
                try:
                    i = to_visit_boards.index(temp_board)
                    if i and temp_board.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = temp_board
                except:
                    to_visit_boards.append(temp_board)

    # path = np.empty(len(winning_board))
    #
    # i = len(winning_board) - 1
    # current_board = winning_board
    # while current_board.previous_move is not None:
    #     path[i] = current_board
    #     copy = current_board.__copy__
    #     # if current_board.previous_move[1] == "down":
