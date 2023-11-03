'''
[문제]
꼭 지나야 할 지점이 주어질 때, 이동 경로 개수 구하기(지나는 지점 순서도 일치해야 함)

[문제풀이]
- dfs 완전탐색으로 시작 지점부터 순회
- 꼭 지나야 할 지점을 지나면 다시 dfs 탐색(이때, count 변수로 어떤 지점을 확인해야 할 지 체크)
- 모든 지점을 지난경우 경로의 개수 하나 추가
'''

# dfs 문제

def dfs(x, y, count):
    global answer

    if count == m:
        answer += 1 # 경로 개수 추가
        return

    if spots[count][0] == x and spots[count][1] == y:
        dfs(x, y, count + 1)
        return

    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n: # 유효한 범위 검증
            if graph[nx][ny] == 0 and visited[nx][ny] == False: # 이동 가능한 지 & 처음 방문인지 검증
                dfs(nx, ny, count)
    visited[x][y] = False


n, m = map(int, input().split())

graph = [[] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

spots = []
for i in range(m):
    a, b = map(int, input().split())
    spots.append((a - 1, b - 1)) # 0행 0열 기준으로 변경

answer = 0
dfs(spots[0][0], spots[0][1], 0)

print(answer)
