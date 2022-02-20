

def has_path_iter_BFS(G, src, dst):
    """No way to make BFS recurively"""
    queue = [src]

    while queue:
        current = queue.pop(0)
        if current == dst:
            return True

        for neighbour in G[current]:
            queue.append(neighbour)

    return False


def has_path_rec_DFS(G, src, dst):
    if src == dst:
        return True

    for neighbour in G[src]:
        if has_path_rec_DFS(G, neighbour, dst):
            return True
    return False


# acyclic graph
graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


print(has_path_iter_BFS(graph, 'f', 'k'))
