

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

        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                start = node
                new_paths = self.get_paths(start, end, path)

                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path_dfs(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                start = node
                sp = self.get_shortest_path_dfs(start, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

    def get_shortest_path_bfs(self, start, end, path=[]):

        visited = []

        if start == end:
            return path

        while self.graph_dict[start]:
            s = self.graph_dict[start].pop(0)

            if s in self.graph_dict.keys() or s in self.graph_dict.values():
                for x in self.graph_dict[s]:
                    if x not in visited:
                        visited.append(x)
                        path.append(x)

        start = visited.pop(0)

        return self.get_shortest_path_bfs(start, end)


        # path = []
        # sp = path + [start]
        # for options in self.graph_dict.values():
        #     while options:
        #         start = options.pop(0)
        #         if start == end:
        #             return 'SP found', path
        #         path.append(start)
        #
        #     while path:
        #         change = path.pop(0)
        #
        #         for start in self.graph_dict[change]:
        #             if start == end:
        #                 return 'SP found', path
        #     path = []



if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Mumbai', 'Warsaw'),
        # ('Mumbai', 'New York'),
        ('Warsaw', 'New York'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'London'),
        ('New York', 'Toronto'),
    ]

    route_graph = Graph(routes)

    start = 'Mumbai'
    end = 'Toronto'
    print()
    # print(f'Shortest path between {start} and {end} by DFS:',
    #       route_graph.get_shortest_path_dfs(start, end))

    print(f'Shortest path between {start} and {end} by BFS:',
          route_graph.get_shortest_path_bfs(start, end))

    # print(f'Paths between {start} and {end}:',
    #       route_graph.get_paths(start, end))

