import heapq
from collections import defaultdict
#중요: heapq에 push를 할 때 튜플을 사용할 경우 튜플의 첫 번째 항목을 기준으로 우선수위를 가지게 된다.
V, E = map(int, input().split())
S = [1]
heap_q = []
edge_table = defaultdict(list)
for i in range(E):
    A, B, C = map(int, input().split())
    edge_table[A].append((B, C))
    edge_table[B].append((A, C))

    if 1 < i <= V:
        heapq.heappush(heap_q, (1000001, i))
    
#while S == T:
    


print(heap_q)
print(edge_table)

'''
test case
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