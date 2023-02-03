import heapq
from collections import defaultdict
#중요: heapq에 push를 할 때 튜플을 사용할 경우 튜플의 첫 번째 항목을 기준으로 우선순위를 가지게 된다.
V, E = map(int, input().split())
visited = [0]*(V+1)
S = [1]
visited[1] = 1
heap_q = []
sum = 0
edge_table = defaultdict(list)
for i in range(E):
    A, B, C = map(int, input().split())
    edge_table[A].append((B, C))
    edge_table[B].append((A, C))

    if 1 < i <= V:
        heapq.heappush(heap_q, (1000001, i))
        
for pair in edge_table[1]:
    heapq.heappush(heap_q, (pair[1], pair[0]))

while len(S) < V:
    least = heapq.heappop(heap_q)
    if visited[least[1]] == 0: #이미 집합에 포함되어 있는지 확인
        sum += least[0]
        S.append(least[1])
        visited[least[1]] = 1

        for pair in edge_table[least[1]]:
            if visited[pair[0]] == 0:
                heapq.heappush(heap_q, (pair[1], pair[0]))

print(sum)
'''
test case
7 9
1 2 8
2 3 10
1 4 9
4 3 5
1 5 11
5 4 13
4 7 12
5 6 8
6 7 7
'''