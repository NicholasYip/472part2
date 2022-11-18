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
            while temp_board.can_move_left(vehicle):
                temp_board.move_left(vehicle)

                board1 = temp_board.__copy__()
                board1.cost = board.cost + 1

                if board1 in to_visit_boards and board1.cost < to_visit_boards[to_visit_boards.index(board1)].cost:
                    to_visit_boards[to_visit_boards.index(board1)] = board1
                else:
                    to_visit_boards.append(board1)


                # found = False
                # TODO: Optimize this
                # for i, el in enumerate(to_visit_boards):
                #     if board1.__eq__(el) and el.cost > board1.cost:
                #         to_visit_boards[i] = board1
                #         found = True
                #         break
                # if not found:
                #     to_visit_boards.append(board1)

            temp_board = board.__copy__()
            while temp_board.can_move_right(vehicle):
                temp_board.move_right(vehicle)
                board2 = temp_board.__copy__()
                board2.cost = board.cost + 1

                if board2 in to_visit_boards and board2.cost < to_visit_boards[to_visit_boards.index(board2)].cost:
                    to_visit_boards[to_visit_boards.index(board2)] = board2
                else:
                    to_visit_boards.append(board2)
                # found = False
                # for i, el in enumerate(to_visit_boards):
                #     if board2.__eq__(el) and el.cost > board2.cost:
                #         to_visit_boards[i] = board2
                #         found = True
                #         break
                # if not found:
                #     to_visit_boards.append(board2)

            temp_board = board.__copy__()
            while temp_board.can_move_up(vehicle):
                temp_board.move_up(vehicle)

                board3 = temp_board.__copy__()
                board3.cost = board.cost + 1

                if board3 in to_visit_boards and board3.cost < to_visit_boards[to_visit_boards.index(board3)].cost:
                    to_visit_boards[to_visit_boards.index(board3)] = board3
                else:
                    to_visit_boards.append(board3)
                # board3.cost = board.cost + 1

                # found = False
                # for i, el in enumerate(to_visit_boards):
                #     if board3.__eq__(el) and el.cost > board3.cost:
                #         to_visit_boards[i] = board3
                #         found = True
                #         break
                # if not found:
                #     to_visit_boards.append(board3)

            temp_board = board.__copy__()
            while temp_board.can_move_down(vehicle):
                temp_board.move_down(vehicle)

                board4 = temp_board.__copy__()
                board4.cost = board.cost + 1

                if board4 in to_visit_boards and board4.cost < to_visit_boards[to_visit_boards.index(board4)].cost:
                    to_visit_boards[to_visit_boards.index(board4)] = board4
                else:
                    to_visit_boards.append(board4)
                # found = False
                # for i, el in enumerate(to_visit_boards):
                #     if board4.__eq__(el) and el.cost > board4.cost:
                #         to_visit_boards[i] = board4
                #         found = True
                #         break
                # if not found:
                    # to_visit_boards.append(board4)

            if board.can_remove(vehicle):
                temp_board = board.__copy__()
                temp_board.remove(vehicle)

                found = False
                for i, el in enumerate(to_visit_boards):
                    if temp_board.__eq__(el) and el.cost > temp_board.cost:
                        to_visit_boards[i] = temp_board
                        found = True
                        break
                if not found:
                    to_visit_boards.append(temp_board)

    # path = np.empty(len(winning_board))
    #
    # i = len(winning_board) - 1
    # current_board = winning_board
    # while current_board.previous_move is not None:
    #     path[i] = current_board
    #     copy = current_board.__copy__
    #     # if current_board.previous_move[1] == "down":
