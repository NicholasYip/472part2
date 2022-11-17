from queue import PriorityQueue


def queue_contains(board, q):
    if q.empty():
        return False
    return any(board.__eq__(item) for item in q.queue)

# compare cost
def uniform_cost_search(initial_board):
    print('=*=*=*=*=*=*=*=*=*Uniform Cost Search=*=*=*=*=*=*=*=*=*=*=*')
    visited_boards = []
    to_visit_boards = PriorityQueue()
    to_visit_boards.put(initial_board)

    while not to_visit_boards.empty() or len(to_visit_boards) == 0:
        board = to_visit_boards.get()
        visited_boards.append(board)
        if board.is_winning_board():
            print(board.state)
            print(board.cost)
            return board
        possible_distances = [1, 2, 3, 4]
        for col in board.state:
            for vehicle_cell in col:
                if vehicle_cell != '.':
                    for distance in possible_distances:
                        if not board.can_move_down(vehicle_cell, distance):
                            break
                        board1 = board.__copy__()
                        board1.move_down(vehicle_cell, distance)
                        if board1 not in visited_boards and not queue_contains(board1, to_visit_boards):
                            to_visit_boards.put(board1, board1.cost)

                    for distance in possible_distances:
                        if not board.can_move_up(vehicle_cell, distance):
                            break
                        board2 = board.__copy__()
                        board2.move_up(vehicle_cell, distance)
                        if board2 not in visited_boards and not queue_contains(board2, to_visit_boards):
                            to_visit_boards.put(board2)

                    for distance in possible_distances:
                        if not board.can_move_left(vehicle_cell, distance):
                            break
                        board3 = board.__copy__()
                        board3.move_left(vehicle_cell, distance)
                        if board3 not in visited_boards or not queue_contains(board3, to_visit_boards):
                            to_visit_boards.put(board3)

                    for distance in possible_distances:
                        if not board.can_move_right(vehicle_cell, distance):
                            break
                        board4 = board.__copy__()
                        board4.move_right(vehicle_cell, distance)
                        if board4 not in visited_boards and not queue_contains(board4, to_visit_boards):
                            to_visit_boards.put(board4)

                    if board.can_remove_vehicle(vehicle_cell):
                        board5 = board.__copy__()
                        board5.remove_vehicle(vehicle_cell)
                        if board5 not in visited_boards and not queue_contains(board5, to_visit_boards):
                            to_visit_boards.put(board5)

