n, m = map(int, input().split())

visited = [[0] * m for i in range(n)] # 방문체크

x, y, d = map(int, input().split())
visited[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

#print(arr)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 시뮬레이션
count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    #if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
        #continue

    if visited[nx][ny] == 0 and arr[nx][ny] == 0: # 방문 안했고 육지면
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: # 회전만 하고 1단계로 돌아가기
        turn_time += 1

    if turn_time == 4:
        # 되돌리기
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][nx] == 0: # 뒤로갈 수 있는 경우
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1