import heapq
def MST(edges,V):
    adj = [[] for i in range(V)]
    for edge in edges:
        adj[edge[0]].append([edge[1],edge[2]])
    sum = 0
    vis = [0]*V
    pq = [(0,0)]
    while pq:
        dis,node = heapq.heappop(pq)
        if not vis[node]:
            vis[node] = 1
            sum += dis
            for vertex,weight in adj[node]:
                if not vis[vertex]:
                    heapq.heappush(pq,(weight,vertex))
    return sum
G = [[0, 2, 4, 1, 0, 0, 0],
     [2, 0, 0, 3, 7, 0, 0],
     [4, 0, 0, 2, 0, 5, 0],
     [1, 3, 2, 0, 7, 8, 4],
     [0, 7, 0, 7, 0, 0, 6],
     [0, 0, 5, 8, 0, 0, 1],
     [0, 0, 0, 4, 6, 1, 0]]
edge = []
for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] !=0:
            edge.append([i,j,G[i][j]])
print(edge)
print(MST(edge,len(G)))