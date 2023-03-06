# dfs
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
 

# dfs로 모든 노드 방문
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 범위 벗어나는 경우
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        # 상하좌우 방문
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1

print(answer)