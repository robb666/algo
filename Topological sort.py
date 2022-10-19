

class Top:

    def __init__(self, graph):
        self.graph = graph

    def sort(self, v, sorted_=[]):

        if v not in sorted_:
            sorted_.append(v)

        node = sorted_[-1]
        print(node)
        if end := self.graph.get(v):
            for airport in end:
                # print(airport)
                if airport:
                    v = self.graph[v].pop()
                    self.sort(v)
                

                return sorted_





di = {'Mumbai': ['Paris', 'Dubai', 'Warsaw'],
      'Warsaw': ['New York'],
      'Paris': ['Dubai', 'New York'],
      'Dubai': ['London'],
      'New York': ['Toronto']}

topo = Top(di)

print(topo.sort('Mumbai'))
