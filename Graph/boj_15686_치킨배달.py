import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())

maps = []
for i in range(n):
  maps.append(list(map(int, input().split())))

houses = [] # 집의 좌표
chickens = [] # 치킨집의 좌표

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1: # 집
            houses.append([i, j])
        elif maps[i][j] == 2: # 치킨 집
            chickens.append([i, j])

result = sys.maxsize

# 조합으로 m개 치킨집 선택
for chicken in combinations(chickens, m):
    tmp = 0  # 모든 치킨 거리 합
    for house in houses:
        chi_len = sys.maxsize # 각 집마다 치킨 거리
        for j in range(m):
            chi_len = min(chi_len, abs(house[0] - chicken[j][0]) + abs(house[1] - chicken[j][1]))
        tmp += chi_len # 모든 치킨 거리 합 갱신
    result = min(result, tmp)

print(result)