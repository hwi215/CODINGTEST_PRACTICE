# 목표) 최대 먹을 수 있는 양
# DFS
import copy
import sys
input = sys.stdin.readline

# (0,0)에서 물고기 먹기

# 물고기 순회 완료

# 1) 물고기 순서대로 죄표찾기
def find_fish(graph, fish):
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] == fish:
                return (i, j)

# 2) 모든 물고기 이동
def move_fish(x, y, graph):
    # 1 ~ 16번 순으로 물고기 이동
    for fish_num in range(1, 17):
        # 물고기 좌표 찾기
        position = find_fish(graph, fish_num)
        # 해당 물고기가 존재하는 경우
        if position:
            x_fish, y_fish = position[0], position[1] # 물고기 좌표 리턴받기
            direction = graph[x_fish][y_fish][1] # 먹은 물고기 방향 저장
            # 반시계 방향으로 45도 회전하며 확인
            for _ in range(len(dir)): # 방향 수 만큼 회전해보기
                nx_fish = x_fish + dir[direction][0]
                ny_fish = y_fish + dir[direction][1]
                # 맵 내부에 위치한 경우
                if 0 <= nx_fish < n and 0 <= ny_fish < n:
                    # 이동할 곳에 상어가 없는 경우
                    if not (nx_fish == x and ny_fish == y):
                        # 해당 방향으로 이동
                        graph[x_fish][y_fish][1] = direction # 먹은 물고기 방향으로 바꾸기
                        # 물고기 간에 위치 변경
                        graph[nx_fish][ny_fish],graph[x_fish][y_fish] = graph[x_fish][y_fish], graph[nx_fish][ny_fish]
                        break # 진행 방향이 확정됐으니까 중단
                direction = (direction + 1) % len(dir) # 다음 방향

# 본격적인 상어 사냥 시작

# 1) 상어의 이동가능한 좌표 찾기
def movable_shark(x, y, graph):
    direction = graph[x][y][1] # 상어 진행 방향
    position = []
    for _ in range(n-1):
        # 진행방향으로 전진
        x += dir[direction][0]
        y += dir[direction][1]
        # 진행 후 맵 내부에 있고, 물고기가 존재하는 경우
        if 0 <= x < n and 0 <= y < n and graph[x][y][0] != -1:
            position.append((x, y))
    return position

# 2) 물고기 먹고 상어 탈출할 때 까지 상어 이동

def dfs(x, y, sum, graph):
    global answer
    graph = copy.deepcopy(graph) # 그래프 복사
    # 상어가 해당 물고기 먹음
    sum += graph[x][y][0]
    graph[x][y][0] = -1 # 잡아먹힘 표시하기
    move_fish(x, y, graph) # 모든 물고기 이동
    # 상어가 이동가능한 좌표 리턴받기
    position = movable_shark(x, y, graph)

    # 이동 가능 좌표가 존재하는 경우
    if position:
        for nx, ny in position:
            dfs(nx, ny, sum, graph) # 반복
    else:
        answer = max(answer, sum) # 최대값으로 갱신
        return
if __name__ == '__main__':
    n = 4
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(n):
            # 물고기 번호, 방향 정보 저장
            # 방향 정보 값에 1을 뺀 이유: 진행방향을 저장한 리스트(d)의 값이 인덱스 0부터 시작하기 떄문
            graph[i][j] = [data[2*j], data[2*j+1]-1]

    # 진행방향: 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
    dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    # (0, 0)에서 시작
    x = y = 0
    answer = 0
    dfs(x, y, 0, graph)
    print(answer)

'''
# 입력받기
n = 4
graph = [[0] * n for _ in range(n)]
for i in range(n):
    fish_nums = list(map(int, input().split()))
    for j in range(n):
        # graph = 물고기 번호, 방향
        graph[i][j] = [fish_nums[j*2], fish_nums[j*2+1]-1]

# 방향
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# (0, 0)에서 시작
x, y = 0, 0
answer = 0
dfs(x, y, 0, graph)
print(answer)

'''