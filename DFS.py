

marked = [False] * G.size()


def dfs(G, v):
    visit(v)
    marked[v] = True
    for w in G.neighbours(v):
        if not marked[w]:
            dfs(G, w)

