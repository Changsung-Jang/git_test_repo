N = int(input())
T = [0]
P = [0]
dp = [0] * (N+1)
for i in range(N):
    x, y = map(int, input().split())
    T.append(x); P.append(y)

for j in range(1, N+1):
    dp[j] = max(dp[j-1], dp[j])
    next = j+T[j]-1
    if next <= N:
        dp[next] = max(dp[next], dp[j-1]+P[j])

print(dp[N])
