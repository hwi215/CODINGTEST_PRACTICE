r, c, t = map(int, input().split())
graph = []

for _ in range(r):
    graph.append(list(map(int, input().split())))

x1, x2 = 0, 0
# 공기청정기 위치 찾기
for i in range(r):
    if graph[i][0] == -1: # 항상 1번 열
        x1, x2 = i, i+1
        break

# 1) 미세먼지 확산
def spread():
    # 반시계방향 - 상좌하우
    dy = [0, -1, 0, 1]
    dx = [-1, 0, 1, 0]

    graph_spread = [[0] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                sum_spr = 0
                spr = graph[i][j] // 5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        graph_spread[nx][ny] += spr # 확산
                        sum_spr += spr
                graph[i][j] -= sum_spr # 확산된 미세먼지 양만큼 빼주기

    for i in range(r):
        for j in range(c):
            graph[i][j] += graph_spread[i][j]


# 2) 공기청정기 바람 이동 - 위쪽(시계방향) - 우상좌하
def air_up():
    dy = [1, 0, -1, 0]
    dx = [0, -1, 0, 1]
    x, y = x1, 1
    d = 0
    before = 0
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if x == x1 and y == 0: # 제자리로 복귀하는 경우
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위 벗어나는 경우
            d += 1 # 방향 바꾸기
            continue
        graph[x][y], before = before, graph[x][y]
        x, y = nx, ny


# 3) 공기청정기 바람 이동 - 아래쪽 - 우하좌상
def air_down():
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    x, y = x2, 1
    d = 0
    before = 0
    while True:
        nx, ny = x + dx[d], y + dy[d]
        if x == x2 and y == 0: # 제자리로 복귀하는 경우
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c: # 범위 벗어나는 경우
            d += 1 # 방향 바꾸기
            continue
        graph[x][y], before = before, graph[x][y]
        x,y = nx, ny


for _ in range(t):
    spread()
    air_up()
    air_down()

answer = 0

for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            answer += graph[i][j]

print(answer)