n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
current = [n//2, n//2] # 현재 좌표 (x, y)
# 왼쪽방향
left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left] #오른쪽방향으로 퍼질때
down = [(-y, x, z) for x, y, z in left] #아래쪽 방향으로 퍼질때
up = [(-x, y, z) for x, y, z in down]  #위쪽방향으로 퍼질때
rate = {'left': left, 'right': right, 'down': down, 'up': up}

def move(count, dx, dy, direction):
    global answer
    for _ in range(count + 1):
        # 현재 좌표 업데이트
        current[0], current[1] = current[0] + dx, current[1] + dy
        # 범위 초과
        if current[0] < 0 or current[1] < 0:
            break

        sum = 0 # 퍼진 값 누적 값
        for dx, dy, r in rate[direction]: # 퍼지는 모래 계산
            nx, ny = current[0] + dx, current[1] + dy
            if r == 0: # 퍼지지 않는 모래는 현재 자리에 누적하기
                sand = graph[current[0]][current[1]] - sum
            else: # 퍼지는 모래 계산
                sand = int(graph[current[0]][current[1]] * r)

            if 0 <= nx < n and 0 <= ny < n: # 범위 내에 존재하면
                graph[nx][ny] += sand
            else: # 범위 밖 - 정답 누적값 업데이트
                answer += sand
            sum += sand # 퍼지는 모래 누적값


for i in range(n):
    if i % 2 == 0: # 짝수면
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    else:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')

print(answer)
