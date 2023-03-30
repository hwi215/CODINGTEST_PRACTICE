import sys
from itertools import combinations

input = sys.stdin.readline
# 행, 렬 수 받기
n, m = map(int, input().split())

# 행렬 받기
maps = []
for i in range(n):
  maps.append(list(map(int, input().split())))

house = []      # 집의 좌표
chick = []      # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1: #집
            house.append([i, j])
        elif maps[i][j] == 2: #치킨집
            chick.append([i, j])

result = 999999

# 조합으로 m개 치킨집 선택
for chi in combinations(chick, m):
    temp = 0            # 도시의 치킨 거리(모든 치킨거리 합)
    for h in house:
        chi_len = 999   # 각 집마다 치킨 거리
        for j in range(m):
             # 작은거리로 업뎃
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len # 모든 치킨 거리 합
    result = min(result, temp) # 경우에 따른 최소 거리

print(result)