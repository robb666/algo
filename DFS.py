import logging


def dfs_rec(G, v, visited):

    visited.append(v)
    for v in G[v]:
        dfs_rec(G, v, visited)

    return visited




# def dfs_it(G, v):
#
#     stack = [v]
#
#     while len(stack) > 0:
#         current = stack.pop()
#         print(current)
#         for neighbour in G[current][::-1]:
#             stack.append(neighbour)
#
#     return stack


if __name__ == '__main__':
    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': ['e'],
             'd': ['f', 'g'],
             'e': [],
             'f': [],
             'g': []
             }

    print(dfs_rec(graph, 'a', []))













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
