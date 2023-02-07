import sys
import heapq
input = sys.stdin.readline
from collections import defaultdict
T = int(input())

INF = 500000001

def dijkstra(start):
    hp = []
    dist = [INF]*(n+1) #최단경로 값 저장 배열
    heapq.heappush(hp, (0, start))
    dist[start] = 0
    

    while(hp):
        distance, vertex = heapq.heappop(hp)

        for v in graph[vertex]:
            dist_update = dist[vertex] + graph[vertex][v]
            if dist_update < dist[v]:
                dist[v] = dist_update                    
                heapq.heappush(hp, (dist[v], v))
        
    return dist

 


for order in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = defaultdict(defaultdict)
    arrv = []
    ans = []

    for _ in range(m):
        a, b, d = map(int, input().split())       
        graph[a][b] = graph[b][a] = d

    for f in range(t):
        arrv.append(int(input()))

    s_dp = dijkstra(s)
    g_dp = dijkstra(g)
    h_dp = dijkstra(h)

    for arrival in arrv:
        if s_dp[g] + graph[g][h] + h_dp[arrival] == s_dp[arrival] or s_dp[h] + graph[g][h] + g_dp[arrival] == s_dp[arrival]:
            ans.append(arrival)
    
    ans.sort()
    print(*ans)
