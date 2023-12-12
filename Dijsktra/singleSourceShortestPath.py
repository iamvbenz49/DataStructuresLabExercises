import heapq

def djikstra(graph,node):
    dist = {vertex:1e7 for vertex in graph}
    dist[node] = 0
    pq = [(dist[node],node)]
    while pq:
        node_dis,node = heapq.heappop(pq)
        print(node_dis,node)
        for vertex,weight in graph[node].items():
            if dist[node]+weight<dist[vertex]:
                dist[vertex] = dist[node]+weight 
                heapq.heappush(pq,(dist[vertex],vertex))
    return dist
graph = {
    "v1":{"v2":2,"v4":1},
    "v2":{"v4":3,"v5":10},
    "v3":{"v1":4},
    "v4":{"v3":2,"v6":8,"v7":4,"v5":2},
    "v5":{"v7":6},
    "v6":{"v3":5},
    "v7":{"v6":1}
}
print(djikstra(graph,"v1"))