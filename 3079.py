T = []
N, M = map(int, input().split())
for i in range(N):
    T.append(int(input()))

start = 1; end = min(T) * M
#print("시작은 ", start, end)

while end - start > 1:
    mid = (start + end) // 2
    people = 0
    for control in T:
        people += mid//control
    
    if people < M:
        start = mid + 1
    else:
        end = mid

#print(start, end)
if start == end:
    print(end)
else:
    people = 0
    for control in T:
        people += start//control
    
    if people >= M:
        print(start)
    else:
        print(end)