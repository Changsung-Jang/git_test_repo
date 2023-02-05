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

dist[K] = 0
for vertex in graph[K]:
    heapq.heappush(hp, (graph[K][vertex], vertex)) #거리 초기화
    
while len(hp):
    distance, v = heapq.heappop(hp)
    if dist[v] == 3000001: #dist 값이 매우 크면 방문 안한 것이므로. 값은 작은 순서대로 나오는 것이므로 비교할 필요 X
        dist[v] = distance
        for vertex in graph[v]:
            if dist[v] + graph[v][vertex] < dist[vertex]:
                heapq.heappush(hp, (dist[v] + graph[v][vertex], vertex)) #거리 초기화


#print(dist)
for idx in range(1, len(dist)):
    
    if dist[idx] == 3000001:
        print("INF")
    else:
        print(dist[idx])