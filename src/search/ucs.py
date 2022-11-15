from queue import PriorityQueue


def uniform_cost_search(board, visited, priority_queue, current_cost):
    print('=*=*=*=*=*=*=*=*=*Uniform Cost Search=*=*=*=*=*=*=*=*=*=*=*')
    visited = set()
    priority_queue = PriorityQueue()
