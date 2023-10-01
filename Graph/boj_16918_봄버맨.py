from collections import deque


# 폭탄있는 곳 찾기
def search_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "O":
                bomb.append((i, j))

# 폭탄 설치되지 않은 곳에 폭탄 설치하기
def search_not_bomb():
    for i in range(r):
        for j in range(c):
            if graph[i][j] != "O":
                graph[i][j] = "O"

# 이동 가능한 범위인지 확인
def is_move(x, y):
    return x >= 0 and y >= 0 and x < r and y < c

# 폭탄 폭발
def bombs():
    while bomb:
        x, y = bomb.popleft()
        graph[x][y] = "."
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_move(nx, ny) and graph[nx][ny] == "O": # 범위에 있고, 폭탄이 설치되어있으면 폭발
                    graph[nx][ny] = "."


r, c, n = map(int, input().split())

graph = [list(map(str, input())) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n -= 1 # 초기에 아무것도 하지 않음

while n > 0:
    bomb = deque()

    search_bomb()

    search_not_bomb() # 3. 폭탄 설치
    n -= 1
    if n == 0:
        break

    bombs() # 4. 폭탄 폭발
    n -= 1


# 출력
for i in range(r):
    print("".join(graph[i]))