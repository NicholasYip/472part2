import numpy as np

from board import Board
from search.ucs import uniform_cost_search

fileName = 'test.txt'
file = open('../static/' + fileName, "r")

i = 0
for line  in file:
    if line[0] == '#' or line == "\n":
        continue
    i = i + 1
    uniform_cost_search(line, i)
    # print(end - start)

