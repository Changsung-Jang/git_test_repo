K, N = map(int, input().split())
lines = [0]*K
for i in range(K):
    lines[i] = int(input())

lines_sum = sum(lines)
max_lines = max(lines)
init_start = max_lines // N
init_end = lines_sum // N

def bin_search(start, end):
    min = (start + end) // 2
    