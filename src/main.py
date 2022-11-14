import numpy as np

# fileName = input('File name containing the board information to initialize the board: ')
fileName = 'sample-input.txt'
file = open('./static/' + fileName, "r")

for line in file:
    # print(line[0])
    if line[0] == '#' or line == "\n":
        continue
    board_fuel = line.strip().split(" ")
    board = np.array(list(board_fuel[0])).reshape((6, 6))
    fuel = board_fuel[1:]
