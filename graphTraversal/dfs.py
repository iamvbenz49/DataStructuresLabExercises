graph = {
    'A':['B','C','E'],
    'B':['A','D','E'],
    'C':['A','F','G'],
    'D':['B'],
    'E':['A','B','D'],
    'F':['C'],
    'G':['C']
}

def dfs(graph,start):
    explored = []
    def helper(graph,start):
        if start not in explored:
            explored.append(start)
            for vertex in graph[start]:
                helper(graph,vertex)
    helper(graph,start)
    return explored
print(dfs(graph,'A'))