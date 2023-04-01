# 목표) 바구니에 들어있는 물의 양 합

n, m = map(int, input().split())

graph = []
move = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for _ in range(m):
    temp = list(map(int, input().split()))
    move.append([temp[0]-1, temp[1]]) # 방향은 0부터

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

clouds = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]

for i in range(m):
    # 1. 구름 이동 - d방향으로 s칸 이동
    d, s = move[i][0], move[i][1]
    next_cloud = []

    for x, y in clouds:
        nx = (n + x + int(dx[d]) * int(s)) % n
        ny = (n + y + int(dy[d]) * int(s)) % n
        next_cloud.append([nx, ny])

    # 2. 구름에서 비내림 - 구름 방문 표시, 물 +1
    visited = [[False] * n for _ in range(n)]
    for x, y in next_cloud:
        graph[x][y] += 1
        visited[x][y] = True

    # 3. 구름 모두 사라짐
    clouds = []

    # 4. 물복사 버그 마법 - 대각선 방향으로 물이 있는 바구니 수 만큼 물 증가
    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]
    for x, y in next_cloud:
        count = 0
        for j in range(4):
            nx = x + cx[j]
            ny = y + cy[j]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] >= 1: # 물이 있는 바구니 갯수 찾기
                count += 1
        graph[x][y] += count # 바구니 수 만큼 물의 양 증가

    # 5. 구름 생성 - 물의 양 2 이상인 칸에 구름 생성, 물의 양 -2, 3번에서 구름이 사라진 칸이 아니여야 함
    for j in range(n):
        for k in range(n):
            if graph[j][k] >= 2 and visited[j][k] == False:
                clouds.append([j, k]) # 구름 생성
                graph[j][k] -= 2 # 물의 양 -2


# 물의 양 합 구하기
answer = 0
for i in range(n):
    answer += sum(graph[i])

print(answer)




