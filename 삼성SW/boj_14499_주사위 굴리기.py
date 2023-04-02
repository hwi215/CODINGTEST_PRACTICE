import sys

input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = []
# 동: 1 서: 2 북: 3 남: 4
moves = [
    [],
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0]
]

# 아래부터 0, 1, 2, 3, 왼쪽 4, 오른쪽 5
# 주사위의 맨 위: dice[0], 맨 아래: dice[2]
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
    if 0 <= x + moves[command][0] < n and 0 <= y + moves[command][1] < m:
        x, y = x + moves[command][0], y + moves[command][1]
        roll(command)

        if graph[x][y] == 0:
            graph[x][y] = dice[2]

        else:
            dice[2] = graph[x][y]
            graph[x][y] = 0

        print(dice[0])