#import sys
from collections import deque

def is_move(x, y): # 이동 가능한 범위인지 확
    return x >= 0 and y >= 0 and x < n and y < m

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft() # 큐에서 꺼내기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_move(nx, ny) == True and graph[nx][ny] == 1: # 이동 가능 확인
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 # 해당 자리에 이동 경우의 수 누적하기

    return graph[n-1][m-1]

#input = sys.stdin.readline
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().strip()))) # strip으로 쪼개기

#graph = [list(map(int, input())) for _ in range(n)]


print(bfs(0, 0))


