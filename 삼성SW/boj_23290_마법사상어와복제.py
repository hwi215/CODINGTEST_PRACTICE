import copy

f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 물고기 이동
def fish_move():

    fish_graph2 = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + f_dx[i], y + f_dy[i]
                    if (nx, ny) != shark and 0 <= nx < 4 and 0 <= ny < 4 and not smell[nx][ny]:
                        fish_graph2[nx][ny].append(i)
                        break
                else:
                    fish_graph2[x][y].append(d) # 이동할 수 없는 칸이 없으면 이동 X
    return fish_graph2

# 상어 이동
def shark_move(x, y, depth, count, visit):
    global max_eat, shark, eat

    if depth == 3:
        if max_eat < count:
            max_eat = count
            shark = (x, y)
            eat = visit[:]
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit: # 처음 방문 - count에 죽은 물고기 수 추가
                visit.append((nx, ny)) # 방문 체크
                shark_move(nx, ny, depth+1, count + len(temp[nx][ny]), visit)
                visit.pop()
            else: # 이미 방문한 경우
                shark_move(nx, ny, depth+1, count, visit)


m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
graph = [[[] for _ in range(4)] for _ in range(4)]

for f_x, f_y, d in fish:
    graph[f_x-1][f_y-1].append(d-1) # 0부터 시작으로 바꿔서 넣기


smell = [[0] * 4 for _ in range(4)]

shark = tuple(map(lambda x: int(x)-1, input().split()))

for _ in range(s):
    eat = list()
    max_eat = -1
    temp = copy.deepcopy(graph) # 모든 물고기 복제
    temp = fish_move() # 물고기 이동
    shark_move(shark[0], shark[1], 0, 0, list())
    for x, y in eat:
        if temp[x][y]:
            temp[x][y] = []
            smell[x][y] = 3

    # 냄새 사라짐
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1

    # 복제 마법
    for i in range(4):
        for j in range(4):
            graph[i][j] += temp[i][j]


#print(graph)

# 물고기 수 구하기
ans = 0
for i in range(4):
    for j in range(4):
        ans += len(graph[i][j])

print(ans)


