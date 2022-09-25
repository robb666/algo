

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
        path = path + [start]
        paths2 = []
        for change in self.graph_dict[start]:
            if end not in self.graph_dict[change]:
                path.append(change)
                # print(path)
                continue

        for start in path:
            if end in self.graph_dict[start]:
                return 'path: ', path
            else:
                paths2.append(self.graph_dict[start])

        for path2 in paths2:
            for start2 in path2:
                if end in self.graph_dict[start2]:
                    print(self.graph_dict[start2], end)
                    return 'path2: ', path2

        return path


if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Mumbai', 'Warsaw'),
        # ('Mumbai', 'New York'),
        ('Warsaw', 'New York'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
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

