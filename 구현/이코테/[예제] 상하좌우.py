n = int(input())
moves = list(map(str, input().split()))

x, y = 1, 1 # 처음 위치 초기화

# L R U D 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for move in moves:
    for i in range(4):
        if move == move_type[i]:
            nx = x + dx[i] # 이동 후 위치 확인
            ny = y + dy[i]

    # 공간 벗어난 경우
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    #else:
    x = nx
    y = ny

print(x, y)


