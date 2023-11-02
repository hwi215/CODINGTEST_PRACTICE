n, m = map(int, input().split())

li = [0] + list(map(int, input().split()))  # 인덱스 1로 맞춰서 넣기

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    # 친구 관계 설정
    graph[a].append(b)
    graph[b].append(a)

answer = 0
for i in range(1, n + 1):
    if len(graph[i]) == 0:  # 친구가 없는 경우 자신이 최고라 생각
        answer += 1
    else:
        check = True
        for j in graph[i]:
            if li[i] <= li[j]:  # 나보다 친구가 쎈 경우
                check = False
                break
        if check == True:  # 친구들 중에 내가 제일 쎈 경우
            answer += 1
print(answer)