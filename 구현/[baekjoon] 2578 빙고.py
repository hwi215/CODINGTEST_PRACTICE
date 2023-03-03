import sys

graph = [list(map(int, input().split())) for _ in range(5)]
mc = [list(map(int, input().split())) for _ in range(5)]


def check():
    bingo_count = 0
    # 가로 확인
    for i in range(5):
        if sum(graph[i]) == 0:
            bingo_count += 1
    # 세로 확인
    for i in range(5):
        y = 0
        for j in range(5):
            if graph[j][i] == 0:
                y += 1
        if y == 5:
            bingo_count += 1

    # 대각선 확인(왼쪽위)
    d = 0
    for i in range(5):
        if graph[i][i] == 0:
            d += 1

    if d == 5:
        bingo_count += 1

    # 대각선 확인(오른쪽 위)
    d2 = 0
    for i in range(5):
        if graph[i][4-i] == 0:
            d2 += 1

    if d2 == 5:
        bingo_count += 1


    return bingo_count



count = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            for h in range(5):
                if mc[i][j] == graph[k][h]:
                    graph[k][h] = 0
                    count += 1
                if count >= 12:
                    result = check()
                    if result >= 3:
                        print(count)
                        exit() #코드종료


