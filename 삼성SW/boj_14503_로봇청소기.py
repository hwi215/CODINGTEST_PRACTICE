# 목표) 청소하는 칸의 갯수
n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 북서남동 - 반시계방향
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 북동남서 - 0321
d_change = [0, 3, 2, 1]
d = d_change[d]

# left
d_change2 = [1, 2, 3, 0]

visited = [[0] * m for _ in range(n)]

count = 0
while True:

    if graph[r][c] == 0:  # 현재 위치 청소
        graph[r][c] = 2
        count += 1

    ch = 0
    for i in range(4):
        d = d_change2[d]
        nx, ny = r + dx[d], c + dy[d]

        if 0 <= nx < n and 0 <= ny < m:  # 범위 내에 있으면
            if graph[nx][ny] == 0:
                r, c = nx, ny
                ch += 1
                break

    if ch == 0:  # 동서남북에 빈칸 없으면
        nx, ny = r - dx[d], c - dy[d]  # 후진
        # 후진 가능하면
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1:
                break
            else:
                r, c = nx, ny
        else:
            break

print(count)