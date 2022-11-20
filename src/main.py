from board import Board
from ucs import uniform_cost_search
import time
from gbfs import greedy_best_first_search


fileName = 'test.txt'
file = open('../static/' + fileName, "r")

i = 0
for line in file:
    if line[0] == '#' or line == "\n":
        continue
    i = i + 1
    # start_ucs = time.time()
    # uniform_cost_search(line, i)
    # end_ucs = time.time()
    # print("ucs time : ", end_ucs - start_ucs)
    greedy_best_first_search(line, i)

