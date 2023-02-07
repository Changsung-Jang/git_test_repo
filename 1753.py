from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
hp = []
dist = [3000001] * (V+1)
graph = defaultdict(defaultdict) 
for i in range(E):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

heapq.heappush(hp, (0, K))
dist[K] = 0

while(hp):
    distance, vertex = heapq.heappop(hp)

    for v in graph[vertex]:
        dist_update = dist[vertex] + graph[vertex][v]
        if dist_update < dist[v]:
            dist[v] = dist_update                    
            heapq.heappush(hp, (dist[v], v))

#print(dist)
for idx in range(1, len(dist)):
    
    if dist[idx] == 3000001:
        print("INF")
    else:
        print(dist[idx])