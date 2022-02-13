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

    for v in G:
        if v:
            value = G[v].pop(0)
            print(G[value])

            visited.append(G[value])
        # else:


    return visited


if __name__ == '__main__':

    # graph = {'0': {'1', '2'},
    #          '1': {'0', '3', '4', '2'},
    #          '2': {'0'},
    #          '3': {'1'},
    #          '4': {'2', '3'},
    #          '5': {'4'}}

    graph = {'a': ['b', 'c'],
             'b': ['d'],
             'c': ['e'],
             'd': ['f'],
             'e': [],
             'f': []}
    # marked = [False] * len(graph)
    # print(dfs_rec(graph, 'a', []))
    print(dfs_it(graph, 'a'))

