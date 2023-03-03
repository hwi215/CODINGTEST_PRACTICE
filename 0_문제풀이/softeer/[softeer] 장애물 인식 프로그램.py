import sys
from collections import deque

answer = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    count = 1
    q = deque()
    q.append((x, y))
    visited[x][y]= True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if not visited[nx][ny] and graph[nx][ny] == '1':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
    answer.append(count)

n = int(sys.stdin.readline())
graph = [input() for _ in range(n)]
