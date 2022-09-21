

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph dict:", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]
        # print(path)
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                start = node
                new_paths = self.get_paths(start, end, path)
                # print(new_paths)
                for p in new_paths:
                    paths.append(p)

        return paths


if __name__ == '__main__':

    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
    ]


    route_graph = Graph(routes)

    # print(route_graph.get_paths('Mumbai', 'Toronto'))

    start = 'Mumbai'
    end = 'Mumbai'
    print()
    print(f'Paths between {start} and {end}:',
          route_graph.get_paths(start, end))



# d = {
#     'Mumbai': ['Paris', 'Dubai'],
#     'Paris': ['Dubai', 'New York']
# }
#
# if 'Paris' in d:
#     print(True)