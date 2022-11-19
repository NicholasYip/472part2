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
            print("Cost: ", board.gn)
            print("States: ", len(visited_boards))
            winning_board = board
            break

        for vehicle in vehicle_list:

            if board.can_move_left(vehicle):
                board1 = board.move_left(vehicle)
                board1.gn = board.gn + 1
                board1.parent = board
                try:
                    i = to_visit_boards.index(board1)
                    if i and board1.gn < to_visit_boards[i].gn:
                        to_visit_boards[i] = board1
                except ValueError:
                    to_visit_boards.append(board1)

                while board1.can_move_left(vehicle):
                    board1 = board1.move_left(vehicle)
                    board1.parent = board

                    try:
                        i = to_visit_boards.index(board1)
                        if i and board1.gn < to_visit_boards[i].gn:
                            to_visit_boards[i] = board1
                    except ValueError:
                        to_visit_boards.append(board1)

            if board.can_move_right(vehicle):
                board2 = board.move_right(vehicle)
                board2.gn = board.gn + 1
                board2.parent = board

                try:
                    i = to_visit_boards.index(board2)
                    if i and board2.gn < to_visit_boards[i].gn:
                        to_visit_boards[i] = board2
                except ValueError:
                    to_visit_boards.append(board2)

                while board2.can_move_right(vehicle):
                    board2 = board2.move_right(vehicle)
                    board2.parent = board

                    try:
                        i = to_visit_boards.index(board2)
                        if i and board2.gn < to_visit_boards[i].gn:
                            to_visit_boards[i] = board2
                    except ValueError:
                        to_visit_boards.append(board2)

            if board.can_move_up(vehicle):
                board3 = board.move_up(vehicle)
                board3.gn = board.gn + 1
                board3.parent = board

                try:
                    i = to_visit_boards.index(board3)
                    if i and board3.gn < to_visit_boards[i].gn:
                        to_visit_boards[i] = board3
                except ValueError:
                    to_visit_boards.append(board3)

                while board3.can_move_up(vehicle):
                    board3 = board3.move_up(vehicle)
                    board3.parent = board

                    try:
                        i = to_visit_boards.index(board3)
                        if i and board3.gn < to_visit_boards[i].gn:
                            to_visit_boards[i] = board3
                    except ValueError:
                        to_visit_boards.append(board3)

            if board.can_move_down(vehicle):
                board4 = board.move_down(vehicle)
                board4.gn = board.gn + 1
                board4.parent = board

                try:
                    i = to_visit_boards.index(board4)
                    if i and board4.gn < to_visit_boards[i].gn:
                        to_visit_boards[i] = board4
                except ValueError:
                    to_visit_boards.append(board4)

                while board4.can_move_down(vehicle):
                    board4 = board4.move_down(vehicle)
                    board4.parent = board
                    try:
                        i = to_visit_boards.index(board4)
                        if i and board4.gn < to_visit_boards[i].gn:
                            to_visit_boards[i] = board4
                    except ValueError:
                        to_visit_boards.append(board4)

            if board.can_remove(vehicle):
                board5 = board.remove(vehicle)
                try:
                    i = to_visit_boards.index(board5)
                    if i and board5.gn < to_visit_boards[i].gn:
                        to_visit_boards[i] = board5
                except ValueError:
                    to_visit_boards.append(board5)

    path = [winning_board]
    temp = winning_board.parent

    while(temp.parent is not None):
        path.append(temp)
        temp = temp.parent

    # path.append(initial_board)
    
    #path = path.reverse
    # print(path[0])
    for item in path:
        print("========")
        print(item.state)
    # print(path[-1].state)

# use tuple or dict for movements