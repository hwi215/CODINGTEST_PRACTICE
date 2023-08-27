def solution(n, computers):
    def dfs(i):
        visited[i] = True

        for j in range(n):
            if not visited[j] and computers[i][j] == 1:
                dfs(j)

    answer = 0
    visited = [False for _ in range(n)]

    for a in range(n):
        if not visited[a]:
            dfs(a)
            answer += 1

    return answer