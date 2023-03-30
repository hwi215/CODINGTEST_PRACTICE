n = int(input())

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1 # 방문체크

    # 커브 방향 넣기
    curve = [d] # 처음 방향
    for i in range(g): # 세대만큼 반복
        for j in range(len(curve)-1, -1, -1):
            curve.append((curve[j]+1) % 4) # 0 1 2 3

    # 커브 방향에 따라 드래곤 커브 만들기
    for i in range(len(curve)):
        x += dx[curve[i]]
        y += dy[curve[i]]
        if x < 0 or x >= 101 or y < 0 or y >= 101: # 범위 벗어나면 무시
            continue

        graph[x][y] = 1 # 방문체크


answer = 0

for i in range(100):
    for j in range(100):
        if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
            answer += 1

print(answer)
