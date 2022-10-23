

class Top:

    def __init__(self, connections, _children=()):
        self.graph = {}
        for k, v in connections:
            if k not in self.graph:
                self.graph[k] = []
            if k in self.graph:
                self.graph[k].append(v)

        self.index = {}
        for k, v in connections:
            if k not in self.index or v not in self.index:
                self.index[k] = 0
                self.index[v] = 0

        for k, v in connections:
            if k in self.graph[k] or v in self.graph[k]:
                self.index[v] += 1

        self._prev = set(_children)

        print(self.graph)
        # print(self.index)

    def sortIII(self):

        topo = []
        visited = set()

        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)


    # def sortII(self):
    #
    #     sett = set()
    #     stack = []
    #     root = []
    #
    #     k = None
    #     while self.graph:
    #         for k, v in self.graph.items():
    #             for child in v:
    #                 if child not in self.graph.keys():
    #                     leaf = self.graph[k].pop(self.graph[k].index(child))
    #                     if leaf not in sett:
    #                         stack.append(leaf)
    #                         sett.add(leaf)
    #                     elif k not in v and k not in sett:
    #                         root.append(k)
    #                         sett.add(k)
    #         self.graph.pop(k)
    #     return list(reversed(stack + root))

    # def sortI(self):
    #
    #     arr = []
    #     for k in self.graph:
    #         if self.index[k] == 0:
    #             arr.append(k)
    #             for item in self.graph[k]:
    #                 self.index[item] -= 1
    #             self.index[k] -= 1
    #     for k in self.index:
    #         if self.index[k] == 0:
    #             arr.append(k)
    #     return arr


# di = {'Mumbai': ['Paris', 'Dubai', 'Warsaw'],
#       'Warsaw': ['New York'],
#       'Paris': ['Dubai', 'New York'],
#       'Dubai': ['London'],
#       'New York': ['Toronto']}

# di = [('Mumbai', 'Paris'),
#       ('Mumbai', 'Dubai'),
#       ('Mumbai', 'Warsaw'),
#       ('Warsaw', 'New York'),
#       ('Paris', 'Dubai'),
#       ('Paris', 'New York'),
#       ('Dubai', 'London'),
#       ('New York', 'Toronto'),
#       ]

di = [('A', 'B'),
      ('A', 'C'),
      ('B', 'D'),
      ('B', 'E'),
      ('C', 'D'),
      ('C', 'F'),
      ('D', 'E'),
      ('D', 'F'),
      ]


# di = [
#       ('B', 'C'),
#       ('A', 'C'),
#       ('B', 'D'),
#       ('C', 'E'),
#       ('D', 'F'),
#       ('E', 'H'),
#       ('E', 'F'),
#       ('F', 'G'),
#       ]

topo = Top(di)
print(topo.sortIII())

# print(topo.sortIII())
