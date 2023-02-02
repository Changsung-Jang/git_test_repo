K, N = map(int, input().split())
lines = [0] * K
for i in range(K):
    lines[i] = int(input())

lines_sum = sum(lines)
max_lines = max(lines)

init_start = max_lines // N
init_end = max_lines #랜선 길이 합친 것을 N으로 나눈 것보단 답이 작을 것

maxim = 0 #구하려는 답의 최댓값
def bin_search(start, end):
    global maxim
    numbers = 0 

    if start == end:
        maxim = start
        return
    elif start == end-1: #해당 조건 만들어주지 않으면 무한 루프 생성
        for line in lines:
            numbers += line // end
            if numbers >= N:
                maxim = end
            else:
                maxim = start
        return 

    mid = (start + end) // 2

    for line in lines:
        numbers += line // mid

    if numbers < N: #조각이 적다 -> 길이는 길다
        bin_search(start, mid-1) #최댓값을 찾는 것인데 mid는 만족하지 못하므로 포함 X

    elif numbers >= N:
        bin_search(mid, end) #mid가 최댓값일 수도 있다

bin_search(init_start, init_end)

print(maxim)