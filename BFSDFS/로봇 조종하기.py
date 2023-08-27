# dp
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[-1e9] * m for _ in range(n)]
left = [[-1e9] * m for _ in range(n)]
right = [[-1e9] * m for _ in range(n)]

dp[0][0] = graph[0][0]

for j in range(1, m): # 0행 작업
    dp[0][j] = dp[0][j-1] + graph[0][j]

for i in range(1, n):
    # 왼 -> 오
    left[i][0] = dp[i-1][0] + graph[i][0]
    for j in range(1, m):
        left[i][j] = max(dp[i-1][j] + graph[i][j], left[i][j-1] + graph[i][j])

    # 오 -> 왼
    right[i][m-1] = dp[i-1][m-1] + graph[i][m-1]
    for j in range(m-2, -1, -1):
        right[i][j] = max(dp[i-1][j] + graph[i][j], right[i][j+1] + graph[i][j])

    # merge
    for j in range(m):
        dp[i][j] = max(left[i][j], right[i][j])

print(dp[n-1][m-1])