n = int(input())

graph = [[0 for _ in range(n+1)]]
total = 0

for _ in range(n):
    data = [0] + list(map(int, input().split()))
    total += sum(data)
    graph.append(data)

answer = int(1e9)


def solve(x, y, d1, d2):
    nums = [[0] * (n+1) for _ in range(n+1)] # 구역번호 저장
    people_count = [0] * 5
    nums[x][y] = 5
    # 2번 조건 - 경계 5로 색칠

    for i in range(1, d1+1):
        nums[x+i][y-i] = 5
        nums[x + d2 + i][y + d2 - i] = 5
    for i in range(1, d2+1):
        nums[x+i][y+i] = 5
        nums[x+d1+i][y-d1+i] = 5

    # 3번 조건 - 경계 내부 5로 변경

    # 4번 조건 - 구역번호 설정

    # 1번 선거구
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if nums[r][c] == 5:
                break
            else:
                #nums[r][c] = 1
                people_count[0] += graph[r][c]

    # 2번 선거구
    for r in range(1, x+d2+1):
        for c in range(n, y, -1):
            if nums[r][c] == 5:
                break
            else:
                #nums[r][c] = 2
                people_count[1] += graph[r][c]

    # 3번 선거구
    for r in range(x+d1, n+1):
        for c in range(1, y-d1+d2):
            if nums[r][c] == 5:
                break
            else:
                #nums[r][c] = 3
                people_count[2] += graph[r][c]

    # 4번 선거구
    for r in range(x+d2+1, n+1):
        for c in range(n, y-d1+d2-1, -1):
            if nums[r][c] == 5:
                break
            else:
                #nums[r][c] = 4
                people_count[3] += graph[r][c]

    people_count[4] = total - sum(people_count[0:4])

    return max(people_count) - min(people_count)


for x in range(1, n+1):
    for y in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    answer = min(answer, solve(x, y, d1, d2))

print(answer)