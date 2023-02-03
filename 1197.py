import heapq
from collections import defaultdict
#중요: heapq에 push를 할 때 튜플을 사용할 경우 튜플의 첫 번째 항목을 기준으로 우선수위를 가지게 된다.
V, E = map(int, input().split())
S = []
heap_q = []
edge_table = defaultdict(list)
for i in range(E):
    A, B, C = map(int, input().split())
    edge_table[A].append((B, C))
    edge_table[B].append((A, C))

    if 1 < i <= V:
        heapq.heappush(heap_q, (1000001, i))



print(heap_q)