from a_star import a_star
from ucs import uniform_cost_search
from gbfs import greedy_best_first_search
import openpyxl
fileName = 'test123.txt'
file = open('../static/' + fileName, "r")

# output to spreadsheet
wb = openpyxl.Workbook()
ws = wb.active
ws.append(["Puzzle Number", "Algorithm", "Heuristic", "Solution Length", "Search Path Length", "Execution Time (sec)"])

i = 0
for line in file:
    if line[0] == '#' or line == "\n":
        continue
    i = i + 1
    # uniform_cost_search(line, i, ws)
    # for h in range(1, 5):
    #     greedy_best_first_search(line, i, h, ws)
    for h in range(1, 5):
        a_star(line, i, h, ws)

wb.save('../static/performance_comparison.xlsx')

