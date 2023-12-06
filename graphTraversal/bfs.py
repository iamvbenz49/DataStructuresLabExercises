graph = {
    'A':['B','C','E'],
    'B':['A','D','E'],
    'C':['A','F','G'],
    'D':['B'],
    'E':['A','B','D'],
    'F':['C'],
    'G':['C']
}

def bfs(graph,start):
    explored = []
    q = [start]
    while q:
        node = q.pop(0)
        if node not in explored:
            explored.append(node)
            for vertex in graph[node]:
                q.append(vertex)
    return explored
print(bfs(graph,'A'))