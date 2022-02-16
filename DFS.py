import logging


# def dfs_rec(G, v, visited):
#
#     visited.append(v)
#     for v in G[v]:
#         dfs(G, v, visited)
#
#     return visited


def dfs_it(G, v):

    visited = []
    visited.append(v)

    for node in G:
        neighbours = G[node]
        if neighbours:
            next = neighbours.pop(0)
            current = G[next]
            visited.append(current)



    return visited


if __name__ == '__main__':

    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': ['e'],
             'd': ['f'],
             'e': [],
             'f': []}
    # marked = [False] * len(graph)
    # print(dfs_rec(graph, 'a', []))
    print(dfs_it(graph, 'a'))



# def dfs_it(G, v):
#
#     visited = []
#     visited.append(v)
#
#     for k in G[v]:
#         for v in k:
#             visited.append(v)
#             if G[v]:
#                 for n in G[v]:
#                     visited.append(n)
#                     if G[n]:
#                         current = G[n].pop(0)
#                         visited.append(current)  # f
#
#     return visited
