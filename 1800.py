import heapq
from collections import defaultdict

graph = defaultdict(list)
hp = []
g_cost = 0
N, P, K = map(int, input().split())
for i in range(P):
    n1, n2, cost = map(int, input().split())
    graph[n1].append((n2, cost)) #value tuple들의 첫번째 요소는 연결된 번호, 2번째 요소는 가격
    graph[n2].append((n1, cost)) 
    if 1 < i <= N:
        heapq.heappush(hp, (1000001, 1)) #1000001로 초기화, tuple은 앞의 값을 기준으로 힙에 삽입 -> 가격 먼저

#print(graph)
for pairs in graph[1]:
    heapq.heappush(hp, (pairs[1], pairs[0]))
    