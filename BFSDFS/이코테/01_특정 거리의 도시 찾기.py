# bfs
from collections import deque
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)


visited = [False] * (n+1)
distance = [0] * (n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        target = q.popleft()
        for t in graph[target]:
            if visited[t] == False:
                distance[t] = distance[target] + 1
                q.append(t)
                visited[t] = True

bfs(x)
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)