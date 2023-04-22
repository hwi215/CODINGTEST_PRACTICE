# bfs 길찾기
from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def in_range(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return False

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if graph[nr][nc] == 0:
                continue
            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1 # 앞에꺼 그대로 받아와서 + 1
                q.append((nr, nc))

    return graph[n-1][m-1] # 맨 마지막 값(도착지점)

print(bfs(0, 0))
print(graph)