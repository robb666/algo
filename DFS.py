import logging


# def dfs_rec(G, v, visited):
#
#     visited.append(v)
#     for v in G[v]:
#         dfs(G, v, visited)
#
#     return visited


def dfs_it(G, v):

    values = []
    values.append(v)
    # while G.values():
    for arr in G.values():
        # values.append(arr)
        while arr:
            # for _ in arr:
                try:
                    v0 = arr.pop(0)
                    values.append(v0)

                    v1 = G[v0].pop(0)
                    values.append(v1)

                    v2 = G[v1].pop(0)
                    values.append(v2)

                    v3 = G[v2].pop(0)
                    values.append(v3)
                except:

                    # print(values)
                    pass

    return values


if __name__ == '__main__':

    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': ['e'],
             'd': ['f', 'g'],
             'e': [],
             'f': [],
             'g': []}
    # marked = [False] * len(graph)
    # print(dfs_rec(graph, 'a', []))
    print(dfs_it(graph, 'a'))



# graph = {'a': ['b', 'c'],
#          'b': ['d'],
#          'c': ['e'],
#          'd': ['f'],
#          'e': [],
#          'f': []}
#
#
# while graph:
#     for v in graph.values():
#         if v:
#             v.pop(0)
#
#
#
# for v in G values,pop(0) if G[values.pop(0)]
#     if v.pop(0) empty then for v in G.pop(0)


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
