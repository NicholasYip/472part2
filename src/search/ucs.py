import numpy as np
from collections import deque


def uniform_cost_search(initial_board):
    print('=*=*=*=*=*=*=*=*=*Uniform Cost Search=*=*=*=*=*=*=*=*=*=*=*')
    visited_boards = set()
    # tuple (Board, parentBoard, direction, vehicle name, distance)
    tup = (initial_board, None,"null", "null",0) 

    to_visit_boards = deque([tup])

    while not len(to_visit_boards) == 0:
        present = to_visit_boards.popleft()
        board = present[0]
        parent = board
        direction = "LOL"
        vehicle_name = "LOL"
        distance = 0



        visited_boards.add(present)
        vehicle_list = sorted(list(board.vehicles.keys()))

        if board.is_winning_board():
            print(board.state)
            print("Cost: ", board.cost)
            print("States: ", len(visited_boards))
            winning_board = board
            break

        for vehicle in vehicle_list:
            distance = 0
            vehicle_name = vehicle

            temp_board = board.__copy__()
            temp_board.cost = board.cost + 1
            while temp_board.can_move_right(vehicle):
                direction = "right"
                distance = distance + 1
                parent = board

                temp_board.move_right(vehicle)
                board2 = temp_board.__copy__()

                tup = (board2, parent, direction, vehicle_name, distance)
                try:
                    i = to_visit_boards.index(board2)
                    if i and board2.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = tup
                except:
                    to_visit_boards.append(tup)



            temp_board = board.__copy__()
            temp_board.cost = board.cost + 1
            distance = 0
            while temp_board.can_move_up(vehicle):
                direction = "up"
                distance = distance + 1
                parent = board

                temp_board.move_up(vehicle)
                board3 = temp_board.__copy__()

                try:
                    i = to_visit_boards.index(board3)
                    if i and board3.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = tup
                except:
                    tup = (board3, parent, direction, vehicle_name, distance)
                    to_visit_boards.append(tup)



            temp_board = board.__copy__()
            temp_board.cost = board.cost + 1
            distance = 0
            while temp_board.can_move_down(vehicle):
                direction = "down"
                distance = distance + 1
                parent = board

                temp_board.move_down(vehicle)
                board4 = temp_board.__copy__()

                try:
                    i = to_visit_boards.index(board4)
                    if i and board4.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = tup
                except:
                    tup = (board4, parent, direction, vehicle_name, distance)
                    to_visit_boards.append(tup)

            temp_board = board.__copy__()
            temp_board.cost = board.cost + 1
            distance = 0
            while temp_board.can_move_left(vehicle):
                direction = "left"
                distance = distance + 1
                parent = board

                temp_board.move_left(vehicle)
                board1 = temp_board.__copy__()

                try:
                    i = to_visit_boards.index(board1)
                    if i and board1.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = tup
                except:
                    tup = (board1, parent, direction, vehicle_name, distance)
                    to_visit_boards.append(tup)



            if board.can_remove(vehicle):
                temp_board = board.__copy__()
                temp_board.remove(vehicle)
                try:
                    i = to_visit_boards.index(temp_board)
                    if i and temp_board.cost < to_visit_boards[i].cost:
                        to_visit_boards[i] = temp_board
                except:
                    to_visit_boards.append(temp_board)



    print("current:\n",present[0].state)
    print("parent:\n", present[1].state)
    print("Direction: ", present[2], " vehicle: ", present[3], " distance: ", present[4])
    # path = np.empty(len(winning_board))
    # 
    # i = len(winning_board) - 1
    # current_board = winning_board
    # while current_board.previous_move is not None:
    #     path[i] = current_board
    #     copy = current_board.__copy__
    #     # if current_board.previous_move[1] == "down":
