# 단순 구현 - 백트래킹
from collections import deque

n, k = map(int, input().split())

li = deque(list(map(int, input().split())))
robot = deque([0] * n)

count = 0
while True:
    # 백트레킹
    if li.count(0) >= k: # 내구도가 0인 칸의 개수가 k개 이상이 ㄴ경우
        break

    # 회전
    li.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 # 어차피 로봇 out이므로

    if sum(robot): # 로봇 존재하면
        for i in range(n-2,-1,-1): # 가장 먼저 벨트에 올라간 로봇부터
            if robot[i] == 1 and robot[i+1] == 0 and li[i+1] >= 1:
                robot[i+1] =1
                robot[i] = 0
                li[i+1] -= 1
        robot[-1] = 0 # 어차피 로봇 out이므로

    if robot[0] == 0 and li[0] >= 1: # 로봇 in 가능한 경우
        robot[0] = 1
        li[0] -= 1

    count += 1

print(count)