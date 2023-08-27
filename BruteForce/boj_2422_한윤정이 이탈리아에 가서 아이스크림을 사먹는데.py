# 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

# 조합 다 구하고 제거하니까 시간초과 남

n, m = map(int, input().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

count = 0

# 테케 크기가 작아서, 그냥 3중 for문 돌리면서 체크하기
for i in range(1, n+1):
    for j in range(i+1, n+1):
        for k in range(j+1, n+1):
            # 섞으면 안되는 조합이 없는 경우
            if graph[i][j] != 1 and graph[j][k] != 1 and graph[i][k] != 1:
                count += 1


print(count)



