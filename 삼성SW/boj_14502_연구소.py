import sys, copy, collections
input = sys.stdin.readline
n, m = map(int, input().split())
max_num = 0
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

empty_list = []
virus_list = []

# 행렬 n x m 초기화
g = [[0] * m for _ in range(n)]

# 입력 받기
for y in range(n):
    # 행 입력받기
    raw = [int(x) for x in input().split()]

    for x in range(m):
        g[y][x] = raw[x]
        if g[y][x] == 0:
            empty_list.append([y, x])
        if g[y][x] == 2:
            virus_list.append([y, x])


# bfs 탐색
def bfs(ng):
    q = collections.deque([])
    # 방문 리스트
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    global max_num

    for virus in virus_list:
        q.append(virus)

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            # 범위
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            # 안전영역 & 방문하지 않은 곳
            if ng[ny][nx] == 0 and visited[ny][nx] == False:
                q.append([ny, nx])
                ng[ny][nx] = 2
                visited[ny][nx] = True # 방문 체크

    for i in range(n):
        cnt += ng[i].count(0)

    # 큰 값으로 갱신
    if max_num < cnt:
        max_num = cnt


# 벽 세우기(3개)
for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            y1, x1 = empty_list[i]
            y2, x2 = empty_list[j]
            y3, x3 = empty_list[k]

            g[y1][x1] = 1
            g[y2][x2] = 1
            g[y3][x3] = 1

            ng = copy.deepcopy(g)
            bfs(ng)

            g[y1][x1] = 0
            g[y2][x2] = 0
            g[y3][x3] = 0

print(max_num)