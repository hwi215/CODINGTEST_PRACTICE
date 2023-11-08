from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
data.sort()

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(s):
    q = deque(data)
    while q:
        virus_num, s_check, x, y = q.popleft()

        if s == s_check:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = virus_num
                q.append((graph[nx][ny], s_check+1, nx, ny))

dfs(s)

print(graph[x-1][y-1])