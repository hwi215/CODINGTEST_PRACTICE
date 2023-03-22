# 점수 찾기
# bfs
import sys
from collections import deque
input = sys.stdin.readline

# 동남서북(시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, target):
    check[x][y] = 1 # 방문체크
    q.append([x, y])
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4): # 동남서북
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: # 범위 내에 존재
                if check[nx][ny] == 0 and graph[nx][ny] == target: # 방문하지 않았고, 현재 위치 값과 같은지 확인(동일한 연속되는 값 찾기 위해서)
                    count += 1
                    check[nx][ny] = 1 # 방문체크
                    q.append([nx, ny])

    return count # 동일한 값을 가진 칸의 갯수 반환

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

x, y, dir = 0, 0, 0
answer = 0
dic = [1, 2, 3, 4, 5, 6] # 주사위

for _ in range(k): # k번 반복
    # 범위 벗어나는 경우 -> 반대방향으로 바꾸기
    if not 0 <= x + dx[dir] < n or not 0 <= y + dy[dir] < m:
        dir = (dir + 2) % 4 # 반대방향으로 바꾸기

    # 범위 안에 있는 경우
    x, y = x + dx[dir], y + dy[dir]

    q = deque()
    check = [[0] * m for _ in range(n)] # 방문체크 행렬

    answer += (bfs(x, y, graph[x][y]) + 1) * graph[x][y] # count(본인꺼 하나 더해주기) * 값

    if dir == 0: # 동
        dic[0], dic[1], dic[2], dic[3], dic[4], dic[5] = dic[3], dic[1], dic[0], dic[5], dic[4], dic[2]
    elif dir == 1: # 남
        dic[0], dic[1], dic[2], dic[3], dic[4], dic[5] = dic[1], dic[5], dic[2], dic[3], dic[0],dic[4]
    elif dir == 2: # 서
        dic[0], dic[1], dic[2], dic[3], dic[4], dic[5] = dic[2], dic[1], dic[5], dic[0], dic[4], dic[3]
    else: # 북
        dic[0], dic[1], dic[2], dic[3], dic[4], dic[5] = dic[4], dic[0], dic[2], dic[3], dic[5], dic[1]


    if dic[5] > graph[x][y]: # 주사위 맨 마지막 숫자 > 해당 위치 숫자: 시계방향으로 90도
        dir = (dir + 1) % 4
    elif dic[5] < graph[x][y]: # 주사위 맨 마지막 숫자 < 해당 위치 숫자: 반시계방향으로 90도
        dir = (dir + 3) % 4


print(answer)





