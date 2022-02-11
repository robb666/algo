



def dfs(G, v):
    visited = set()
    marked[v] = True
    for w in G:
        if not marked[int(w)]:
            dfs(G, int(w))
        visited.add(w)
    return visited


if __name__ == '__main__':

    graph = {'0': {'1', '2'},
             '1': {'0', '3', '4'},
             '2': {'0'},
             '3': {'1'},
             '4': {'2', '3'},
             '5': {'4'}}

    print(len(graph))

    marked = [False] * len(graph)

    print(marked)

    print(dfs(graph, 0))

