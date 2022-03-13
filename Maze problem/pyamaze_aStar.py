from pyamaze import maze
from queue import PriorityQueue


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2

    return abs(x1 - x2) + abs(y1 - y2)


def aStar(m):
    start = (m.rows, m.cols)
    g_score = {cell:float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start] = h(start, (1, 1))

    open = PriorityQueue()
    open.put((h(start, (1, 1)), h(start, (1, 1)), start))

    while not open.empty():
        currCell = open.get()[2]
        ...



m = maze(5, 5)
m.CreateMaze()



m.run()

























