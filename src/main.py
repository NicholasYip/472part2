from search.ucs import uniform_cost_search
from board import Board

# fileName = input('File name containing the board information to initialize the board: ')
fileName = 'test.txt'
file = open('./static/' + fileName, "r")

for line in file:
    if line[0] == '#' or line == "\n":
        continue
<<<<<<< HEAD
=======
    board_fuel = line.strip().split(" ")
    board = Board(list(board_fuel[0]), board_fuel[1:])

>>>>>>> badd97af3ea07e8c905d11c8c90a0c41649529cb

board_fuel = line.strip().split(" ")
board = Board(list(board_fuel[0]), board_fuel[1:])
print(board.state)
# print(board.move_down('H', 1))
# print(board.state)



# print("Heuristic 1")
# print(board.h1())
# print("Heuristic 2")
# print(board.h2())
# print("Heuristic 3")
# print(board.h3(2))
print("Heuristic 4")
print(board.h4())
print("DONE")
