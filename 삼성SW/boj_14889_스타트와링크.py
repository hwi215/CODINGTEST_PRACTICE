# 목표) 두 팀 점수의 차이 최소값 찾기
# dfs(백트래킹)

import sys
input = sys.stdin.readline

graph = []
n = int(input())
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [False for _ in range(n)]

result = int(1e9)

def dfs(depth, index):
    global result

    # 중단 조건
    if n//2 == depth:
        #print(depth, index)
        sum1, sum2 = 0, 0
        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    sum1 += graph[i][j]
                    sum1 += graph[j][i]
                elif not visited[i] and not visited[j]:
                    sum2 += graph[i][j]
                    sum2 += graph[j][i]

        result = min(result, abs(sum1-sum2))
        return

    # dfs
    for i in range(index, n):
        if not visited[i]:
            visited[i] = True # 방문체크
            dfs(depth+1, i+1)
            visited[i] = False

dfs(0, 0)
print(result)