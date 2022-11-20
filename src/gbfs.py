import numpy as np
import time
from collections import deque
from queue import PriorityQueue
from src.board import Board


def greedy_best_first_search(board_line, index):
    # f = open('../static/gbfs/gbfs-sol-{}.txt'.format(index), "w")
    # s = open('../static/ucs/gbfs-search-{}.txt'.format(index), "w")
    board_fuel = board_line.strip().split(" ")
    initial_board = Board(list(board_fuel[0]), board_fuel[1:])
    # f.write("Initial board configuration: " + board_line + "\n")
    # f.write(str(initial_board.state) + "\n\n")
    # f.write("Car fuel available: " + str(initial_board.fuel) + "\n\n")
    visited_boards = set()
    # to_visit_boards = deque([initial_board])
    to_visit_boards = PriorityQueue()
    to_visit_boards.put((1, initial_board))
    start = time.time()
    winning_board = None

    while not to_visit_boards.empty():
        board = to_visit_boards.get()[1]
        visited_boards.add(board)
        vehicle_list = list(board.vehicles.keys())
        board.hn = board.h1()

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
                board1.hn = board1.h1()
                board1.fn = board1.gn + board1.hn
                board1.parent = board
                distance = 1
                board1.movement = (vehicle, "left", distance)

                while True:
                    to_visit_boards.put((board1.hn, board1))
                    if not board1.can_move_left(vehicle):
                        break
                    board1 = board1.move_left(vehicle)
                    board1.hn = board1.h1()
                    distance = distance + 1
                    board1.movement = (vehicle, "left", distance)

            if board.can_move_right(vehicle):
                board2 = board.move_right(vehicle)
                board2.gn = board.gn + 1
                board2.hn = board2.h1()
                board2.fn = board2.gn + board2.hn
                board2.parent = board
                distance = 1
                board2.movement = (vehicle, "right", distance)
                while True:
                    to_visit_boards.put((board2.hn, board2))
                    if not board2.can_move_right(vehicle):
                        break
                    board2 = board2.move_right(vehicle)
                    board2.hn = board2.h1()
                    distance = distance + 1
                    board2.movement = (vehicle, "right", distance)

            if board.can_move_up(vehicle):
                board3 = board.move_up(vehicle)
                board3.gn = board.gn + 1
                board3.hn = board3.h1()
                board3.fn = board3.gn + board3.hn
                board3.parent = board
                distance = 1
                board3.movement = (vehicle, "up", distance)
                while True:
                    to_visit_boards.put((board3.hn, board3))
                    if not board3.can_move_up(vehicle):
                        break
                    board3 = board3.move_up(vehicle)
                    board3.hn = board3.h1()
                    distance = distance + 1
                    board3.movement = (vehicle, "up", distance)

            if board.can_move_down(vehicle):
                board4 = board.move_down(vehicle)
                board4.gn = board.gn + 1
                board4.hn = board4.h1()
                board4.fn = board4.gn + board4.hn
                board4.parent = board
                distance = 1
                board4.movement = (vehicle, "down", distance)
                while True:
                    to_visit_boards.put((board4.hn, board4))
                    if not board4.can_move_down(vehicle):
                        break
                    board4 = board4.move_down(vehicle)
                    board4.hn = board4.h1()
                    distance = distance + 1
                    board4.movement = (vehicle, "down", distance)

            if board.can_remove(vehicle):
                board5 = board.remove(vehicle)
                board5.hn = board5.h1()
                board5.fn = board5.gn + board5.hn
                to_visit_boards.put((board5.hn, board5))

    end = time.time()
    print("gbfs time: ", end-start)
    # f.write("\nRuntime: " + str(end - start) + " seconds")

    # for board in visited_boards:
    #     stringified_board = ''
    #     for row in board.state:
    #         for char in row:
    #             stringified_board = stringified_board + (str(char))
    #     s.write("{} {} {} : {} \n".format(board.fn, board.gn, board.hn, stringified_board))
    #
    # if winning_board is not None:
    #     f.write("\nSearch path length: " + str(len(visited_boards)))
    #     f.write("\nSolution path length: " + str(board.gn))
    #     path = [winning_board]
    #     temp = winning_board.parent
    #     #
    #     while temp.parent is not None:
    #         path.append(temp)
    #         temp = temp.parent
    #     path.append(initial_board)
    #     path.reverse()
    #     f.write("\nSolution path: ")
    #     for item in path:
    #         if not item.movement:
    #             continue
    #         movement_str = str(item.movement[0]) + " " + str(item.movement[1]) + " " + str(item.movement[2])
    #         f.write(movement_str + " -> ")
    #     f.write("\n\n")
    #     for item in path:
    #         if item.state is None or not item.movement: continue
    #         grid = ""
    #         for x in item.state:
    #             grid += "".join(x)
    #         item.state = grid
    #         #
    #         movement_str = str(item.movement[0]) + "\t" + str(item.movement[1]) + "\t" + str(item.movement[2])
    #         f.write("{} \t {} {} \n".format(movement_str, str(item.fuel.get(item.movement[0])), str(item.state)))
    #     f.write("\n{}".format(np.array(list(winning_board.state)).reshape((6, 6))))
    # else:
    #     f.write("\n\nNo solution found GG WP ")
    # f.close()
    # s.close()
