import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = []

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dice = [0] * 6

# 주사위 굴리기
def roll(direction):
    if direction == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[5], dice[2], dice[0]
    elif direction == 2:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[2]
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    else:  # direction == 4
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]


for _ in range(n):
    graph.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

for command in commands:
    nx = x + dx[command-1]
    ny = y + dy[command-1]
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        roll(command)

        if graph[x][y] == 0:
            graph[x][y] = dice[2]
        else:
            dice[2] = graph[x][y]
            graph[x][y] = 0

        print(dice[0])