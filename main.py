N, M, K = map(int, input().split())
route = [[0]*(N+1) for i in range(N+1)] 
dp = [[-9999]*(N+1) for i in range(N+1)]
visit = [0]*(N+1)
flag = 0
for i in range(K):
    a, b, c = map(int, input().split())
    if route[a][b] < c:
        route[a][b] = c
        
#print(route)
#visit[N] = 1 
#print(visit)

def dfs(city):
    if city == N:
        flag = 1
        visit[city] = 1
        dp[0][city] = 0 
        return

    for next in range(city+1, N+1):
        if route[city][next]: #연결된 도시만 탐색해야 하므로
            if not visit[next]:
                dfs(next)
            
            for i in range(M-1):
                if dp[i][next] >= 0: #있어야 더한다.
                    dp[i+1][city] = max(dp[i+1][city], dp[i][next] + route[city][next])
    
    visit[city] = 1


dfs(1)
maxim = -9999
for index in range(1, M):
    maxim = max(maxim, dp[index][1])

print(maxim)