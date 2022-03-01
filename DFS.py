
def dfs_rec(G, v, visited):

    visited.append(v)
    for v in G[v]:
        dfs_rec(G, v, visited)

    return visited


def dfs_iter(G, v):

    stack = [v]
    visited = []

    while stack:
        current = stack.pop()
        # job...
        if current not in visited:
            visited.append(current)
        for neighbour in G[current][::-1]:
            stack.append(neighbour)

    return visited


if __name__ == '__main__':
    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': ['e'],
             'd': ['f', 'g'],
             'e': [],
             'f': [],
             'g': ['o'],
             'o': []
             }

    print(dfs_iter(graph, 'a'))
